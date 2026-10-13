#!/usr/bin/env python3
"""Compare local delivery bytes and, optionally, every PDF page; never write inputs."""

import argparse
import hashlib
import json
from pathlib import Path
import sys


def fingerprint(path):
    digest = hashlib.sha256()
    size = 0
    with path.open('rb') as source:
        for block in iter(lambda: source.read(1024 * 1024), b''):
            digest.update(block)
            size += len(block)
    return {'name': path.name, 'bytes': size, 'sha256': digest.hexdigest()}


def is_prefix(before, after):
    with before.open('rb') as left, after.open('rb') as right:
        for block in iter(lambda: left.read(1024 * 1024), b''):
            if right.read(len(block)) != block:
                return False
    return True


def compare(before, after, pdf=False):
    before, after = Path(before), Path(after)
    if not before.is_file() or not after.is_file():
        raise ValueError('Both inputs must be existing local files')
    left, right = fingerprint(before), fingerprint(after)
    identical = (left['bytes'], left['sha256']) == (right['bytes'], right['sha256'])
    result = {'before': left, 'after': right, 'byte_identical': identical,
              'before_is_prefix_of_after': is_prefix(before, after),
              'same_content': identical, 'content_basis': 'bytes',
              'musical_accuracy_verified': False, 'signature_trust_verified': False}
    if not pdf:
        return result
    try:
        import fitz
    except ImportError as error:
        raise RuntimeError('PDF comparison requires PyMuPDF in the active Python environment') from error
    pages = []
    with fitz.open(before) as original, fitz.open(after) as delivered:
        if not original.is_pdf or not delivered.is_pdf:
            raise ValueError('--pdf requires two PDF files')
        if original.needs_pass or delivered.needs_pass:
            raise ValueError('Encrypted PDFs requiring a password are not supported')
        for number in range(min(len(original), len(delivered))):
            a, b = original[number], delivered[number]
            x, y = a.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False), b.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
            xhash = hashlib.sha256(x.samples).hexdigest()
            yhash = hashlib.sha256(y.samples).hexdigest()
            pages.append({'page': number + 1, 'geometry_equal': a.rect == b.rect,
                          'text_equal': a.get_text() == b.get_text(),
                          'raster_equal': (x.width, x.height, xhash) == (y.width, y.height, yhash),
                          'before_raster_sha256': xhash, 'after_raster_sha256': yhash})
        same = len(original) == len(delivered) and all(
            page['geometry_equal'] and page['text_equal'] and page['raster_equal'] for page in pages)
        result.update(same_content=same, content_basis='all-page geometry, extracted text and RGB raster',
                      pdf={'before_pages': len(original), 'after_pages': len(delivered), 'dpi': 144,
                           'renderer': 'PyMuPDF', 'renderer_version': fitz.VersionBind, 'pages': pages})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('before', type=Path)
    parser.add_argument('after', type=Path)
    parser.add_argument('--pdf', action='store_true', help='Also compare every rendered PDF page (requires PyMuPDF)')
    parser.add_argument('--require-same-content', action='store_true', help='Exit 1 when the selected content comparison differs')
    args = parser.parse_args()
    try:
        result = compare(args.before, args.after, args.pdf)
    except Exception as error:
        print(json.dumps({'error': str(error), 'comparison_completed': False}), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if args.require_same_content and not result['same_content'] else 0


if __name__ == '__main__':
    raise SystemExit(main())

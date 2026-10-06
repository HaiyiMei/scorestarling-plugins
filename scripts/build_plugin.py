"""Build the ScoreStarling plugin ZIP from tracked files in this repository.

The default source is the Git index. --source working-tree builds a local draft from tracked
paths without staging changes. Version and contents always come from the same source.
Entries are sorted, timestamps fixed and file modes taken from Git; manifests sit at the ZIP root.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = ('.github/', 'scripts/', 'tests/', '.gitignore')
MANIFESTS = ('plugin.json', '.claude-plugin/plugin.json')


def version(files):
    contents = {path: content for path, _, content in files}
    versions = {json.loads(contents[name])['version'] for name in MANIFESTS}
    if len(versions) != 1:
        raise SystemExit(f'Plugin manifests disagree on the version: {sorted(versions)}')
    return versions.pop()


def tracked(source='index'):
    # Both sources use tracked paths and index modes; untracked artifacts never enter the ZIP.
    listing = subprocess.run(['git', 'ls-files', '-s', '-z'], cwd=ROOT, check=True,
                             capture_output=True, text=True).stdout
    for entry in sorted(filter(None, listing.split('\0')), key=lambda line: line.split('\t', 1)[1]):
        meta, path = entry.split('\t', 1)
        if path.startswith(EXCLUDED):continue
        mode, blob, stage = meta.split()
        if stage != '0':
            raise SystemExit(f'Unmerged plugin file: {path}')
        file_path = ROOT / path
        if mode not in {'100644','100755'} or (source == 'working-tree' and
                               (file_path.is_symlink() or not file_path.resolve().is_relative_to(ROOT))):
            raise SystemExit(f'Refusing plugin symlink or submodule: {path}')
        if source == 'working-tree':
            content = file_path.read_bytes()
        else:
            content = subprocess.run(['git', 'cat-file', 'blob', blob], cwd=ROOT, check=True, capture_output=True).stdout
        yield path, int(mode, 8) & 0o777, content


def build(out, source='index'):
    files = list(tracked(source))
    target = Path(out) / f'scorestarling-plugin-{version(files)}.zip'
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, 'w') as archive:
        for path, mode, content in files:
            info = zipfile.ZipInfo(path, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100000 | mode) << 16
            archive.writestr(info, content)
    return target


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--out', default=str(ROOT / 'data/releases'), help='Directory for the ZIP (default: data/releases)')
    parser.add_argument('--source', choices=('index', 'working-tree'), default='index',
                        help='Content source: index for CI/releases, working-tree for an unstaged local draft')
    parser.add_argument('--version', action='store_true', help='Print the package version and exit')
    args = parser.parse_args()
    if args.version:
        print(version(list(tracked(args.source))))
    else:
        target = build(args.out, args.source)
        print(target)
        print(hashlib.sha256(target.read_bytes()).hexdigest())

"""Plugin ZIPs use one content source, match their version, exclude untracked files and refuse symlinks."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]


with tempfile.TemporaryDirectory(prefix='scorestarling-plugin-build-') as tmp:
    repo = Path(tmp) / 'repo'
    package = repo
    (package / '.claude-plugin').mkdir(parents=True)
    (repo / 'scripts').mkdir()
    script = repo / 'scripts/build_plugin.py'
    shutil.copy2(ROOT / 'scripts/build_plugin.py', script)
    subprocess.run(['git', '-C', str(repo), 'init', '-q'], check=True, capture_output=True)
    manifests = (package / 'plugin.json', package / '.claude-plugin/plugin.json', package / 'gemini-extension.json')
    for manifest in manifests:
        manifest.write_text(json.dumps({'name': 'scorestarling', 'version': '0.1.0'}))
    readme = package / 'README.md'
    readme.write_text('staged source\n')
    subprocess.run(['git', '-C', str(repo), 'add', '.'], check=True, capture_output=True)

    for manifest in manifests:
        manifest.write_text(json.dumps({'name': 'scorestarling', 'version': '0.1.1', 'developer': 'ScoreStarling'}))
    readme.write_text('working draft\n')
    (package / 'untracked-secret.txt').write_text('fixture that must not be packaged')

    def run(*args, ok=True):
        result = subprocess.run([sys.executable, str(script), *map(str, args)], cwd=ROOT,
                                capture_output=True, text=True)
        if ok:
            assert result.returncode == 0, result.stderr
        else:
            assert result.returncode != 0
        return result

    assert run('--version').stdout.strip() == '0.1.0'
    assert run('--source', 'working-tree', '--version').stdout.strip() == '0.1.1'
    index_result = run('--out', Path(tmp) / 'index')
    index_zip = Path(index_result.stdout.splitlines()[0])
    assert index_zip.name == 'scorestarling-plugin-0.1.0.zip'
    with ZipFile(index_zip) as archive:
        assert json.loads(archive.read('plugin.json'))['version'] == '0.1.0'
        assert archive.read('README.md') == b'staged source\n'
        assert 'untracked-secret.txt' not in archive.namelist()
        assert not any(name.startswith(('scripts/','tests/','.github/')) for name in archive.namelist())
    second_zip = Path(run('--out', Path(tmp) / 'repeat').stdout.splitlines()[0])
    assert second_zip.read_bytes() == index_zip.read_bytes()

    draft_result = run('--source', 'working-tree', '--out', Path(tmp) / 'draft')
    draft_zip = Path(draft_result.stdout.splitlines()[0])
    assert draft_zip.name == 'scorestarling-plugin-0.1.1.zip'
    with ZipFile(draft_zip) as archive:
        assert json.loads(archive.read('plugin.json'))['version'] == '0.1.1'
        assert archive.read('README.md') == b'working draft\n'
        assert 'untracked-secret.txt' not in archive.namelist()
        assert not any(name.startswith(('scripts/','tests/','.github/')) for name in archive.namelist())

    manifests[1].write_text(json.dumps({'name': 'scorestarling', 'version': '0.1.2'}))
    failed = run('--source', 'working-tree', '--out', Path(tmp) / 'mismatch', ok=False)
    assert 'disagree on the version' in failed.stderr
    assert not list((Path(tmp) / 'mismatch').glob('*.zip'))

    manifests[1].write_text(json.dumps({'name': 'scorestarling', 'version': '0.1.1'}))
    outside = Path(tmp) / 'outside.txt'
    outside.write_text('must not follow a link outside the package')
    readme.unlink()
    readme.symlink_to(outside)
    failed = run('--source', 'working-tree', '--out', Path(tmp) / 'symlink', ok=False)
    assert 'Refusing plugin symlink or submodule' in failed.stderr
    assert not list((Path(tmp) / 'symlink').glob('*.zip'))

    readme.unlink()
    readme.write_text('working draft\n')
    outside_dir = Path(tmp) / 'outside-directory'
    shutil.move(package / '.claude-plugin', outside_dir)
    (package / '.claude-plugin').symlink_to(outside_dir, target_is_directory=True)
    failed = run('--source', 'working-tree', '--out', Path(tmp) / 'directory-link', ok=False)
    assert 'Refusing plugin symlink or submodule' in failed.stderr
    assert not list((Path(tmp) / 'directory-link').glob('*.zip'))

print('Plugin build: index/draft version consistency, tracked files, reproducibility and symlink bounds: PASSED')

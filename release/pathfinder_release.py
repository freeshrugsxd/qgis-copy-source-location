from pathlib import Path
from shutil import copy2, copystat, make_archive, rmtree


parents = Path(__file__).parents
root = parents[2]
src = parents[1]
dest = parents[0]
release_root = dest / 'release'
release = release_root / 'pathfinder'

flist = [
    '__init__.py',
    'pathfinder.py',
    'resources.py',
    'metadata.txt',
    'i18n/pathfinder.pro',
    'i18n/pathfinder_en.ts',
    'i18n/pathfinder_pl.qm',
    'i18n/pathfinder_ru.qm',
    'i18n/pathfinder_es.ts',
    'i18n/pathfinder_de.ts',
    'i18n/pathfinder_fr.ts',
    'i18n/pathfinder_ru.ts',
    'i18n/pathfinder_de.qm',
    'i18n/pathfinder_pl.ts',
    'i18n/pathfinder_es.qm',
    'i18n/pathfinder_en.qm',
    'i18n/pathfinder_fr.qm',
    'icons/open_in_explorer.svg',
    'icons/copy.svg',
    'icons/resources.qrc',
    'lib/__init__.py',
    'lib/core.py',
    'lib/layertreecontextmenumanager.py',
    'lib/eventfilter.py',
    'lib/utils.py',
    'lib/settingsdialog.py',
    'ui/settingsdiag.ui'
]

dirs = ['i18n', 'icons', 'lib', 'ui']

release.mkdir(parents=True)

for d in dirs:
    release.joinpath(d).mkdir(parents=True)

for f in flist:
    copy2(src / f, release / f)

for d in dirs:
    copystat(src / d, release / d)

make_archive('pathfinder', 'zip', root_dir=release_root)
rmtree(release_root)

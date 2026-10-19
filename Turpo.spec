# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

datas = [
    ('Game.py', '.'),
    ('images', 'images'),
    ('sounds', 'sounds'),
    ('music', 'music'),
    ('logo Game.png', '.'),
    ('team_logo.png', '.'),
    ('game_icon.ico', '.'),
]
binaries = []
hiddenimports = [
    'pygame',
    'pgzrun',
    'questions',
    'answers',
    'start_page',
    'play_page',
    'pause_page',
    'game_over_page',
    'store',
    'makers_page',
    'questions_page',
]

pgzero_datas, pgzero_binaries, pgzero_hiddenimports = collect_all('pgzero')
datas += pgzero_datas
binaries += pgzero_binaries
hiddenimports += pgzero_hiddenimports

a = Analysis(
    ['Exe code.py'],
    pathex=['.'],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Turpo',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['game_icon.ico'],
)

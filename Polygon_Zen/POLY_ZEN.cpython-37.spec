# -*- mode: python -*-

block_cipher = None


a = Analysis(['POLY_ZEN.cpython-37.pyc'],
             pathex=['C:\\Users\\FeedFall8\\source\\repos\\Polygon Zen\\Polygon Zen'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='POLY_ZEN.cpython-37',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )

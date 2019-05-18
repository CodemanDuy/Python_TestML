# -*- mode: python -*-

block_cipher = None

added_files = [
    ('config.json', '.'),  # Loads the '' file from your root folder and outputs it with the same name on the same place.
]

a = Analysis(['__main__.py'],
             pathex=['Z:\\WorkDev\\GitHub Repository\\TestOnSolve'],
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
          name='ExchangeRatesPrediction',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )

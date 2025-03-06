# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Icon file path - create an icon for your app
icon_file = 'app_icon.ico'  # Replace with your actual icon file

a = Analysis(
    ['audio transcription code.py'],
    pathex=[],
    binaries=[],
    datas=[
        # Add any additional data files your app needs
        # Example: ('path/to/data/file', 'destination/in/bundle')
    ],
    hiddenimports=[
        'torch',
        'torch.backends.cudnn',
        'transformers',
        'transformers.models.whisper',
        'transformers.models.whisper.processing_whisper',
        'transformers.models.whisper.tokenization_whisper',
        'transformers.models.whisper.configuration_whisper',
        'transformers.models.whisper.modeling_whisper',
        'librosa',
        'librosa.core',
        'librosa.util',
        'librosa.feature',
        'librosa.filters',
        'python-docx',
        'docx',
        'customtkinter',
        'PIL',
        'PIL._tkinter_finder',
        'json',
        'threading',
        'platform',
        'numpy'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='AudioTransPro',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,  # Changed to False to hide console window for end users
    runtime_tmpdir=None,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_file if os.path.exists(icon_file) else None
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='AudioTransPro'
)
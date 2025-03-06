# AudioTrans Pro

An AI-powered audio transcription application that uses state-of-the-art models to convert speech to text with high accuracy.

## Features

- Multi-language support (French, English, German, Spanish, Italian)
- Multiple output formats (TXT, DOCX)
- Adjustable transcription quality settings
- Timestamp support
- Dark/Light theme

## System Requirements

- Windows 10 or 11 (64-bit)
- 8GB RAM minimum (16GB recommended)
- 2GB free disk space
- Internet connection (for model download)

## Installation

### Option 1: Use the Installer

1. Download the latest installer from the [Releases](https://github.com/tofunori/Audio-transcription/releases) page
2. Run the installer and follow the instructions
3. The application will download the necessary AI models on first run

### Option 2: Development Setup

1. Clone this repository
   ```
   git clone https://github.com/tofunori/Audio-transcription.git
   cd Audio-transcription
   ```

2. Create a virtual environment and install dependencies
   ```
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the application
   ```
   python "audio transcription code.py"
   ```

## Building the Installer

1. Install PyInstaller and Inno Setup
   ```
   pip install pyinstaller
   ```
   Download Inno Setup from https://jrsoftware.org/isdl.php

2. Create an icon for your app and save it as `app_icon.ico`

3. Build the application with PyInstaller
   ```
   pyinstaller AudioTrans.spec
   ```

4. Compile the installer with Inno Setup
   - Open AudioTransInstaller.iss in Inno Setup
   - Click Build > Compile

5. Find the installer in the `installer` directory

## Troubleshooting

### Accelerate Dependency Error

If you see an error like:
```
Using `low_cpu_mem_usage=True` or a `device_map` requires Accelerate: `pip install 'accelerate>=0.26.0'`
```

Install the accelerate package:
```
pip install accelerate>=0.26.0
```

Then rebuild the application.

### Other Issues

- Make sure you have all required dependencies installed
- Check that the model has been downloaded correctly (in the `models` directory)
- For large files, try using the "Rapide" (Fast) option to reduce memory usage

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details.

## Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper) - Speech recognition model
- [Transformers](https://github.com/huggingface/transformers) - AI model library
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Modern UI toolkit

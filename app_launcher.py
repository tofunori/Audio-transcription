import os
import sys
import subprocess

# Check if running as a frozen application
is_frozen = getattr(sys, 'frozen', False)

# Get application directory
if is_frozen:
    app_dir = os.path.dirname(sys.executable)
else:
    app_dir = os.path.dirname(os.path.abspath(__file__))

def main():
    """Main launcher function"""
    # Check if model downloader exists
    downloader_path = os.path.join(app_dir, "model_downloader.py")
    main_app_path = os.path.join(app_dir, "audio transcription code.py")
    main_exe_path = os.path.join(app_dir, "AudioTransPro.exe")
    
    # Check if the model directory exists
    model_dir = os.path.join(app_dir, "models")
    models_exist = os.path.exists(model_dir) and os.path.isdir(model_dir)
    
    if not models_exist:
        # Models don't exist, run the downloader first
        print("First run: Starting model downloader...")
        if is_frozen:
            # In frozen app, run the bundled downloader executable
            os.system(f'start "" "{os.path.join(app_dir, "model_downloader.exe")}"')
        else:
            # In development, run the Python script
            subprocess.Popen([sys.executable, downloader_path])
    else:
        # Models exist, run the main application
        print("Starting main application...")
        if is_frozen:
            os.system(f'start "" "{main_exe_path}"')
        else:
            subprocess.Popen([sys.executable, main_app_path])

if __name__ == "__main__":
    main()

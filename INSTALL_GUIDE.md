# AudioTrans Pro - Complete Installation Guide

This guide will walk you through the process of creating a professional installer for your AudioTrans Pro application.

## Prerequisites

1. **Python 3.9+ installed**
2. **PyInstaller installed**: `pip install pyinstaller`
3. **Inno Setup 6+ installed**: [Download here](https://jrsoftware.org/isdl.php)
4. **Icon file**: Create an `.ico` file for your application (recommended)

## Step 1: Add the Model Downloader Script

1. Save the `model_downloader.py` script provided in this package to your project directory
2. Test it works by running: `python model_downloader.py`

## Step 2: Modify Your Main Application

Add the following code at the beginning of your `audio transcription code.py` file, right after your imports:

```python
# Check if model is available and download if needed
def check_and_download_model():
    """Check if the model is downloaded, and if not, run the downloader"""
    try:
        model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
        if not os.path.exists(model_dir) or len(os.listdir(model_dir)) == 0:
            # Model is not downloaded
            if os.path.exists("model_downloader.py"):
                import subprocess
                subprocess.Popen(["python", "model_downloader.py"])
                sys.exit(0)
    except Exception as e:
        print(f"Error checking model: {e}")

# Run model check before starting the app (if not running as frozen app)
if __name__ == "__main__" and not getattr(sys, 'frozen', False):
    check_and_download_model()
```

## Step 3: Create an Application Icon

1. Create a 256x256 pixel PNG image of your application logo
2. Convert it to ICO format using an online converter or tools like:
   - [ConvertICO](https://convertio.co/png-ico/)
   - [ICO Converter](https://www.icoconverter.com/)
3. Save the file as `app_icon.ico` in your project directory

## Step 4: Build with PyInstaller

1. Copy the optimized `AudioTrans.spec` file to your project directory
2. Make sure your icon file is named correctly in the spec file
3. Open a command prompt in your project directory and run:

```
pyinstaller AudioTrans.spec
```

4. Check the `dist/AudioTransPro` folder to ensure all files were created correctly

## Step 5: Create the Installer with Inno Setup

1. Copy the optimized `AudioTransInstaller.iss` file to your project directory
2. Make sure your icon file is referenced correctly in the ISS file
3. Open Inno Setup and load the `AudioTransInstaller.iss` file
4. Click "Build" or press F9 to compile the installer
5. The installer will be created in the `installer` folder

## Step 6: Testing Your Installer

1. Test the installer on a clean virtual machine to ensure it works correctly
2. Verify all features:
   - Installation process
   - Model downloading
   - Application startup
   - Uninstallation

## Advanced Customization Options

### Adding a Splash Screen

For a more professional look, add a splash screen to your app startup:

1. Create a splash screen image (PNG or JPG)
2. Add the following code to your application:

```python
def show_splash():
    splash = ctk.CTkToplevel()
    splash.title("")
    splash.overrideredirect(True)
    
    # Load image
    splash_img = ctk.CTkImage(
        light_image=Image.open("splash.png"),
        dark_image=Image.open("splash.png"),
        size=(400, 300)
    )
    
    # Display image
    img_label = ctk.CTkLabel(splash, image=splash_img, text="")
    img_label.pack()
    
    # Center on screen
    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    x = (screen_width - 400) // 2
    y = (screen_height - 300) // 2
    splash.geometry(f"400x300+{x}+{y}")
    
    # Close after 3 seconds
    splash.after(3000, splash.destroy)
    splash.update()
    
# Call this function before initializing your main app
```

### Adding an Auto-Updater

For future updates, consider adding an auto-updater:

1. Create a version.json file on your GitHub that contains:
```json
{
  "version": "1.0.0",
  "download_url": "https://github.com/tofunori/Audio-transcription/releases/download/v1.0.0/AudioTransPro_Setup.exe",
  "release_notes": "Initial release"
}
```

2. Add update checking code to your app:
```python
def check_for_updates():
    try:
        import requests
        response = requests.get("https://raw.githubusercontent.com/tofunori/Audio-transcription/main/version.json")
        data = response.json()
        current_version = "1.0.0"  # Your app's current version
        
        if data["version"] > current_version:
            # Prompt user to update
            if messagebox.askyesno("Update Available", 
                f"Version {data['version']} is available. Would you like to download it now?\n\nRelease Notes:\n{data['release_notes']}"):
                import webbrowser
                webbrowser.open(data["download_url"])
    except Exception as e:
        print(f"Error checking for updates: {e}")
```

## Troubleshooting

### Common Issues and Solutions

1. **Missing dependencies in the PyInstaller bundle**:
   - Use `--debug=imports` flag with PyInstaller to detect missing modules
   - Add them to the `hiddenimports` list in your spec file

2. **Antivirus false positives**:
   - Sign your installer with a code signing certificate if possible
   - Submit your application to antivirus vendors for whitelisting
   - Add detailed instructions for users (as you've done with VERIFICATION.txt)

3. **Model download failures**:
   - Implement better error handling in the model downloader
   - Provide alternative download methods or direct users to manual download

4. **Issues with paths in the packaged application**:
   - Always use relative paths with `os.path.join()`
   - Check for the `frozen` attribute in `sys` to detect if running as executable

## Final Steps and Distribution

1. **Test on different Windows versions** (Windows 10/11)
2. **Create a GitHub release** with your installer
3. **Add detailed installation instructions** to your README
4. **Consider submitting to software directories** for wider exposure

Good luck with your AudioTrans Pro application distribution!
import os
import sys
import time
import threading
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
import torch

# Define models path
def get_models_dir():
    """Get the directory where models should be stored"""
    if hasattr(sys, '_MEIPASS'):  # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_dir, "models")

class ModelDownloaderApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # App configuration
        self.title("AudioTrans Pro - Model Downloader")
        self.geometry("600x400")
        self.resizable(True, True)
        
        # Set appearance mode and color theme
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        
        # Create main frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title label
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="AudioTrans Pro - First Run Setup",
            font=("Segoe UI", 20, "bold")
        )
        self.title_label.pack(pady=(0, 20))
        
        # Info text
        self.info_text = ctk.CTkTextbox(
            self.main_frame,
            height=100,
            font=("Segoe UI", 12)
        )
        self.info_text.pack(fill="x", padx=10, pady=10)
        self.info_text.insert("1.0", (
            "Welcome to AudioTrans Pro!\n\n"
            "Before you can use the application, we need to download the Whisper AI model. "
            "This is a one-time process and may take several minutes depending on your internet connection. "
            "The model requires approximately 2GB of disk space.\n\n"
            "Click 'Download Model' to begin."
        ))
        self.info_text.configure(state="disabled")
        
        # Progress frame
        self.progress_frame = ctk.CTkFrame(self.main_frame)
        self.progress_frame.pack(fill="x", padx=10, pady=10)
        
        # Progress bar
        self.progress_var = ctk.DoubleVar(value=0.0)
        self.progress_bar = ctk.CTkProgressBar(
            self.progress_frame,
            variable=self.progress_var,
            width=500,
            height=20
        )
        self.progress_bar.pack(pady=10)
        
        # Status label
        self.status_var = ctk.StringVar(value="Ready to download")
        self.status_label = ctk.CTkLabel(
            self.progress_frame,
            textvariable=self.status_var,
            font=("Segoe UI", 12)
        )
        self.status_label.pack(pady=5)
        
        # Button frame
        self.button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.button_frame.pack(fill="x", padx=10, pady=(20, 10))
        
        # Download button
        self.download_btn = ctk.CTkButton(
            self.button_frame,
            text="Download Model",
            command=self.download_model,
            width=150,
            height=40,
            font=("Segoe UI", 14, "bold")
        )
        self.download_btn.pack(side="left", padx=(20, 10))
        
        # Skip button
        self.skip_btn = ctk.CTkButton(
            self.button_frame,
            text="Skip Download",
            command=self.skip_download,
            width=150,
            height=40,
            fg_color="#777777",
            font=("Segoe UI", 14)
        )
        self.skip_btn.pack(side="left", padx=10)
        
        # Exit button
        self.exit_btn = ctk.CTkButton(
            self.button_frame,
            text="Exit",
            command=self.exit_app,
            width=100,
            height=40,
            fg_color="#d63031",
            font=("Segoe UI", 14)
        )
        self.exit_btn.pack(side="right", padx=(10, 20))
        
        # Check if model already exists
        self.models_dir = get_models_dir()
        if self.check_model_exists():
            self.status_var.set("Model already downloaded!")
            self.progress_var.set(1.0)
            self.download_btn.configure(state="disabled")
        
    def check_model_exists(self):
        """Check if the model files already exist"""
        # Basic check - this can be improved to verify all required files
        model_id = "openai/whisper-large-v3"
        cache_dir = self.models_dir
        
        # Check if the model directory exists and has files
        if os.path.exists(cache_dir):
            model_files = [f for f in os.listdir(cache_dir) if "whisper" in f.lower()]
            if len(model_files) > 0:
                return True
        return False
    
    def download_model(self):
        """Download the Whisper model"""
        self.download_btn.configure(state="disabled")
        self.skip_btn.configure(state="disabled")
        
        # Create a thread for downloading
        threading.Thread(target=self._download_model_thread, daemon=True).start()
    
    def _download_model_thread(self):
        """Background thread for model download"""
        try:
            # Create models directory if it doesn't exist
            os.makedirs(self.models_dir, exist_ok=True)
            
            # Update status
            self.status_var.set("Downloading model...")
            self.progress_var.set(0.2)
            
            # Set cache directory for transformers
            model_id = "openai/whisper-large-v3"
            cache_dir = self.models_dir
            
            # Load model (this will download it)
            self.status_var.set("Downloading processor...")
            processor = AutoProcessor.from_pretrained(model_id, cache_dir=cache_dir)
            self.progress_var.set(0.4)
            
            self.status_var.set("Downloading model (this may take a while)...")
            device = "cuda:0" if torch.cuda.is_available() else "cpu"
            torch_dtype = torch.float16 if device == "cuda:0" else torch.float32
            
            model = AutoModelForSpeechSeq2Seq.from_pretrained(
                model_id,
                torch_dtype=torch_dtype,
                low_cpu_mem_usage=True,
                use_safetensors=True,
                cache_dir=cache_dir
            )
            
            self.progress_var.set(0.9)
            self.status_var.set("Finishing up...")
            
            # Save model configuration to verify it's properly downloaded
            config_file = os.path.join(cache_dir, "whisper_config.txt")
            with open(config_file, "w") as f:
                f.write(f"Model: {model_id}\n")
                f.write(f"Downloaded: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Device: {device}\n")
            
            # Complete
            self.progress_var.set(1.0)
            self.status_var.set("Model downloaded successfully!")
            
            # Display success message
            self.show_success_dialog()
            
        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")
            self.progress_var.set(0)
            self.download_btn.configure(state="normal")
            self.skip_btn.configure(state="normal")
    
    def show_success_dialog(self):
        """Show success dialog and offer to start the application"""
        success_window = ctk.CTkToplevel(self)
        success_window.title("Download Complete")
        success_window.geometry("400x200")
        success_window.resizable(False, False)
        success_window.transient(self)
        success_window.grab_set()
        
        # Center the window
        success_window.update_idletasks()
        x = self.winfo_x() + (self.winfo_width() - success_window.winfo_width()) // 2
        y = self.winfo_y() + (self.winfo_height() - success_window.winfo_height()) // 2
        success_window.geometry(f"+{x}+{y}")
        
        # Success message
        message_label = ctk.CTkLabel(
            success_window,
            text="Model downloaded successfully!",
            font=("Segoe UI", 16, "bold")
        )
        message_label.pack(pady=(20, 10))
        
        info_label = ctk.CTkLabel(
            success_window,
            text="You can now start using AudioTrans Pro.",
            font=("Segoe UI", 12)
        )
        info_label.pack(pady=10)
        
        # Button frame
        button_frame = ctk.CTkFrame(success_window, fg_color="transparent")
        button_frame.pack(fill="x", padx=10, pady=20)
        
        # Launch app button
        launch_btn = ctk.CTkButton(
            button_frame,
            text="Launch Application",
            command=self.launch_app,
            width=150,
            height=35,
            font=("Segoe UI", 12, "bold")
        )
        launch_btn.pack(side="left", padx=20)
        
        # Exit button
        exit_btn = ctk.CTkButton(
            button_frame,
            text="Exit",
            command=self.exit_app,
            width=100,
            height=35,
            fg_color="#777777",
            font=("Segoe UI", 12)
        )
        exit_btn.pack(side="right", padx=20)
    
    def skip_download(self):
        """Skip the model download (may cause issues if model is required)"""
        skip_window = ctk.CTkToplevel(self)
        skip_window.title("Skip Download")
        skip_window.geometry("400x200")
        skip_window.resizable(False, False)
        skip_window.transient(self)
        skip_window.grab_set()
        
        # Center the window
        skip_window.update_idletasks()
        x = self.winfo_x() + (self.winfo_width() - skip_window.winfo_width()) // 2
        y = self.winfo_y() + (self.winfo_height() - skip_window.winfo_height()) // 2
        skip_window.geometry(f"+{x}+{y}")
        
        # Warning message
        message_label = ctk.CTkLabel(
            skip_window,
            text="Warning: Skip Model Download?",
            font=("Segoe UI", 16, "bold")
        )
        message_label.pack(pady=(20, 10))
        
        info_label = ctk.CTkLabel(
            skip_window,
            text="The application requires the Whisper model to function.\nSkipping this step may cause errors.",
            font=("Segoe UI", 12)
        )
        info_label.pack(pady=10)
        
        # Button frame
        button_frame = ctk.CTkFrame(skip_window, fg_color="transparent")
        button_frame.pack(fill="x", padx=10, pady=20)
        
        # Skip anyway button
        skip_btn = ctk.CTkButton(
            button_frame,
            text="Skip Anyway",
            command=lambda: [skip_window.destroy(), self.launch_app()],
            width=150,
            height=35,
            fg_color="#d63031",
            font=("Segoe UI", 12, "bold")
        )
        skip_btn.pack(side="left", padx=20)
        
        # Cancel button
        cancel_btn = ctk.CTkButton(
            button_frame,
            text="Cancel",
            command=lambda: skip_window.destroy(),
            width=100,
            height=35,
            fg_color="#777777",
            font=("Segoe UI", 12)
        )
        cancel_btn.pack(side="right", padx=20)
    
    def launch_app(self):
        """Launch the main application"""
        # Get the path to the main executable
        if hasattr(sys, '_MEIPASS'):
            main_app = os.path.join(os.path.dirname(sys.executable), "AudioTransPro.exe")
        else:
            main_app = "audio transcription code.py"
        
        # Launch the application if it exists
        if os.path.exists(main_app):
            self.destroy()
            os.system(f'start "" "{main_app}"')
        else:
            self.status_var.set(f"Error: Cannot find main application")
    
    def exit_app(self):
        """Exit the application"""
        self.destroy()
        sys.exit(0)

if __name__ == "__main__":
    app = ModelDownloaderApp()
    app.mainloop()
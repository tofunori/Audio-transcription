#define MyAppName "AudioTrans Pro"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Audio Transcription"
#define MyAppURL "https://github.com/tofunori/Audio-transcription"
#define MyAppExeName "AudioTransPro.exe"

[Setup]
; Unique identifier for the app
AppId={{F4A36F2E-9F6A-4E48-B5C1-89F99BBBF021}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
OutputDir=installer
OutputBaseFilename=AudioTransPro_Setup
Compression=lzma2/ultra64
SolidCompression=yes
WizardStyle=modern
DisableWelcomePage=no
DisableDirPage=no
DisableProgramGroupPage=no
; Request admin rights to avoid permission issues
PrivilegesRequired=admin
; Set minimum Windows version (Windows 10 recommended for ML apps)
MinVersion=10.0
SetupIconFile=app_icon.ico
UninstallDisplayIcon={app}\{#MyAppExeName}
; Create a log file during installation
SetupLogging=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "french"; MessagesFile: "compiler:Languages\French.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 6.1; Check: not IsAdminInstallMode

[Files]
; Main application files
Source: "dist\AudioTransPro\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\AudioTransPro\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; Documentation
Source: "README.txt"; DestDir: "{app}"; Flags: ignoreversion isreadme
Source: "LICENSE.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "VERIFICATION.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "antivirus_instructions.txt"; DestDir: "{app}"; Flags: ignoreversion
; Default preferences file - will only be copied if it doesn't exist already
Source: "default_preferences.json"; DestDir: "{app}"; DestName: "audiotrans_preferences.json"; Flags: onlyifdoesntexist

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\Documentation\README"; Filename: "{app}\README.txt"
Name: "{group}\Documentation\License"; Filename: "{app}\LICENSE.txt"
Name: "{group}\Documentation\Verification"; Filename: "{app}\VERIFICATION.txt"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon

[Run]
; Show important files after installation
Filename: "{app}\README.txt"; Description: "View README file"; Flags: postinstall shellexec skipifsilent
Filename: "{app}\VERIFICATION.txt"; Description: "View Security Verification Information"; Flags: postinstall shellexec skipifsilent
Filename: "{app}\antivirus_instructions.txt"; Description: "View Antivirus Instructions"; Flags: postinstall shellexec skipifsilent
; Launch app after installation
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: files; Name: "{app}\audiotrans_preferences.json"
Type: filesandordirs; Name: "{app}\__pycache__"

[Code]
// Show a message about first run and model download
procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    MsgBox('When you first run AudioTrans Pro, it will download the necessary AI models. This may take some time depending on your internet connection. Please be patient during the first launch.', mbInformation, MB_OK);
  end;
end;
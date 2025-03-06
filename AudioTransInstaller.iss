#define MyAppName "AudioTrans Pro"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Audio Transcription"
#define MyAppExeName "AudioTrans.exe"

[Setup]
; Unique identifier for the app
AppId={{F4A36F2E-9F6A-4E48-B5C1-89F99BBBF021}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
; Add publisher URL and other details for legitimacy
AppPublisherURL=https://github.com
AppSupportURL=https://github.com
AppUpdatesURL=https://github.com
; Sign the installer if you have a certificate
;SignTool=standard
; Compression settings that don't trigger AV
Compression=lzma2/normal
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
OutputDir=installer
OutputBaseFilename=AudioTrans_Setup
Compression=lzma2/ultra64
SolidCompression=yes
WizardStyle=modern
DisableWelcomePage=no
DisableDirPage=no
DisableProgramGroupPage=no
PrivilegesRequired=lowest

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "french"; MessagesFile: "compiler:Languages\French.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
; Add file information and verification
Source: "dist\AudioTransPro\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs signonce nocompression
; Add documentation files
Source: "README.txt"; DestDir: "{app}"; Flags: ignoreversion isreadme
Source: "antivirus_instructions.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "LICENSE.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "VERIFICATION.txt"; DestDir: "{app}"; Flags: ignoreversion

[Messages]
WelcomeLabel2=This will install [name] on your computer.%n%nThis software is licensed under the MIT License. Security verification information is available in VERIFICATION.txt.%n%nThe installer and program files are not encrypted or obfuscated, and can be verified using the provided checksums.%n%nBy continuing, you agree to the terms of the license agreement.

[InstallDelete]
; Clean up old files to prevent conflicts
Type: filesandordirs; Name: "{app}\*"

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
; Show important files after installation
Filename: "{app}\LICENSE.txt"; Description: "View License Agreement"; Flags: postinstall shellexec skipifsilent
Filename: "{app}\README.txt"; Description: "View README file"; Flags: postinstall shellexec skipifsilent
Filename: "{app}\antivirus_instructions.txt"; Description: "View Antivirus Instructions"; Flags: postinstall shellexec skipifsilent
Filename: "{app}\VERIFICATION.txt"; Description: "View Security Verification Information"; Flags: postinstall shellexec skipifsilent
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[Code]
function InitializeSetup(): Boolean;
begin
  Result := True;
end;

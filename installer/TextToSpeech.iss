#define MyAppName "Filipov Voice Translator"
; MyAppVersion is overwritten from the root VERSION file by scripts\build_installer.ps1
#define MyAppVersion "1.4.0"
#define MyAppPublisher "Evtinko Auktions Ltd (Filipov)"
#define MyAppExeName "TextToSpeech.exe"

[Setup]
AppId={{A8E7F2C3-4B1D-4E9A-9C2F-1234567890AB}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={userpf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputDir=..\installer_output
; Version in filename so older builds stay alongside (e.g. *_1.2.0.exe vs *_1.4.0.exe).
OutputBaseFilename=FilipovVoiceTranslatorSetup_{#MyAppVersion}
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
ArchitecturesInstallIn64BitMode=x64compatible
; Optional: configure SignTool in Inno if you prefer compiler-side signing.
; SignTool=signtool
; SignedUninstaller=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "..\dist\TextToSpeech\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

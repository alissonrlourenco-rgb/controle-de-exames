; Modelo para Inno Setup 6. Recuperar o AppId anterior antes de distribuir.
#define MyAppName "Controle de Exames"
#define MyAppVersion "0.1.0"
#define MyAppExeName "ControleExames.exe"

[Setup]
AppId={{B43C98D1-41E9-41C4-9F4B-AC63ABCF1672}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
DefaultDirName={autopf}\ControleExames
DefaultGroupName={#MyAppName}
OutputDir=..\..\installer-output
OutputBaseFilename=ControleExames_Setup_{#MyAppVersion}
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
PrivilegesRequired=lowest

[Files]
Source: "..\..\dist\ControleExames\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Abrir {#MyAppName}"; Flags: nowait postinstall skipifsilent

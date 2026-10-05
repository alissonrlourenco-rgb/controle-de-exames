from pathlib import Path

root = Path(SPECPATH).resolve().parents[1]
resources = root / "src" / "controle_exames" / "resources"
icon = resources / "icons" / "ControleExames.ico"

a = Analysis(
    [str(root / "scripts" / "run_app.py")],
    pathex=[str(root / "src")],
    binaries=[],
    datas=[(str(resources), "controle_exames/resources")],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz, a.scripts, [],
    exclude_binaries=True,
    name="ControleExames",
    debug=False,
    strip=False,
    upx=False,
    console=False,
    icon=str(icon) if icon.exists() else None,
)
coll = COLLECT(exe, a.binaries, a.datas, strip=False, upx=False, name="ControleExames")

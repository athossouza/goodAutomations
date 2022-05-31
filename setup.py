import sys
from cx_Freeze import setup, Executable


# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os", "openpyxl", "json", "time", "getpass"], "excludes": ["tkinter"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None

setup(
    name="Zendesk Change License",
    version="0.1",
    description="Zendesk Change Licenses (By Athos)",
    options={"build_exe": build_exe_options},
    executables=[Executable("Zendesk\ZDTrocaLicenca10.py", base=base, icon="icon.ico")],
)
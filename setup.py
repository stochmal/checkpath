'''create Windows executable'''
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

setup(
    name = "checkpath",
    version = "1.3",
    description = "Check PATH environment variable",
    options = {"build_exe": build_exe_options},
    executables = [Executable("checkpath.py", base=None)]
)

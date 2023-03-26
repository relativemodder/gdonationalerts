from pymem import Pymem
import pymem.process
from pathlib import Path

def inject_dll(dll_path, process_name):
    dll_path_bytes = bytes(str(Path(dll_path).absolute()), "UTF-8")
    process = Pymem(process_name=process_name)
    pymem.process.inject_dll(process.process_handle, dll_path_bytes)

def inject_notification_mod():
    inject_dll("./notifications-in-gd.dll", "GeometryDash.exe")
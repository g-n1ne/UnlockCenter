from platform import uname
from importlib import import_module

current_arch = uname().machine
supported_archs = ["aarch64", "x86_64"]

if current_arch in supported_archs:
    try:
        filename = f"unlockcenter_{current_arch}"
        module = import_module(filename)
        module.main()
    except Exception as e:
        print(e)
        print("Failed to start!")
else:
    print("Platform not supported!")


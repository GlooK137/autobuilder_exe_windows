from os import system, remove
from shutil import rmtree, copy2


async def build(path):


    script = [
        [ system, f"cd {path}"],
        [ system, r"python -m venv venv"],
        [ system, r"venv\Scripts\pip install -r requirements.txt"],
        [ system, r"venv\Scripts\pyinstaller -F main.py"],
        [ rmtree, "venv"],
        [ copy2,  r"dist\main.exe main.exe"],
        [ rmtree, "dist" ],
        [ rmtree, "build" ],
        [ remove, "main.spec" ]
    ]

    for command in script:
        
        try:

            command[0](command[1])

        except Exception as e:

            print(f"{command[0]}({command[1]})",e)
            return 0

    file = open(path+"/main.exe","rb")
    return file
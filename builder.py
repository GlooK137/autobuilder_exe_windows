from os import system, remove
from shutil import rmtree, copy2


async def build(path):


    script = [
        [ system, rf"python -m venv {path}\venv"],
        [ system, rf"{path}\venv\Scripts\pip install -r {path}\requirements.txt"],
        [ system, rf"{path}\venv\Scripts\pyinstaller -F {path}\main.py"],
        [ rmtree, rf"{path}\venv"],
        [ copy2,  rf"{path}\dist\main.exe {path}\main.exe"],
        [ rmtree, rf"{path}\dist" ],
        [ rmtree, rf"{path}\build" ],
        [ remove, rf"{path}\main.spec" ]
    ]

    for command in script:
        
        try:

            command[0](command[1])

        except Exception as e:

            print(f"{command[0]}({command[1]})",e)
            return [0,f"{command[0]}({command[1]})"]

    return [1]
from os import system
async def build(path):
    system("copy build_exe.bat "+path+"\\build_exe.bat")
    system(f"cd {path} && build_exe.bat")
    file = open(path+"/main.exe","rb")
    return file
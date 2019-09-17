from cx_Freeze import setup, Executable

setup(
    name='Bot Binary',
    version='1.0.0',
    description='.py to .exe',
    executables=[Executable('main.py')]

)

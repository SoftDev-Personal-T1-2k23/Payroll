::Build & Rename exe
if %IS_DEBUG% == 1 goto :build_debug

::--additional-hooks-dir=setup.py

:build_release
set "EXE_TITLE=Program-Release.exe"
pyinstaller program.py --onefile --windowed
goto :rename_exe

:build_debug
set "EXE_TITLE=Program-Debug.exe"
pyinstaller program.py --onefile

:rename_exe
cd /d "%~dp0\dist"
rename "Program.exe" %EXE_TITLE%

echo.
echo Build Successful
echo.
echo exe_title: %EXE_TITLE%
echo.

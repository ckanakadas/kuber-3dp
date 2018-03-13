@echo OFF
@setlocal ENABLEDELAYEDEXPANSION
echo %~1
if "%~1" == "" (
    echo Please provide xml file path as a first parameter.
    exit /B 1
)

if not exist "%~1" (
    echo Xml file with given path does not exist.
    exit /B 2
)

if exist "%~1.tmp" del /F /Q "%~1.tmp"

for /F "delims=" %%G in (%~1) do (
    set LINE=%%G
    if not "!LINE!" == "!LINE:RUNNING=!" (
        set LINE=!LINE:-=HANDG!
    )
                if not "!LINE!" == "!LINE:TIMETOCOMPLETE=!" (
        set LINE=!LINE:-=4:30!
    )
    >> "%~1.tmp" echo !LINE!
)

del /F /Q "%~1"
copy "%~1.tmp" "%~1"

@endlocal

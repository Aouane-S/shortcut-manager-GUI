@echo off
cd %~dp0
cd /d "%~dp0"
copy %~dp0icones\SystemProperties.ico "%SystemRoot%\System32\"
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"="
    echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"

:: Add SystemProperties to context Menus
::-------------------------------------
SetACL.exe -silent -on "HKCR\Directory\shell\SystemProperties" -ot reg -actn setowner -ownr "n:Administrators"
SetACL.exe -silent -on "HKCR\Directory\shell\SystemProperties" -ot reg -actn ace -ace "n:Administrators;p:full"
SetACL.exe -silent -on "HKCR\Directory\shell\SystemProperties\command" -ot reg -actn setowner -ownr "n:Administrators"
SetACL.exe -silent -on "HKCR\Directory\shell\SystemProperties\command" -ot reg -actn ace -ace "n:Administrators;p:full"

reg add "HKCR\Directory\shell\SystemProperties" /v "" /t REG_SZ /d "SystemProperties" /f 1>NUL 2>NUL
reg add "HKCR\Directory\shell\SystemProperties" /v "Icon" /t REG_SZ /d "%SystemRoot%\System32\SystemProperties.ico" /f 1>NUL 2>NUL
reg add "HKCR\Directory\shell\SystemProperties" /v "NeverDefault" /t REG_SZ /d "" /f 1>NUL 2>NUL
reg add "HKCR\Directory\shell\SystemProperties" /v "NoWorkingDirectory" /t REG_SZ /d "" /f 1>NUL 2>NUL
reg add "HKCR\Directory\shell\SystemProperties" /v "Position" /t REG_SZ /d "Bottom" /f 1>NUL 2>NUL
reg add "HKCR\Directory\shell\SystemProperties\command" /v "" /t REG_SZ /d "control.exe sysdm.cpl" /f 1>NUL 2>NUL
SetACL.exe -silent -on "HKCR\Directory\Background\shell\SystemProperties" -ot reg -actn setowner -ownr "n:Administrators"
SetACL.exe -silent -on "HKCR\Directory\Background\shell\SystemProperties" -ot reg -actn ace -ace "n:Administrators;p:full"
SetACL.exe -silent -on "HKCR\Directory\Background\shell\SystemProperties\command" -ot reg -actn setowner -ownr "n:Administrators"
SetACL.exe -silent -on "HKCR\Directory\Background\shell\SystemProperties\command" -ot reg -actn ace -ace "n:Administrators;p:full"
reg add "HKCR\Directory\Background\shell\SystemProperties" /v "" /t REG_SZ /d "SystemProperties" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\SystemProperties" /v "Icon" /t REG_SZ /d "%SystemRoot%\System32\SystemProperties.ico" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\SystemProperties" /v "NeverDefault" /t REG_SZ /d "" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\SystemProperties" /v "NoWorkingDirectory" /t REG_SZ /d "" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\SystemProperties" /v "Position" /t REG_SZ /d "Bottom" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\SystemProperties\command" /v "" /t REG_SZ /d "control.exe sysdm.cpl" /f 1>NUL 2>NUL

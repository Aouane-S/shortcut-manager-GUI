@echo off
cd %~dp0
cd /d "%~dp0"
echo %CD%
copy %~dp0icones\network.ico "%SystemRoot%\System32\"
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
::--------------------------------------
SetACL.exe -silent -on "HKCR\Directory\shell\Network" -ot reg -actn setowner -ownr "n:Administrators"
SetACL.exe -silent -on "HKCR\Directory\shell\Network" -ot reg -actn ace -ace "n:Administrators;p:full"
SetACL.exe -silent -on "HKCR\Directory\shell\Network\command" -ot reg -actn setowner -ownr "n:Administrators"
SetACL.exe -silent -on "HKCR\Directory\shell\Network\command" -ot reg -actn ace -ace "n:Administrators;p:full"

::Background
reg add "HKCR\Directory\Background\shell\Network" /v "" /t REG_SZ /d "Network" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\Network" /v "Icon" /t REG_SZ /d "%SystemRoot%\System32\network.ico" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\Network" /v "NeverDefault" /t REG_SZ /d "" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\Network" /v "NoWorkingDirectory" /t REG_SZ /d "" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\Network" /v "Position" /t REG_SZ /d "Top" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\Network\command" /v "" /t REG_SZ /d "C:\Windows\System32\control.exe ncpa.cpl" /f 1>NUL 2>NUL



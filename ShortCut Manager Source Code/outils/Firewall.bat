@echo off
cd %~dp0
cd /d "%~dp0"
echo %CD%
copy %~dp0icones\firewall.ico "%SystemRoot%\System32\"
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
copy %~dp0icones\firewall.ico "%SystemRoot%\System32\"
SetACL.exe -silent -on "HKCR\Directory\shell\Firewall" -ot reg -actn setowner -ownr "n:Administrators"
SetACL.exe -silent -on "HKCR\Directory\shell\Firewall" -ot reg -actn ace -ace "n:Administrators;p:full"
SetACL.exe -silent -on "HKCR\Directory\shell\Firewall\command" -ot reg -actn setowner -ownr "n:Administrators"
SetACL.exe -silent -on "HKCR\Directory\shell\Firewall\command" -ot reg -actn ace -ace "n:Administrators;p:full"

::Background
reg add "HKCR\Directory\Background\shell\Firewall" /v "" /t REG_SZ /d "Firewall" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\Firewall" /v "Icon" /t REG_SZ /d "%SystemRoot%\System32\firewall.ico" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\Firewall" /v "NeverDefault" /t REG_SZ /d "" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\Firewall" /v "NoWorkingDirectory" /t REG_SZ /d "" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\Firewall" /v "Position" /t REG_SZ /d "Top" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\Firewall\command" /v "" /t REG_SZ /d "%SystemRoot%\System32\control.exe firewall.cpl" /f 1>NUL 2>NUL




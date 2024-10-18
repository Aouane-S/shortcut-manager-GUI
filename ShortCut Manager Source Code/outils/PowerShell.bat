
@echo off
:: use PowerShell in context Menus
::-------------------------------------
cd %~dp0
cd /d "%~dp0"
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

:: Add "Open PowerShell" to context menus
SetACL.exe -silent -on "HKCR\Directory\shell\PowershellMenu" -ot reg -actn setowner -ownr "n:Administrators"
SetACL.exe -silent -on "HKCR\Directory\shell\PowershellMenu" -ot reg -actn ace -ace "n:Administrators;p:full"
SetACL.exe -silent -on "HKCR\Directory\shell\PowershellMenu\command" -ot reg -actn setowner -ownr "n:Administrators"
SetACL.exe -silent -on "HKCR\Directory\shell\PowershellMenu\command" -ot reg -actn ace -ace "n:Administrators;p:full"

reg add "HKCR\Directory\shell\runasps" /v "" /t REG_SZ /d "PowerShell" /f 1>NUL 2>NUL
reg add "HKCR\Directory\shell\runasps" /v "Icon" /t REG_SZ /d "powershell.exe" /f 1>NUL 2>NUL
reg add "HKCR\Directory\shell\runasps" /v "NeverDefault" /t REG_SZ /d "" /f 1>NUL 2>NUL
reg add "HKCR\Directory\shell\runasps" /v "NoWorkingDirectory" /t REG_SZ /d "" /f 1>NUL 2>NUL
reg add "HKCR\Directory\shell\runasps" /v "Position" /t REG_SZ /d "Top" /f 1>NUL 2>NUL
reg add "HKCR\Directory\shell\runasps\command" /v "" /t REG_SZ /d "powershell.exe -noexit -command Set-Location -literalPath '%%V'" /f 1>NUL 2>NUL
SetACL.exe -silent -on "HKCR\Directory\Background\shell\PowershellMenu" -ot reg -actn setowner -ownr "n:Administrators"
SetACL.exe -silent -on "HKCR\Directory\Background\shell\PowershellMenu" -ot reg -actn ace -ace "n:Administrators;p:full"
SetACL.exe -silent -on "HKCR\Directory\Background\shell\PowershellMenu\command" -ot reg -actn setowner -ownr "n:Administrators"
SetACL.exe -silent -on "HKCR\Directory\Background\shell\PowershellMenu\command" -ot reg -actn ace -ace "n:Administrators;p:full"
reg delete "HKCR\Directory\Background\shell\PowershellMenu" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\runasps" /v "" /t REG_SZ /d "PowerShell" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\runasps" /v "Icon" /t REG_SZ /d "powershell.exe" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\runasps" /v "NeverDefault" /t REG_SZ /d "" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\runasps" /v "NoWorkingDirectory" /t REG_SZ /d "" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\runasps" /v "Position" /t REG_SZ /d "Top" /f 1>NUL 2>NUL
reg add "HKCR\Directory\Background\shell\runasps\command" /v "" /t REG_SZ /d "powershell.exe -noexit -command Set-Location -literalPath '%%V'" /f 1>NUL 2>NUL
reg add "HKCR\LibraryFolder\Shell\runasps" /v "" /t REG_SZ /d "PowerShell" /f 1>NUL 2>NUL
reg add "HKCR\LibraryFolder\Shell\runasps" /v "Icon" /t REG_SZ /d "powershell.exe" /f 1>NUL 2>NUL
reg add "HKCR\LibraryFolder\Shell\runasps" /v "NeverDefault" /t REG_SZ /d "" /f 1>NUL 2>NUL
reg add "HKCR\LibraryFolder\Shell\runasps" /v "NoWorkingDirectory" /t REG_SZ /d "" /f 1>NUL 2>NUL
reg add "HKCR\LibraryFolder\Shell\runasps" /v "Position" /t REG_SZ /d "Top" /f 1>NUL 2>NUL
reg add "HKCR\LibraryFolder\Shell\runasps\command" /v "" /t REG_SZ /d "powershell.exe -noexit -command Set-Location -literalPath '%%V'" /f 1>NUL 2>NUL
reg add "HKCR\LibraryFolder\background\shell\runasps" /v "" /t REG_SZ /d "PowerShell" /f 1>NUL 2>NUL
reg add "HKCR\LibraryFolder\background\shell\runasps" /v "Icon" /t REG_SZ /d "powershell.exe" /f 1>NUL 2>NUL
reg add "HKCR\LibraryFolder\background\shell\runasps" /v "NeverDefault" /t REG_SZ /d "" /f 1>NUL 2>NUL
reg add "HKCR\LibraryFolder\background\shell\runasps" /v "NoWorkingDirectory" /t REG_SZ /d "" /f 1>NUL 2>NUL
reg add "HKCR\LibraryFolder\background\shell\runasps" /v "Position" /t REG_SZ /d "Top" /f 1>NUL 2>NUL
reg add "HKCR\LibraryFolder\background\shell\runasps\command" /v "" /t REG_SZ /d "powershell.exe -noexit -command Set-Location -literalPath '%%V'" /f 1>NUL 2>NUL

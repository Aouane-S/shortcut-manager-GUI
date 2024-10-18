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
:: Delete "PowerShell" to context menus
reg delete "HKCR\Directory\shell\PowershellMenu" /f 1>NUL 2>NUL
reg delete "HKCR\Directory\Background\shell\PowershellMenu" /f 1>NUL 2>NUL

reg delete "HKCR\Directory\Background\shell\Powershell" /f 1>NUL 2>NUL
reg delete "HKCR\Directory\Background\shell\runasps" /f 1>NUL 2>NUL
reg delete "HKCR\Directory\shell\runasps" /f 1>NUL 2>NUL
reg delete "HKCR\LibraryFolder\Shell\runasps" /f 1>NUL 2>NUL
reg delete "HKCR\LibraryFolder\background\shell\runasps" /f 1>NUL 2>NUL


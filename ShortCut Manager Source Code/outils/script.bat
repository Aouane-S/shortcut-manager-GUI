@echo off
:: use PowerShell in context Menus
::-------------------------------------
cd %~dp0
cd /d "%~dp0"
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

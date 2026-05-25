@echo off
title Kaffe Launcher

cls

echo Kaffe Launcher
echo.

set /p compiler=Kaffe Compiler file: 
set /p ksscompiler=KSS Compiler file: 
set /p inputfile=Input file: 
set /p outputfile=Output file: 

:compile

echo.
echo Compiling...

%compiler% %inputfile% %outputfile% %ksscompiler%

echo.
echo Done!
echo.

set /p retry=Recompile? (y/n): 
cls
if /i "%retry%"=="y" goto compile

exit
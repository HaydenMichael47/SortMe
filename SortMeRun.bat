@echo off
where python > tmpFile
set /p pyPath= < tmpFile
del tmpFile
echo %pyPath%

set myPath=%cd%
echo %myPath%

%pyPath% %myPath%\SortMe.py
PAUSE
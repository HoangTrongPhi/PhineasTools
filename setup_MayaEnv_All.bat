@echo off
title Setup Maya Environment - PhineasTools
REM === 1. Set MAYA_APP_DIR ===
echo --------------------------------------------
echo Setting environment variable MAYA_APP_DIR...
echo --------------------------------------------

setx MAYA_APP_DIR "%USERPROFILE%\Documents\maya"
echo MAYA_APP_DIR set to: %USERPROFILE%\Documents\maya
echo (This takes effect in new sessions only.)
echo.

echo Environment setup complete!
echo --------------------------------------------

pause

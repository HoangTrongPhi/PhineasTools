
robocopy %SOURCE%\PhineasTools\Technical_Release\_icons  %DESTINATION% %USERPROFILE%\Documents\maya\2024\prefs\icons  /mir
robocopy %SOURCE%\PhineasTools\Technical_Release\_icons  %DESTINATION% %USERPROFILE%\Documents\maya\2025\prefs\icons  /mir
robocopy %SOURCE%\PhineasTools\Technical_Release\_icons  %DESTINATION% %USERPROFILE%\Documents\maya\2026\prefs\icons  /mir


robocopy %SOURCE%\PhineasTools\Technical_Release\Software\Maya\Data\Shelves  %DESTINATION% %USERPROFILE%\Documents\maya\2024\prefs\shelves  /mir
robocopy %SOURCE%\PhineasTools\Technical_Release\Software\Maya\Data\Shelves  %DESTINATION% %USERPROFILE%\Documents\maya\2025\prefs\shelves  /mir
robocopy %SOURCE%\PhineasTools\Technical_Release\Software\Maya\Data\Shelves  %DESTINATION% %USERPROFILE%\Documents\maya\2026\prefs\shelves  /mir



robocopy %SOURCE%\PhineasTools\Technical_Release\Software\Maya\Data\support  %DESTINATION% %USERPROFILE%\Documents\maya\scripts  /e


robocopy %SOURCE%\PhineasTools\Technical_Release\Software\Maya\Data\site-packages  %DESTINATION% %USERPROFILE%\Documents\maya\scripts\site-packages  /e


robocopy %SOURCE%\PhineasTools\Technical_Release\Software\Maya\Data\site-packages  %DESTINATION% %USERPROFILE%\Documents\maya\2024\scripts\site-packages  /mir
robocopy %SOURCE%\PhineasTools\Technical_Release\Software\Maya\Data\site-packages  %DESTINATION% %USERPROFILE%\Documents\maya\2025\scripts\site-packages  /mir
robocopy %SOURCE%\PhineasTools\Technical_Release\Software\Maya\Data\site-packages  %DESTINATION% %USERPROFILE%\Documents\maya\2026\scripts\site-packages  /mir

pause
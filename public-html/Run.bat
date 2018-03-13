@echo off
setlocal enabledelayedexpansion

FOR /F "usebackq delims=" %%G IN ("ip.txt") DO (
  Set "line=%%G" & echo !line:"=!)>>"textfile2.txt"
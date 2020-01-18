@ECHO off
REM ***************************************************************************
REM Copyright (c) to Pandiarajan
REM Licensed under the MIT License
REM Replace correct value in the script before execting
REM Values to be replaced are with in << >>

set CUR_YYYY=%date:~10,4%
set CUR_MM=%date:~4,2%
set CUR_DD=%date:~7,2%
set CUR_HH=%time:~0,2%
if %CUR_HH% lss 10 (set CUR_HH=0%time:~1,1%)

set CUR_NN=%time:~3,2%
set CUR_SS=%time:~6,2%
set CUR_MS=%time:~9,2%
set FILENAME=%CUR_DD%-%CUR_MM%-%CUR_YYYY%-%CUR_HH%_%CUR_NN%_%CUR_SS%

ECHO 'Running python FTPSyncUtil.py "<<Server IP Address>>" "<<Local Folder Path>>" "<<FTP username>>" "<<FTP password>>"' 

python FTPSyncUtil.py "<<Server IP Address>>" "<<Local Folder Path>>" "<<FTP username>>" "<<FTP password>>" > %FILENAME%.log

ECHO "Successfully completed. Please refer log %FILENAME%.log for more details"

REM ***************************************************************************
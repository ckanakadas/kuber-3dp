echo %1
copy NUL D:\file_monitor\%1.txt
echo %1 > D:\file_monitor\%1.txt
echo %date% %time% >> D:\file_monitor\%1.txt
set root=D:\file_monitor
cd  /d %root%
git pull https://ckanakadas@bitbucket.org/ckanakadas/file_monitor.git master
git status
git add --all .
git commit -m "Test commit"
git push https://ckanakadas@bitbucket.org/ckanakadas/file_monitor.git master

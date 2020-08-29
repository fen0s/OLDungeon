rd /s/q saves
mkdir saves
echo *>saves\.gitignore
echo !.gitignore>>saves\.gitignore
del transcript.txt
FOR /d /r . %%d IN ("__pycache__") DO @IF EXIST "%%d" rd /s /q "%%d"
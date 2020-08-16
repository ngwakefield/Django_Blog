Small notes

Virtual environment is djangoblog
Run conda activate djangoblog

To run the server, form the top level dir
python manage.py runserver

About setting environment variables
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#setting-environment-variables

But note that using powershell requires different activation scripts
Instead, you must create env_vars.ps1 (instead of .bat)
And powershell syntax is as follows:

For activation (example):
$Env:EMAIL_USER="myemail@email.com"
For deactivation:
Remove-Item Env:\EMAIL_USER

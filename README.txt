If you do not have the module which helps creating virtual env, run:
pip install virtualenv

In order to create a new virtual environment, run:
python -m venv {name_for_virtual_env}
Ex:
python -m venv env8

Next step is to activate the virtual environment. Run script inside:
.{name_for_virtual_env}\Scripts\Activate.ps1
Ex:
.\env8\Scripts\Activate.ps1

If you can't execute the script to activate a virtual env, try to run first:
Set-ExecutionPolicy Unrestricted -Scope Process

pip is a manager which helps installing python libraries, we can even specify a version. Example of commands:
pip install requests
pip install numpy==1.20.0
pip list
pip install --upgrade requests
pip unistall requests
pip freeze > file_with_current_versions_of_libraries.txt
pip install -r file_with_current_versions_of_libraries.txt
How to deactivate a virtual env? Type:
deactivate
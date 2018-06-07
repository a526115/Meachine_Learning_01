# 1. How to create requirements.txt
# Option 1 - Recommendation:
pip install pipreqs
pipreqs --force workspace_path

# Option 2:
pip freeze > workspace_path

# Create Anaconda virtual env and run below command in activate env
pip install -r requirements.txt

# 2.Anaconda + Python3.6

# basic command for Anaconda
conda list
conda env list
conda update conda

# crate virtual env
conda create -n your_env_name python=X.X（2.7, 3.6)

# enable virtual env
Linux:  source activate your_env_name
Windows: activate your_env_name

# delete virtual env
conda remove -n your_env_name --all

# delete specific package
conda remove --name your_env_name  package_name

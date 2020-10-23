### Please review the [Interfaces Team Contributor Guide](https://predikto.atlassian.net/l/c/ZXHujzjy) before commiting to this repo.

## Getting started
- First you'll need to get the source of the project.

```bash
git clone git@bitbucket.org:predikto/{{cookiecutter.repo_name}}.git
cd {{cookiecutter.repo_name}}
```

- If you do not have `conda` on your machine, you'll need to install it here. The conda docs will point you to the proper installation script. You should download the 64bit, python 3.7, full Anaconda install for your OS.

(Conda Install)[https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html]

- Create a conda environment in which we can install the dependencies

```bash
conda env create -f environment.yml
conda activate {{cookiecutter.repo_name}}
```

- If you in the future need to delete your conda env to recreate it, you can delete the enviroment and everything in it with:

```bash
conda deactivate  ## Get out of the {{cookiecutter.repo_name}} env if you need to.
conda env remove --name {{cookiecutter.repo_name}}
```

- Make sure to copy `pip.conf` to `$HOME/.pip/pip.conf` so that you can
  pull down internal dependencies from the VPN.

- Now we can install our dependencies:

```bash
pip install -r requirements/local.txt
```

- Make sure your local Docker is running.

- Now the following command will setup the database and run the server:

```bash
source local_env.sh
docker-compose up -d

flask db upgrade
flask run

```

### Test Setup

- To run tests:

```bash
source test_env.sh
source ./tests/setup_tests.sh
pytest
```

- To tear down test data: `docker-compose down`

### pre-commit

Pre-commit can run various scripts just prior to a `git commit`. Here, it is used to quickly check formatting and that linting passes.

After pip installing this repo with `pip install -r requirements/local.txt`, install the pre-commit hooks with

```bash
pre-commit install
```

This sets pre-commit to run. The first run will be a little slower since pre-commit will need to fetch it's dependencies. If your code doesn't pass the checks, pre-commit may automatically make some formatting changes to your code that you will have to amend/accept, and then stage, before moving on to staging these changes and committing. flake8 warnings and errors will need to be fixed manually. You can also run these checks and fixes manually with

```bash
pre-commit run -a
```

Our pre-commit setup is using black, flake8 and safety. Black is an auto-formatter that will auto-format your code. Flake8 is a linter that will complain when you violate it's rules. Safety is a tool that looks for known security vulnerabilities in installed dependencies. Amoung these you will need to fight with Flake8 the most. You will become familiar with it's rules as you run afoul of them. You can check out their docs for how to add exceptions for violations:

[Flake8](https://flake8.pycqa.org/en/latest/)

You might also want to check out the docs for black and safety:

[black](https://black.readthedocs.io/en/stable/)
[safety](https://github.com/pyupio/safety)

If you install pre-commit globally, you may on occasion need to commit to repos that are not configured with it. You can tell git to ignore the lack of a pre-commit with:

```bash
export PRE_COMMIT_ALLOW_NO_CONFIG=1
```

You will on occasion need to ignore pre-commit checks and rapidly push changes without fighting pre-commit. On such occasions you can use:

```bash
git commit --no-verify
```
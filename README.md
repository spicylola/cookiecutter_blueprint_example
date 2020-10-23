## Getting started with creating the cookiecutter

### Directory Structure
- /{{cookiecutter.repo_name} - main level directory where entire contents of your service will go
    - hooks.py
        - post_gen_project.py - contains the hook for generating the models based off the cookiecutter.model_files argument
          must be in format: {"values":["m3.py"]}
    - requirements- directory that contains the dependencies for the service
        - base.txt - minimal level of dependencies needed for application to run
        - dev.txt - minimal level of dependencies needed for application to run in development environment
        - local.txt - minimal level of dependencies needed for application to run locally
    - /tests
       - __init__.py
       - conftest.py - since tests are based on pytest, file that contains fixtures for tests
       - data_mutations.py - file that holds the mutation queries needed for the tests to run
       - data_queries.py - file that holds the queries for the tests to run
       - test_graphql.py - file that holds the tests, usually data is imported from data_queries.py and data_mutations.py

    - /{{cookiecutter.repo_name}
        - __init__.py contains the flask application with db instance, migration, instance and all the necessary components
          to run the application
        - models - flask models will go here, based on graphene sqlalchemy,but not limited to
          -__init__.py
        - schema - graphql schema objects belong in this repo
          - __init___.py
          - base.py - Custom field overrides the base graphene-sqlalchemy-filter field to add pagination support, and
             turn off native graphql relay arguments such as before, first, last, after
          - schema.py - query and mutation objects  for the graphql are contained in the is file
          - {{cookiecutter.repo_name}.py - not mandatory - contains the filter field objects, mutation resolver objects
    - .flake8 - linting for the service
    - .gitignore - files that will be ignored by git
    - CHANGELOG.md - file that contains changelog information
    - docker-compose.yml - for local development only contains postgres images for a test instance and local instance
    - Dockerfile - dockerfile that contains steps necessary needed to turn application into a docker container
    - local_env.sh - bash script that exports variables for local development
    - pip.conf - conf file that add predikto pypy server
    - Readme.md - Readme for how to run application, tests
    - run_migrations.sh - bash script for running database migrations for deployment
    - settings.py - contains the configurations for the flask application
    - start_app_http.py - because you do not want to run Flask run beyond local development, wsgi server for running application
       is contained in this file
    - test_env.sh - bash script for export test environment variables


Make sure you have  cookiecutter installed, preferably in a virtual environment

```bash
pip install cookiecutter
```

First you'll need to get the source of the project.

```bash
git clone git@bitbucket.org:predikto/api_blueprint.git
```
Once you have cloned the repo, you will go to the directory, you want to generate your cookiecutter service in.api_blueprint

```bash
cookiecutter api_blueprint
```

This will prompt you to something that looks like this and you will fill it out when prompted and hit enter to the next line:

```bash
full_name [Damilola Shonaike]: (some_example_name_here)
email [damilola.shonaike@utc.com]: (some_example_email_here)
repo_name [api_blueprint]: (some_example_repo_name_here)
version [2020.9.1]: (version_number_here)
db_username [predikto]: (some_db_username_here)
db_password [qwerty]: (some_db_password_here)
test_db_port [54321]: (some_db_test_port_here)
db_port [5432]: (some_db_test_port_here)
model_files [default]: {"values":["model1.py", "model2.py", "model3.py"]}
```

### Migrations Directory
 Because Migrations is native to alembic, You will use Flask Migrate once you have successfully created your models:
(You only need to do this the first time)
```bash
source local_env.sh
docker-compose up -d
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### Tests

This is the Readme portion You will keep for running the repo locally, everything above this line you can erase
once you have successfully created the microservice

We use Graphene and snapshots for testing, examples can be found here: https://docs.graphene-python.org/en/latest/testing/
The snapshots directory will appear the first time you run tests

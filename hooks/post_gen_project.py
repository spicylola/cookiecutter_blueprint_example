from collections import OrderedDict

model_files = {{ cookiecutter.model_files }}
for item in model_files["values"]:
  new_file = open("{{cookiecutter.repo_name}}/models/"+item, "x")
  new_file.close()


# Heating-X-code-generator

Use Jinja to create YAML files for all the template sensors and helpers required for a complete home installation of Heating X zones.

To get started:
1. Make sure you have Python 3 installed.
2. Create a virtual environment with `python3 -m venv .venv`.
3. Activate your virtual environment with `source .venv/bin/activate`.
4. Install the required dependencies with `python3 -m pip install requirements.txt`.
5. Make your own `config.yaml` with `cp config.yaml.sample config.yaml`.
6. Edit the contents of the resulting `config.yaml` to match your own installation (zones and thermostats).
7. Create the required files with `python generate.py` which will output the files into
the `output/` directory.

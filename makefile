PYTHON:=python3.7
VENV:=venv

all: venv

setup-env: 
	sudo add-apt-repository ppa:deadsnakes/ppa
	sudo apt install $(PYTHON)
	sudo apt install python3-pip
	sudo apt install $(PYTHON)-distutils
	sudo apt-get install python3-dev
	$(PYTHON) -m pip install virtualenv

./$(VENV)/bin/activate: requirements.txt
	$(PYTHON) -m virtualenv $(VENV) --python=$(PYTHON)
	./$(VENV)/bin/pip install --upgrade pip
	./$(VENV)/bin/pip install -r requirements.txt

venv: ./$(VENV)/bin/activate

run:
	./$(VENV)/bin/$(PYTHON) run.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: setup-env clean venv run
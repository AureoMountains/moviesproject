
PYTHON := python
PIP := $(PYTHON) -m pip
SCRIPT := movies.py
VENV := .venv

.PHONY: run check install clean help

help:
	@echo "Available commands:"
	@echo "  make install  Install dependencies"
	@echo "  make run      Run the movie analysis"
	@echo "  make check    Check Python syntax"
	@echo "  make clean    Remove generated Python files"

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) $(SCRIPT)

check:
	$(PYTHON) -m py_compile $(SCRIPT)

clean:
	$(PYTHON) -c "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.pyc')]"
	$(PYTHON) -c "import shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__') if p.is_dir()]" 

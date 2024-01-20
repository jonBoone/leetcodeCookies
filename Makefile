help:
	@echo "Makefile Help:"
	@echo ""
	@echo "build			build leetcodeCookies package"
	@echo "clean			clean builds"
	@echo "install			install leetcodeCookies in current python env"
	@echo "run			run leetcodeCookies installed in current python env"
	@echo "upload			upload leetcodeCookies package to PyPi"

build:
	@python -m build

clean:
	@rm -rf dist/
	@rm -rf build/
	@rm -rf *egg-info/

install:
	pip install -e .

run:
	@~/leetcodeCookes


upload:
	@twine upload --verbose dist/*

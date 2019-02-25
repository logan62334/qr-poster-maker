release:
	python setup.py bdist_wheel --universal
	python setup.py bdist_wheel upload


all: app

app: clean pythonToApp/setup.py
	python3 pythonToApp/setup.py py2app

clean:
	rm -rf build dist
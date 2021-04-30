MACOS_DIST=dist/macOS

all:

app: clean pythonToApp/setup.py
	python3 pythonToApp/setup.py py2app -d ${MACOS_DIST} -b ${MACOS_DIST}
	mv ${MACOS_DIST}/python* ${MACOS_DIST}/build

clean:
	rm -rf dist
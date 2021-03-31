all: main

main: Main.py
	python3 Main.py

test : game/test/Village.py
	python3 -m game.test.MainTest
venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

test: venv
	. venv/bin/activate; python -m pytest -sv

.PHONY: ttygame
ttygame:
	. venv/bin/activate; python -m main $(NPLAYERS) --nocurses

.PHONY: game
game:
	. venv/bin/activate; python -m main $(NPLAYERS)


clean:
	rm -rf venv
	find -iname "*.pyc" -delete

run: main.py
	python3 main.py
	convert pic.ppm pic.png
	display pic.png

clean:
	rm *.pyc
	rm *~
	rm *.png
	rm *.ppm

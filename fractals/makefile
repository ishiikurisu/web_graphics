.PHONY: run
run:
	rm -rf julia
	mkdir julia
	python3 main.py
	magick convert mandelbrot.ppm mandelbrot.png
	magick convert julia.ppm julia.png
	magick convert burning_ship.ppm burning_ship.png
	magick convert -delay 4 -loop 0 julia/*.ppm julia.gif
	rm *.ppm
	rm -rf julia


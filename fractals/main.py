ITER_LIMIT = 100
HEIGHT = 500
WIDTH = 500


def pixels_to_complex_plane(x, y):
    r = (x / WIDTH) * 4.0 - 2.0 
    i = (y / HEIGHT) * 4.0 - 2.0

    return r + (1j * i)


def escape_time(f, z0):
    z = z0
    i = 0

    while abs(z) < 2.0 and i < ITER_LIMIT:
        z = f(z0, z)
        i += 1

    return abs(z) > 2.0 


def escape_time_fractal(f):
    outlet = []

    for y in range(HEIGHT):
        line = []
        for x in range(WIDTH):
            z = pixels_to_complex_plane(x, y)
            line.append(escape_time(f, z))
        outlet.append(line)
        
    return outlet


def mandelbrot(z0, z):
    return z ** 2 + z0


def new_julia(c0):
    return lambda z0, z: (z ** 2) + c0


def burning_ship(z0, z):
    return (abs(z.real) + 1j * abs(z.imag)) ** 2 + z0


def matrix_to_image(inlet, output_file):
    with open(output_file, "w") as fp:
        fp.write(f"P1 {WIDTH} {HEIGHT} ")
        for line in inlet:
            for escaped in line:
                fp.write(f"{0 if escaped else 1} ")


def main():
    print("--- # mandelbrot set")
    mandelbrot_set = escape_time_fractal(mandelbrot)
    matrix_to_image(mandelbrot_set, "mandelbrot.ppm")

    print("--- # julia fractal")
    julia = new_julia(-0.8406 + 0.1242j)
    # julia = new_julia(0 + 0j)
    julia_set = escape_time_fractal(julia)
    matrix_to_image(julia_set, "julia.ppm")

    # TODO julia fractal animation
    print("--- # burning ship fractal")
    burning_ship_set = escape_time_fractal(burning_ship)
    matrix_to_image(burning_ship_set, "burning_ship.ppm")


if __name__ == "__main__":
    main()


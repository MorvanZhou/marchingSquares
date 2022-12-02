import masq


# masq.random(20, 30, bound=0.5)
# masq.simplex_noise(20, 30, bound=0.5, wavelength=5, show_point=False)
# masq.loop_random(20, 30, bound=0.5)
masq.loop_simplex_noise(20, 30, bound=0.5, wavelength=5, increment=0.01, show_point=False)

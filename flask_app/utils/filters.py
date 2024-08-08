def percentage_format(number):
    return f"{number/100:.0%}"


def lighten_colour(hex):
    FACTOR = 1.1
    h = hex.lstrip("#")
    rgb = tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))
    rgb_light = tuple(i * FACTOR for i in rgb)
    return f"rgb{rgb_light}"

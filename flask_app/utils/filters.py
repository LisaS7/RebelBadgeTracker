def percentage_format(number):
    return f"{number/100:.0%}"


def lighten_colour(hex):
    h = hex.lstrip("#")
    rgb = tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))
    rgb_light = tuple(i * 1.5 for i in rgb)
    return f"rgb{rgb_light}"

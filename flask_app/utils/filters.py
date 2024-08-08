def percentage_format(number):
    return f"{number/100:.0%}"


def adjust_colour(hex, factor):
    h = hex.lstrip("#")
    rgb = tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))
    rgb_light = tuple(i * factor for i in rgb)
    return f"rgb{rgb_light}"

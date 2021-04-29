RESISTOR_COLORS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

def value(colors):
    first = colors[0]
    second = colors[1]
    return RESISTOR_COLORS[first] * 10 + RESISTOR_COLORS[second]
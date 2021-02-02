import math


def dist_from_point_to_line(x, y, x1, y1, x2, y2):
    """dist_from_point_to_line.
    ある点と他の二点を通る直線との距離を求める

    Args:
        x:
        y:
        x1:
        y1:
        x2:
        y2:
    """

    a = y2 - y1
    b = -(x2 - x1)
    c = -x1 * (y2 - y1) + y1 * (x2 - x1)
    den = math.sqrt(a**2 + b**2)
    num = abs(a * x + b * y + c)
    dist = num / den
    return dist


def dist_from_point_to_line2(x, y, x1, y1, x2, y2):
    """dist_from_point_to_line.
    ある点と他の二点を通る直線との距離を求める

    Args:
        x:
        y:
        x1:
        y1:
        x2:
        y2:
    """
    p = complex(x, y)
    p1 = complex(x1, y1)
    p2 = complex(x2, y2)
    p -= p1
    p2 -= p1
    rot_p = p2 / abs(p2)
    p /= rot_p
    return p.imag

def distance_points(x, y, checkpoint):
    wx, wy = checkpoint

    return math.sqrt((x - wx) ** 2 + (y - wy) ** 2)

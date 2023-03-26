def clamp(val, minimum, maximum):
    if val < minimum: return minimum
    elif val > maximum: return maximum
    return val
def calculate_slope_and_intercept(x1, y1, x2, y2):
    if x1 == x2:  # Avoid division by zero error
        return None, x1
    else:
        slope = (y2 - y1) / (x2 - x1)
        intercept = y1 - slope * x1
        return slope, intercept


def line_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    m1, c1 = calculate_slope_and_intercept(x1, y1, x2, y2)
    m2, c2 = calculate_slope_and_intercept(x3, y3, x4, y4)
    
    if m1 is None: # if the first line is vertical
        x = c1
        y = m2 * x + c2 if m2 is not None else None
    elif m2 is None: # if the second line is vertical
        x = c2
        y = m1 * x + c1 if m1 is not None else None
    elif m1 == m2: # parallel lines
        x = y = None
    else: # lines intersect
        x = (c2 - c1) / (m1 - m2)
        y = m1 * x + c1

    # Check if the intersection point lies within both line segments
    if x is not None and y is not None:
        is_within_x_range_1 = min(x1, x2) <= x <= max(x1, x2)
        is_within_y_range_1 = min(y1, y2) <= y <= max(y1, y2)
        is_within_x_range_2 = min(x3, x4) <= x <= max(x3, x4)
        is_within_y_range_2 = min(y3, y4) <= y <= max(y3, y4)
        if is_within_x_range_1 and is_within_y_range_1 and is_within_x_range_2 and is_within_y_range_2:
            return True

    return False

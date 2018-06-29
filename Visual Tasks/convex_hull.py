from nodebox.graphics import Point

def convex_hull(mypoints):

    x_vals = []
    for p in mypoints:
        x_vals.append(p.x)

    y_vals = []
    for p in mypoints:
       y_vals.append(p.y)

    new_points = zip(x_vals,y_vals)

    points = sorted(set(new_points))
 
    if len(points) <= 1:
        return mypoints

    # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
    # Returns a positive value, if OAB makes a counter-clockwise turn,
    # negative for clockwise turn, and zero if the points are collinear.
    def cross(o, a, b):
       return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull 
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list. 
    hull = lower[:-1] + upper[:-1]

    hullPoints = []
    for h in hull:
        hullPoints.append(Point(h[0],h[1]))

    return hullPoints



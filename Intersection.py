from __future__ import division
from collections import namedtuple

Point = namedtuple('Point', 'x y')
Segment = namedtuple('Segment', 'ep1 ep2')


def find_slope(segment):
    """
    Return the slope of the line segment, if it is defined. If it is
    undefined, return None.
    """
    p1, p2 = segment.ep1, segment.ep2
    if p2.x - p1.x == 0.0:
        return None
    else:
        return (p2.y-p1.y) / (p2.x-p1.x)


def find_y_intercept(slope, point):
    """
    Return the y-intercept of an infinite line with slope equal to slope that
    passes through point. If slope does not exist, return None.
    """
    if slope is None:
        return None
    else:
        return point.y - slope*point.x


def order_segment(segment):
    """
    Order endpoints in segment primarily by x position, and secondarily by y
    position.
    """
    ep1, ep2 = segment.ep1, segment.ep2
    if (ep1.x > ep2.x or ep1.x == ep2.x and ep1.y > ep2.y):
        segment.ep1, segment.ep2 = segment.ep2, segment.ep1


def order_segments(segments):
    """
    Order segments by each segment's first endpoint. Similar to order_segment,
    order primarily by first endpoint's x position, and secondarily by first
    endpoint's y position.
    """
    seg1, seg2 = segments
    if (seg1.ep1.x > seg2.ep1.x or seg1.ep1.x == seg2.ep1.x
            and seg1.ep1.y > seg2.ep1.y):
        segments[0], segments[1] = segments[1], segments[0]


def on(point, segment):
    """
    Return True if point lies on segment. Otherwise, return False.
    """
    return (within(segment.ep1.x, point.x, segment.ep2.x) and
            within(segment.ep1.y, point.y, segment.ep2.y))


def within(p, q, r):
    """
    Return True if q is between p and r. Otherwise, return False.
    """
    return p <= q <= r or r <= q <= p


def find_intersection(segment1, segment2):
    """
    Return an intersection point of segment1 and segment2, if one exists. If
    multiple points of intersection exist, randomly return one of those
    intersection points. If no intersection exists, return None.
    """
    [s1, s2] = [find_slope(l) for l in [segment1, segment2]]
    [k1, k2] = [find_y_intercept(s, l[0])
                for s, l in [(s1, segment1), (s2, segment2)]]

    if s1 == s2:
        if k1 != k2:
            return None
        #  at this point, the two line segments are known to lie on the same
        #  infinite line (i.e. all of the endpoints are collinear)
        segments = [segment1, segment2]
        for segment in segments:
            order_segment(segment)
        order_segments(segments)
        intersection = segments[1].ep1
    else:
        #  assume segment 1 has slope and segment 2 doesn't
        s, x, k = s1, segment2.ep1.x, k1
        #  assumption wrong, segment 1 doesn't have a slope, but segment 2 does
        if s1 is None:
            s, x, k = s2, segment1.ep1.x, k2
        #  assumption wrong, segments 1 and 2 both have slopes
        elif s2 is not None:
            x = (k2-k1) / (s1-s2)
        y = s*x + k
        intersection = Point(x, y)

    if on(intersection, segment1) and on(intersection, segment2):
        return intersection
    else:
        return None
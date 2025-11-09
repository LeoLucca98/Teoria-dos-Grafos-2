
from typing import Tuple, List
Point = Tuple[float, float]
def _orient(a: Point, b: Point, c: Point) -> float:
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
def _on_segment(a: Point, b: Point, p: Point) -> bool:
    return (min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and
            min(a[1], b[1]) <= p[1] <= max(a[1], b[1]))
def segments_intersect(p1: Point, q1: Point, p2: Point, q2: Point, proper: bool=True) -> bool:
    o1 = _orient(p1, q1, p2); o2 = _orient(p1, q1, q2); o3 = _orient(p2, q2, p1); o4 = _orient(p2, q2, q1)
    if o1*o2 < 0 and o3*o4 < 0: return True
    if not proper:
        if o1 == 0 and _on_segment(p1, q1, p2): return True
        if o2 == 0 and _on_segment(p1, q1, q2): return True
        if o3 == 0 and _on_segment(p2, q2, p1): return True
        if o4 == 0 and _on_segment(p2, q2, q1): return True
    return False
def polygon_edges(poly: List[Point]):
    n = len(poly)
    for i in range(n):
        yield poly[i], poly[(i+1)%n]

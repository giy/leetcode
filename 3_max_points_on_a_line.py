#!/usr/bin/env
# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
	max_p = 0
	if (len(points)) <= 2:
            return len(points)
	for i in range(len(points)):
	    p = {}
	    dup = 1
	    for j in range(len(points)):
		# Check that i != j, don't double count
                if points[i].x == points[j].x and points[i].y == points[j].y and i != j:
		    dup += 1 # Count both points
                elif i != j:
	            # The slope of a vertical line is infinity
                    if points[i].x == points[j].x:
		        p['inf'] = p.get('inf', 0) + 1
		    # The slope of a horizontal line is zero
		    elif points[i].y == points[j].y:
		        p['zero'] = p.get('zero', 0) + 1
                    else:
		        slope = 1.0*(points[j].y - points[i].y)/(points[j].x - points[i].x)
                        p[slope] = p.get(slope, 0) + 1
            vals = p.values()
	    if vals:
                max_p = max(max_p, max(vals) + dup)
	    else:
		max_p = max(max_p, dup)
	return max_p

so = Solution()
points1 = [Point(0,0), Point(0,0)]
points2 = [Point(0,0)]
points3 = [Point(0,0), Point(1,1), Point(1,-1)]
points4 = [Point(84,250),Point(0,0),Point(1,0),Point(0,-70),Point(0,-70),Point(1,-1),Point(21,10),Point(42,90),Point(-42,-230)]
print so.maxPoints(points1)
print so.maxPoints(points2)
print so.maxPoints(points3)
print so.maxPoints(points4)

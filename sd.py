def slope(point1,point2): 
    return (point2[1]-point1[1]) / (point2[0]-point1[0])

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        slope_sorted = {}

        for i in range(len(points)) :
            for k in range(i+1,len(points)) :
                sl = slope(points[i],points[k])
                if sl in slope_sorted.keys() :
                    m = slope_sorted[sl]
                    slope_sorted[sl] =  set(m.append(points[k]).append(points[i]))
        
                else :
                    slope_sorted[sl] = [points[k],points[i]]
        
        print(slope_sorted)




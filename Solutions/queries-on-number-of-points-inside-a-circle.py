"""
Link: https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
"""


def countPoints(points, queries):
    result = [0]*len(queries)
    for point in points:
        x = point[0]
        y = point[1]
        for query_index in range(len(queries)):
            q_x = queries[query_index][0]
            q_y = queries[query_index][1]
            r_square = queries[query_index][2] ** 2
            diff_1 = (x-q_x)**2
            diff_2 = (y-q_y)**2
            if diff_1 + diff_2 <= r_square:
                result[query_index] += 1
    return result


points = [[1,3],[3,3],[5,3],[2,2]]
queries = [[2,3,1],[4,3,1],[1,1,2]]
print(countPoints(points,queries))
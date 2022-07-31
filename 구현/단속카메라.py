from collections import deque
point = []
def solution(routes):
    global point
    answer = 1
    for r in routes:
        if r[0] > r[1]:
            r[1], r[0] = r[0], r[1]
    
    routes = deque(sorted(routes, key =lambda x: x[1]))
    # print(routes)
    s, e = routes.popleft()
    point = [e]
    while(routes):
        start, end = routes[0]
        if start <= e:
            routes.popleft()
        else:
            answer += 1
            if routes:
                s, e = routes.popleft()
                point.append(e)

    return answer

# print(solution([[200,201], [-2,0], [5, 7], [0, 8]]))
# print(point)
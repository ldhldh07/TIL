def ccw(x1, y1, x2, y2, x3, y3):
    cross_product = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
    if cross_product > 0 : 
        return 1 # 반시계 방향
    elif cross_product < 0 :
        return -1 # 시계 방향
    else :
        return 0 # 일직선


# 선분 AB와 선분 CD의 교차 여부를 판단하는 함수
def is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    # 두 선분 중 하나라도 같은 끝점을 가지면 교차
    if [x1, y1] == [x3, y3] or [x1, y1] == [x4, y4] or [x2, y2] == [x3, y3] or [x2, y2] == [x4, y4]:
        return True
    
    ab = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    cd = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

    # 두 선분이 일직선에 있는 경우
    if ab == 0 and cd == 0:
        if [x1, y1] > [x2, y2]:
            x1, y1, x2, y2 = x2, y2, x1, y1
        if [x3, y3] > [x4, y4]:
            x3, y3, x4, y4 = x4, y4, x3, y3
        return not((x2 < x3) or (x4 < x1))

    return ab <= 0 and cd <= 0

print(is_intersect(0, 0, 1, 1, 1, 0, 0, 1))  # 두 선분이 교차하므로 True
print(is_intersect(0, 0, 1, 1, 2, 2, 3, 3))  # 두 선분이 교차하지 않으므로 False

def josephus(people):
    circle = []
    for i in range(people):
        circle.append(i+1)
    while len(circle)>1:
        circle.pop(1)
        circle.append(circle.pop(0))
    return circle[0]

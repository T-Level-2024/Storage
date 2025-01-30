def josephus(people):
    circle = []
    for i in range(people):
        circle.append(i+1)
    while len(circle)>1:
        print(circle[0], circle[1], circle)
        circle.pop(1)
        circle.append(circle.pop(0))
    print(circle)
    return circle[0]

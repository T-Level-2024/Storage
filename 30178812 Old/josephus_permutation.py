def who_goes_free(n, k):
    circle = []
    for i in range(n):
        circle.append(i)
    while len(circle)>1:
        try:
            print(circle[k-1], circle)
            circle.pop(k-1)
            for i in range(0, k-1):
                circle.append(circle.pop(0))
        except IndexError:
            print("Index error: lite")
            while True:
                try:
                    k -= len(circle)
                    print(circle[k-1], circle[k], circle)
                    circle.pop(k)
                    print("Len "+str(range(len(circle))))
                    for i in range(len(circle)):
                        print(circle[0], "Test")
                        circle.append(circle.pop(0))
                        print(circle[0], circle)
                    break
                except IndexError:
                    print("Index error")
                
    print(circle)
    return circle[0]

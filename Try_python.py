if __name__ == '__main__':
    firstl = list()
    secondl = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        firstl.append(name)
        firstl.append(score)
        #print(firstl)
        for i in range(1):
            secondl.append(firstl)
    print(secondl)



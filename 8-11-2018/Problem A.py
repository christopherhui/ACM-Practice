aList = [int(x) for x in input().split()]
n, m = aList[0], aList[1]
map = {}
king = input()
map[king] = 1
for i in range(n):
    famTree = [int(x) for x in input().split()]
    if famTree[1] in map:
        if famTree[2] in map:
            map[famTree[0]] = (map[famTree[1]] + map[famTree[2]]) / 2
        else:
            map[famTree[0]] = (map[famTree[1]]) / 2
            map[famTree[2]] = 0

    elif famTree[2] in map:
        if famTree[1] in map:
            map[famTree[0]] = (map[famTree[1]] + map[famTree[2]]) / 2
        else:
            map[famTree[0]] = (map[famTree[2]]) / 2
            map[famTree[1]] = 0

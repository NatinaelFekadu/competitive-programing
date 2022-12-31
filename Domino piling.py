def maximumDomino(size1,size2):
    area=size1 * size2
    result=area // 2
    return result
size1, size2 = map(int, input().split())
print(maximumDomino(size1,size2))

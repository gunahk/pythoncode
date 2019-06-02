list = [67,67,767,345,7,2,34,45,4545,45]
MiddleIndex=int(len(list)/2)


print('list is',list )
print('Middle number in  list is ',list[MiddleIndex])

print('starting list to middle is ',list[:MiddleIndex])
print('Middlen list to end is ',list[MiddleIndex:])


Temp=list.copy()
NewList=Temp[:MiddleIndex]

list.sort()
print('Sorted list in order',list)

print('sorting list in acending order to middle is ',list[:MiddleIndex])
print('sorting list in acending order from middle to end is ',list[MiddleIndex:])

print('Smalest 3 numbers in list ',list[:3])
print('Median number in list ',list[MiddleIndex+1])

NewList.sort()
print('starting list upto middle acending order is',NewList[:MiddleIndex])

NewList.sort(reverse=True)
print('starting list in upto middle decending order is ',NewList[:MiddleIndex])
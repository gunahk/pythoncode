my_input=input('enter the numbers that can store in the list  :')
my_list=my_input.split(',')
mylist=list(my_list)

#mylist = [67,67,767,345,7,2,34,45,4545,45]
MiddleIndex=int(len(mylist)/2)


print('mylist is',mylist )
print('Middle item in list is ',mylist[MiddleIndex])

print('starting item in list to middle item in list is ',mylist[:MiddleIndex])
print('Middle item in list to end item in list ',mylist[MiddleIndex:])


Temp=mylist.copy()
Newmylist=Temp[:MiddleIndex]

mylist.sort()
print('Sorted mylist in order',mylist)

print('sorted items in list in acending order to middle item is ',mylist[:MiddleIndex])
print('sorted items in list in acending order from middle item to end item is ',mylist[MiddleIndex:])

print('Smalest 3 items in list ',mylist[:3])
print('Median number in list ',mylist[MiddleIndex+1])

Newmylist.sort()
print('starting item in mylist upto middle item in ascending order is',Newmylist[:MiddleIndex])

Newmylist.sort(reverse=True)
print('starting item in mylist  upto middle item in decending order is ',Newmylist[:MiddleIndex])

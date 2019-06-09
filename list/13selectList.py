my_input=input('enter the numbers that can store in the list  :')
my_list=my_input.split(',')
myList=list(my_list)

index=int(input(f"Select the index from the List {myList}"))
print(f'{myList[index-1]} is selected')
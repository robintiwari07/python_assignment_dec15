arbitrary_list = [1, 2, 4, 4, 3, 5, 6]
for i in range(0,len(arbitrary_list)):
    print(arbitrary_list[i])

print("After cubing, we get values as")
empty_list=[]
for i in range(0, len(arbitrary_list)):
    cubed=(arbitrary_list[i]**3)
    print(cubed)
    empty_list.append(cubed)

print("list after cubing all the numbers are: ",empty_list)

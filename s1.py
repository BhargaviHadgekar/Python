# mylist = [ "one", "two", "three" ]
# mylist1= [ "four", "five", "six" ]
# newlist = mylist + mylist1
# print(newlist)
# # Output: ['one', 'two', 'three', 'four', 'five', 'six']

# mylist.extend(mylist1)
# print(mylist)
# # Output: ['one', 'two', 'three', 'four', 'five', 'six']

# mylist += mylist1
# print(mylist)
# # Output: ['one', 'two', 'three', 'four', 'five', 'six', 'four', 'five', 'six']

# list1= [1, 2, 3]
# list2= [4, 5, 6]
# list1.append(list2)
# print(list1)
# # Output: [1, 2, 3, [4, 5, 6]]
# list1= [1, 2, 3]
# list2= [4, 5, 6]
# list1.insert(3, list2)
# print(list1)
# # Output: [1, 2, 3, [4, 5, 6]]
# list1.index(2)
# print(list1)

# mylist[0] = "JESON"
# print(mylist)

# mylist.pop(0)
# print(mylist)

# mylist.remove("five")
# print(mylist)

# convert list into tuple
my_tuple = (1, 2, 3, 3, 4)
temp_list = list(my_tuple)
print(temp_list)
temp_list.remove(3)
my_tuple = tuple(temp_list)
my_tuple
print(my_tuple)  # (1, 2, 3)
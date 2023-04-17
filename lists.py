list_of_numbers = [77, 23, 46, 1337]

print(list_of_numbers)

#add to list - append
list_of_numbers.append(30)
print(list_of_numbers)

#access items from a list
print(list_of_numbers[0])
print(list_of_numbers[3])

#slicing lists
print(list_of_numbers[0:2])

#sorts list
list_of_numbers.sort()
print(list_of_numbers)
print(list_of_numbers.reverse())
print(list_of_numbers.clear()) #clears list
list_inside_list = [["acebook", "password"], ["makersbnb","123456"], ["chitter", "qwerty"]]
print(list_inside_list)
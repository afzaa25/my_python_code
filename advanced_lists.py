# numbers = [1,2,3,4,5]
# numbers.append(6)
# print(numbers)
# numbers.append(7)
# print(numbers)


# passwords = [
# {'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
# {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'}
# ]

# def find_acebook(passwords):
#     for password in passwords:
#         if password['service'] == 'acebook':
#             return password

# print(find_acebook(passwords))

passwords = [
{'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
{'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'}
]

def is_acebook(password):
    return password['service'] == 'acebook'

print(next(filter(is_acebook, passwords)))

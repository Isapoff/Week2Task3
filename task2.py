# Задачи на темy: Списки, Методы списков(p.1)
# 1
# names = ['john', 'Jessica', 'Jerry', 'Tom', 'Ben']
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])

# 2
# cars = ['BMW X5', 'Subaru BRZ', 'Nissan GTR']
# my_car = ("My favorite car is " + cars[2].title() + ".")
# print(my_car)

# motorcycles = ['honda', 'suzuki', 'BMW'] 
# moto = ('I like ' + motorcycles[1].title() + ' motorcycles')
# print(moto)

# 3
# s = ['str1', 'str2']
# s.reverse()
# print(s)

# 4
# num = [1, 2, 3, 4, 5, 6, 7]
# res = len(num) // 2 + len(num) % 1
# a = (num[3:7])
# b = (num[0:3])
# print(a + b)


# Задачи на темy: Списки, Методы списков(р.2)
# 1
# guests = ["Belek! ", "Baha! ", "Arsen! "]
# for friend in guests:
#     print('Hello ' + friend.title() + 'Come for lunch today.')

# 2
# guests = ["Belek ", "Baha ", "Arsen "]
# friend = guests.pop(0)
# print(friend.title() + 'can\'t come today.')
# friend = guests.insert(0, 'Ali ')
# friend = guests.pop(0)
# print('Today come ' + friend.title())
# guests = ["Ali ", "Baha ", "Arsen "]
# for friend in guests:
#     print('Hello ' + friend.title() + 'Come for lunch today.')

# 3
# guests = ["Ali", "Baha ", "Arsen "]
# guests.insert(0, "Bakyt ")
# guests.insert(2, "Azat ")
# guests.append('Adil ')
# for friend in guests:
#     print('Hello ' + friend.title() + 'Come for lunch today.')


# 4
# guests = ["Ali ", "Baha ", "Arsen ", "Bakyt ", "Azat ", "Adil "]
# friend = guests.pop(1)
# print('Hello, ' + friend.title() + 'I\'m sorry to cancel invitation.')
# friend = guests.pop(2)
# print('Hello, ' + friend.title() + 'I\'m sorry to cancel invitation.')
# friend = guests.pop(1)
# print('Hello, ' + friend.title() + 'I\'m sorry to cancel invitation.')
# friend = guests.pop()
# print('Hello, ' + friend.title() + 'I\'m sorry to cancel invitation.')

# friend = ('Hello, ' + guests[0].title() + 'the previous invintation remains valid.')
# print(friend)
# friend = ('Hello, ' + guests[1].title() + 'the previous invintation remains valid.')
# print(friend)

# del(guests[0])
# del(guests[0])
# print(guests)

# 5
# suitcase = []
# suitcase.append('glasses')
# suitcase.append('towel')
# suitcase.append('shorts')
# suitcase.append('phone')
# suitcase.append('shirt')
# print(suitcase)
# suitcase.pop()
# print(suitcase)
# suitcase.insert(0, 'book')
# print(suitcase)

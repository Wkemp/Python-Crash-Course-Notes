my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("The first three items in my foods list are:")
for item in my_foods[:3]:
    print(item.title())

print("Three items from the middle of the list are:")
for item in my_foods[1:4]:
    print(item.title())

print("The last three items from my list are:")
for item in my_foods[1:]:
    print(item.title())
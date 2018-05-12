usernames = ['admin', 'ndangelo', 'user03', 'user04', 'user05']

for user in usernames:
    if user =='admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user.title() + ", thank you for logging in again.")
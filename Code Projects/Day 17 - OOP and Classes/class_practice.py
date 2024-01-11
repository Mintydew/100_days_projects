class User:

    def __init__(self, user_id, username):
        print("new user being created...")
        # You can change the name of the variable/parameter on however you want it (e.g. self.id does not match user_id
        # and that's ok)
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1 # The user who wer are following goes up by one
        self.following += 1 # And the users own following count also goes up by one

# user_1 = User()
# user_1.id = "001"
# user_1.username = "danny"
#
# # Setting up attributes and calling it
# print(user_1.username)

user_1 = User(1, "Jill")
user_2 = User(2, "Jack")

# print(user_2.id)
# print(user_2.followers)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

class Friend:
    def __init__(self, user_name, real_name, last_online):
        self.user_name = user_name
        self.real_name = real_name
        self.last_online = last_online
    def friend_info(self):
        print(f"Username: {self.user_name}")
        print(f"Name: {self.real_name}")
        print(f"Last Online (hours): {self.last_online}")

friend_list = []

with open('FriendList/friends.txt', 'r') as file:
    for line in file:
        friend_data = line.strip().split(',')
        if len(friend_data) == 3:
            userName = friend_data[0].strip()
            realName = friend_data[1].strip()
            lastOnline = int(friend_data[2].strip())

            friend = Friend(userName, realName, lastOnline)
            friend_list.append(friend)

for friend in friend_list:
    friend.friend_info()
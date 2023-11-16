#Creates the class "Friend"
class Friend:
    #Initializes members of friend object
    def __init__(self, user_name, real_name, last_online):
        self.user_name = user_name
        self.real_name = real_name
        self.last_online = last_online
    
    #Prints members of friend object
    def __str__(self):
        return (f"Username: {self.user_name}\nReal Name: {self.real_name}\nHours since Last Online: {self.last_online}\n")

#method that fills the global friend list array with the data from friends.txt
def initialize_friend_list(file_path):
    friend_list = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                friend_data = line.strip().split(',')
                if len(friend_data) == 3:
                    userName = friend_data[0].strip()
                    realName = friend_data[1].strip()
                    lastOnline = int(friend_data[2].strip())

                    friend = Friend(userName, realName, lastOnline)
                    friend_list.append(friend)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except ValueError:
        print("Error: Invalid data format in the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return friend_list



# Remove Friend Function
def remove_friend(friend_list, user_name):
    try:
        for i, friend in enumerate(friend_list):
            if friend.user_name == user_name:
                del friend_list[i]
                print(f"Removed friend: {user_name}")
                return
            
        raise ValueError(f"No friend found with username: {user_name}")
    except ValueError as e:
        print(e)

class Friend:
    def __init__(self, user_name, real_name, player_score):
        self.user_name = user_name
        self.real_name = real_name
        self.player_score = player_score
    def friend_info(self):
        print(f"Username: {self.user_name}")
        print(f"Name: {self.real_name}")
        print(f"Player Score: {self.player_score}")

friend_list = []
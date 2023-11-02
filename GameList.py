
class Game:
    def __init__(self, game_title, hours_played, num_achievements):
        self.game_title = game_title
        self.hours_played = hours_played
        self.num_achievements = num_achievements

    def game_info(self):
        print(f"Game: {self.title}")
        print(f"Hours: {self.hours}")
        print(f"Achievements: {self.achievements}")

game_list = []
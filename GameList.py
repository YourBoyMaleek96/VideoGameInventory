
class Game:
    def __init__(self, game_title, hours_played, num_achievements):
        self.game_title = game_title
        self.hours_played = hours_played
        self.num_achievements = num_achievements

    def game_info(self):
        print(f"Game: {self.game_title}")
        print(f"Hours: {self.hours_played}")
        print(f"Achievements: {self.num_achievements}")

game_list = []

with open('GameList/games.txt', 'r') as file:
    for line in file:
        game_data = line.strip().split(',')
        if len(game_data) == 3:
            title = game_data[0].strip()
            hours = int(game_data[1].strip())
            achievements = int(game_data[2].strip())

            game = Game(title, hours, achievements)
            game_list.append(game)

for game in game_list:
    game.game_info()
#Creates the class "Game"
class Game:
    #Initializes members of game object
    def __init__(self, game_title, hours_played, num_achievements):
        self.game_title = game_title
        self.hours_played = hours_played
        self.num_achievements = num_achievements

    #Prints members of game object
    def __str__(self):
        return (f"Game Title: {self.game_title}\n Hours Played: {self.hours_played}\n Number of Achievements: {self.num_achievements}")

#method that fills the global games list array with the data from games.txt
def initialize_game_list(file_path):
    game_list = []
    with open(file_path, 'r') as file:
        for line in file:
            game_data = line.strip().split(',')
            if len(game_data) == 3:
                title = game_data[0].strip()
                hours = int(game_data[1].strip())
                achievements = int(game_data[2].strip())

                game = Game(title, hours, achievements)
                game_list.append(game)
    
    return game_list
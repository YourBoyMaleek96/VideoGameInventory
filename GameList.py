#Creates the class "Game"
class Game:
    #Initializes members of game object
    def __init__(self, game_title, hours_played, num_achievements):
        self.game_title = game_title
        self.hours_played = int(hours_played)
        self.num_achievements = int(num_achievements)

    #Prints members of game object
    def __str__(self):
        return (f"Game Title: {self.game_title}\nHours Played: {self.hours_played}\nNumber of Achievements: {self.num_achievements}\n")

#method that fills the global games list array with the data from games.txt
def initialize_game_list(file_path):
    game_list = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                game_data = line.strip().split(',')
                if len(game_data) == 3:
                    title = game_data[0].strip()
                    hours = int(game_data[1].strip())
                    achievements = int(game_data[2].strip())

                    game = Game(title, hours, achievements)
                    game_list.append(game)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except ValueError:
        print("Error: Invalid data format in the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return game_list

def calculate_achievement_score(list):
    total_achievements = 0

    for game in list:
        total_achievements += game.num_achievements
   
    return total_achievements
   
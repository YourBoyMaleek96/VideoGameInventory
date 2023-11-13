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

#Add Game Function
def add_game(game_list, title, hours, achievements):
    try:
        hours = int(hours)
        achievements = int(achievements)
        new_game = Game(title, hours, achievements)
        game_list.append(new_game)
    except ValueError:
        print("Invalid data: 'hours played' and 'number of achievements' must be integers.")
    except Exception as e:
        print(f"An error occurred: {e}")

#Remove Game Function
def remove_game(game_list, title):
    try:
        for i, game in enumerate(game_list):
            if game.game_title == title:
                del game_list[i]
                print(f"Removed game: {title}")
                return
        
        raise ValueError(f"No game found with title: {title}")
    except ValueError as e:
        print(e)


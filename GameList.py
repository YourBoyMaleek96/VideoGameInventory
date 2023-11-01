
class Game:
    def __init__(self, title, hours, achievements):
        self.title = title
        self.hours_played = hours
        self.achievements = achievements

    def game_list(self):
        print(f"Game: {self.title}")
        print(f"Hours: {self.hours}")
        print(f"Achievements: {self.achievements}")

games = [
    {"title": "NBA 2K", "hours": 400, "achievements": 13},
    {"title": "Zelda: Breath of the Wild", "hours": 256, "achievements": 32},
    {"title": "Dark Souls I", "hours": 331, "achievements": 38},
    {"title": "Call of Duty: Black Ops I", "hours": 142, "achievements": 21},
    {"title": "Chivalry II", "hours": 35, "achievements": 3},
    {"title": "Mario Kart 8", "hours": 696, "achievements": 52},
    {"title": "Spiderman II", "hours": 12, "achievements": 2},
    {"title": "Sea of Thieves", "hours": 502, "achievements": 163},
    {"title": "Super Mario Bros", "hours": 72, "achievements": 18},
    {"title": "Silent Hill 2", "hours": 16, "achievements": 7}
]

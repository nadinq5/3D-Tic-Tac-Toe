import csv
class Player():
    def __init__(self, name='', age='', country='', score=0, wins=0, total_games=0):
        self.name = name
        self.age = age
        self.country = country
        self.score = score
        self.wins = wins
        self.total_games = total_games

    def player_exists(self, player_name):
        with open('players.csv') as players_objects:
            players_objects.seek(0)
            reader_obj = csv.DictReader(players_objects)
            existing_players_list = list(reader_obj)
            for existing_player in existing_players_list:
                existing_player_name = existing_player.get('name')
                if existing_player_name == player_name:
                    player_found = Player(
                            name=existing_player.get('name'),
                            age=existing_player.get('age'),
                            country=existing_player.get('country'),
                            score=int(existing_player.get('score')),
                            wins=int(existing_player.get('wins')),
                            total_games=int(existing_player.get('total_games'))
                    )
                    print(f"Player found, welcome back, {player_name}")
                    return player_found
        return None




    def add_score(self):
        self.score += 1

    def add_wins(self):
        self.wins += 1

    def add_total_games(self):
        self.total_games += 1


def main():
    pass

if __name__ == "__main__":
    main()

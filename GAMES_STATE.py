from PLAYER import Player
from RULES import Rules
from CUBE import Cube
from MATRIX import Matrix
import time
import sys
import csv

def prGreen(skk):
    print("\033[92m {}\033[00m" .format(skk))

class Game_State():
    def __init__(self):
        pass

    def play_turn(self, cube, player):

        # for remaining in range(60, 0, -1):
        #     sys.stdout.write("\r")
        #     sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        #     sys.stdout.flush()
        #     time.sleep(1)

        floor = input(f'{player.name} please enter 2 for Top, 1 for Middle and 0 for Bottom: ')
        validate_floor = True
        while validate_floor:
            if not 0 <= int(floor) <= 2:
                floor = input(f'Invalid floor. Please enter 2 for Top, 1 for Middle and 0 for Bottom: ')
            else:
                validate_floor = False

        floor = Rules.floor_dictionary.get(floor)

        if not getattr(cube, floor).check_full():
            floor = input(f'Floor {floor} already full, please enter another floor.')
            floor = Rules.floor_dictionary.get(floor)

        x_cord = input(f'{player.name} please enter x coordinate (0, 1, 2): ')
        y_cord = input(f'{player.name} please enter y coordinate (0, 1, 2): ')

        valid_input_loop = False

        while not valid_input_loop:
            if not (0 <= int(x_cord) <= 2 and 0 <= int(y_cord) <= 2):
                x_cord = input(f'Invalid coordinates, please enter x coordinate (0, 1, 2): ')
                y_cord = input(f'Invalid coordinates, please enter y coordinate (0, 1, 2): ')

            elif getattr(cube, floor).matrix[int(y_cord)][int(x_cord)] != '_':
                print(f'Please enter another set of coordinates. Coordinate already populated.')
                x_cord = input(f'Invalid coordinates, please enter x coordinate (0, 1, 2): ')
                y_cord = input(f'Invalid coordinates, please enter y coordinate (0, 1, 2): ')
            else:
                valid_input_loop = True

        return x_cord, y_cord, floor


    def game_start(self, player1, player2):
        turn_counter = 0
        top_matrix = Matrix()
        middle_matrix = Matrix()
        bottom_matrix = Matrix()
        cube = Cube(top_matrix, middle_matrix, bottom_matrix)

        print(f'{player1.name} uses X.')
        print(f'{player2.name} uses O.')
        print(cube)
        while turn_counter < 28:
            x_cord, y_cord, floor = self.play_turn(cube, player1)
            getattr(cube, floor).matrix[int(y_cord)][int(x_cord)] = 'X'
            turn_counter += 1
            self.check_win(cube, floor, x_cord, y_cord, 'X', player1, player2)
            print(cube)

            x_cord, y_cord, floor = self.play_turn(cube, player2)
            getattr(cube, floor).matrix[int(y_cord)][int(x_cord)] = 'O'
            turn_counter += 1
            print(floor)
            self.check_win(cube, floor, x_cord, y_cord, 'O', player2, player1)
            print(cube)
        print(f'Tie! No winners.')
        self.restart(player1, player2)


    def start(self):
            print(f'Hello, welcome to 3D Tic-Tac-Toe.')
            player1_name = input(f'Please enter the name of the first player: ')
            first_player = Player()
            first_player = first_player.player_exists(player1_name)

            if first_player == None:
                print(f'New player, welcome.')
                age = input("Please enter your age: ")
                country = input("Please enter your nationality: ")
                first_player = Player(player1_name, age, country)
                with open('players.csv', 'a') as players_objects:
                    players_objects.write(f'{player1_name},{age},{country},{0},{0},{0}\n')

            player2_name = input(f'Please enter the name of the second player: ')
            second_player = Player()
            second_player = second_player.player_exists(player2_name)

            if second_player == None:
                print(f'New player, welcome.')
                age = input("Please enter your age: ")
                country = input("Please enter your nationality: ")
                second_player = Player(player2_name, age, country)
                with open('players.csv', 'a') as players_objects:
                    players_objects.write(f'{player2_name},{age},{country},{0},{0},{0}\n')
            self.game_start(first_player, second_player)

    def restart(self, player1, player2):
        valid_input = False
        while not valid_input:
            play_again = input(f'Would you like to play another game? (Yes/No): ')
            play_again = play_again.lower()
            if play_again == 'yes':
                valid_input = True
                self.game_start(player1, player2)
            elif play_again == 'no':
                print('Exiting game... Thanks for playing')
                exit()
            else:
                print('Please enter a valid input.')

    def check_win_2d(self, cube, floor, x_cord, y_cord, x_or_o):
        possible_solutions = []
        for i in Rules.TWOD_WIN_STATES:
            for j in i:
                new_tuple = (int(y_cord), int(x_cord))
                # print(j)
                # print(new_tuple)
                if new_tuple == j:
                    # print(i)
                    possible_solutions.append(i)

        for i in possible_solutions:
            score_counter = 0
            for j in i:
                if getattr(cube, floor).matrix[j[0]][j[1]] == x_or_o:
                    score_counter += 1
            if score_counter == 3:
                return True
        return False

    def check_win_vertical(self, cube, x_cord, y_cord, x_or_o):
        counter = 0
        if cube.T.matrix[int(y_cord)][int(x_cord)] == x_or_o:
            counter += 1
        if cube.M.matrix[int(y_cord)][int(x_cord)] == x_or_o:
            counter += 1
        if cube.B.matrix[int(y_cord)][int(x_cord)] == x_or_o:
            counter += 1
        if counter == 3:
            return True
        else:
            return False

    def check_win_diag(self, cube, floor, x_cord, y_cord, x_or_o):
        counter = 0
        possible_solutions = []
        for i in Rules.TWOD_WIN_STATES:
            for j in i:
                new_tuple = (int(y_cord), int(x_cord))
                if new_tuple == j:
                    possible_solutions.append(i)

        if Rules.floor_dictionary.get(floor) == 'T':
            for k in possible_solutions:
                if k.index((y_cord, x_cord)) == 2:
                    k = k.reverse()
        elif Rules.floor_dictionary.get(floor) == 'B':
            for k in possible_solutions:
                if k.index((y_cord, x_cord)) == 0:
                    k = k.reverse()
        elif Rules.floor_dictionary.get(floor) == 'M':
            for k in range(len(possible_solutions)):
                possible_solutions.append(possible_solutions[k].reverse())
        print(possible_solutions)
        for i in possible_solutions:
            top_floor_coordinates = i[0]
            middle_floor_coordinates = i[1]
            bottom_floor_coordinates = i[2]

            counter = 0
            if cube.T.matrix[top_floor_coordinates[0]][top_floor_coordinates[1]] == x_or_o:
                counter += 1
            if cube.M.matrix[middle_floor_coordinates[0]][middle_floor_coordinates[1]] == x_or_o:
                counter += 1
            if cube.B.matrix[bottom_floor_coordinates[0]][bottom_floor_coordinates[1]] == x_or_o:
                counter += 1
            if counter == 3:
                return True
        return False

    # def check_wins:
    #     pass
    def check_win(self, cube, floor, x_cord, y_cord, x_or_o, player, player2):
        if self.check_win_2d(cube, floor, x_cord, y_cord, x_or_o) == True:
            print(cube)
            self.end(player, player2)

        if self.check_win_vertical(cube, x_cord, y_cord, x_or_o):
            print(cube)
            self.end(player, player2)

        if floor != 'M':
            if self.check_win_diag(cube, floor, x_cord, y_cord, x_or_o) == True:
                print(cube)
                self.end(player, player2)
        elif floor == 'M' and x_cord == 1 and y_cord == 1:
            if self.check_win_diag(cube, floor, x_cord, y_cord, x_or_o) == True:
                print(cube)
                self.end(player, player2)

    def end(self, player, player2):
        prGreen(f'Congratulations {player.name}, you have won!')
        # print(f'Congratulations {player.name}, you have won!')
        player.add_score()
        player.add_wins()
        player.add_total_games()
        player2.add_total_games()
        print(f'Wins: {player.wins}')
        print(f'Total Score: {player.score}')
        self.update_user('players.csv', player.name, player.score, player.wins, player.total_games)
        self.update_user('players.csv', player2.name, player2.score, player2.wins, player2.total_games)
        self.restart(player, player2)
        # with open('players.csv', 'r+') as players_objects:
        #     list_of_lines = players_objects.readlines()
        #     for line in list_of_lines:
        #         line_split = line.split(',')
        #         if line_split[0] == player.name:
        #             line_split[3] = str(int(line_split[3]) + 1)
        #             line_split[4] = str(int(line_split[4]) + 1)
        #             line_split[5] = str(int(line_split[5]) + 1)
        #             updated_row = f'{line_split[0]},{line_split[1]},{line_split[2]},{line_split[3]},{line_split[4]},{line_split[5]}'
        #             print(f'Updated line: {updated_row}')
        #             players_objects.write(line.replace(line, updated_row))
        #         if line_split[0] == player2.name:
        #             line_split[5] = str(int(line_split[5]) + 1)
        #             updated_row = f'{line_split[0]},{line_split[1]},{line_split[2]},{line_split[3]},{line_split[4]},\
        #                                                 {line_split[5]}'
        #             players_objects.write(line.replace(line, updated_row))


    def update_user(self, file_name, name_to_find, score, wins, total_games):
        updated_data = []
        with open('players.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                name = row['name']
                if name == name_to_find:
                    # Update the attributes
                    row['score'] = str(score)
                    row['wins'] = str(wins)
                    row['total_games'] = str(total_games)
                updated_data.append(row)
        with open(file_name, 'w', newline='') as csv_file:
            fieldnames = ['name', 'age', 'country', 'score', 'wins', 'total_games']
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(updated_data)

def main():
    pass

if __name__ == "__main__":
    main()
from PLAYER import Player
from RULES import Rules
class Game_State():


    def game_start(self):
        pass
    def start(self, player1=None, player2=None):
        if(player1 != None and player2 != None):
            self.game_start(player1, player2)
        else:
            print(f'Hello, welcome to 3D Tic-Tac-Toe.')
            player1_name = input(f'Please enter the name of the first player: ')
            player_exists(player1_name)





            player1 = Player()
            player2 = Player()
            player1.input_player()

    def restart(self, player1, player2):
        valid_input = False
        while not valid_input:
            play_again = input(f'Would you like to play another game? (Yes/No)')
            if play_again == 'Yes':
                self.start(player1, player2)
                valid_input = True
            elif play_again == 'No':
                print('Exiting game... Thanks for playing')
                exit()
            else:
                print('Please enter a valid input.')

    def check_win_2d(self, floor, x_cord, y_cord, x_or_o):
        possible_solutions = []
        for i in Rules.TWOD_WIN_STATES:
            for j in i:
                if (y_cord, x_cord) == j:
                    possible_solutions.append(i)

        for i in possible_solutions:
            score_counter = 0
            for j in i:
                if floor[j[0]][j[1]] == x_or_o:
                    score_counter += 1
            if score_counter == 3:
                return True
        return False

    def check_win_vertical(self, cube, x_cord, y_cord, x_or_o):
        counter = 0
        if cube.T[y_cord][x_cord] == x_or_o:
            counter += 1
        if cube.M[y_cord][x_cord] == x_or_o:
            counter += 1
        if cube.B[y_cord][x_cord] == x_or_o:
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
                if (y_cord, x_cord) == j:
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

        for i in possible_solutions:
            top_floor_coordinates = i[0]
            middle_floor_coordinates = i[1]
            bottom_floor_coordinates = i[2]

            counter = 0
            if cube.T[top_floor_coordinates[0]][top_floor_coordinates[1]] == x_or_o:
                counter += 1
            if cube.M[middle_floor_coordinates[0]][middle_floor_coordinates[1]] == x_or_o:
                counter += 1
            if cube.B[bottom_floor_coordinates[0]][bottom_floor_coordinates[1]] == x_or_o:
                counter += 1
            if counter == 3:
                return True
        return False

    # def check_wins:
    #     pass
    def check_win(self, cube, floor, x_cord, y_cord, x_or_o, player, player2):
        if self.check_win_2d(floor, x_cord, y_cord, x_or_o) == True:
            self.end(player, player2)

        if self.check_win_vertical(cube, x_cord, y_cord, x_or_o):
            self.end(player, player2)

        if floor != 'M':
            if self.check_win_diag(self, cube, floor, x_cord, y_cord, x_or_o) == True:
                self.end(player, player2)
        elif floor == 'M' and x_cord == 1 and y_cord == 1:
            if self.check_win_diag(self, cube, floor, x_cord, y_cord, x_or_o) == True:
                self.end(player)

    def end(self, player, player2):
        print(f'Congratulations {player.name}, you have won!')
        player.add_score()
        player.add_wins()
        print(f'Wins: {player.wins}')
        print(f'Total Score: {player.score}')
        self.restart(player, player2)

# def main():
#     cube =


# if __name__ == "__main__":
#     main()
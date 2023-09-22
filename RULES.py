from MATRIX import Matrix
from CUBE import Cube

class Rules:
    TWOD_WIN_STATES = [[(0, 0), (0, 1), (0, 2)],
                     [(0, 0), (1, 0), (2, 0)],
                     [(0, 0), (1, 1), (2, 2)],
                     [(1, 0), (1, 1), (1, 2)],
                     [(2, 0), (2, 1), (2, 2)],
                     [(0, 1), (1, 1), (2, 1)],
                     [(0, 2), (1, 2), (2, 2)],
                     [(2, 0), (1, 1), (0, 2)]]

    floor_dictionary = {'0': 'B', '1': 'M', '2': 'T'}

    VERTICAL_WIN_STATES = []

    def validate_assignment(self, x_or_o, x_cord, y_cord, floor, cube):
        # floor_dictionary = {'0': 'B', '1': 'M', '2': 'T'}
        if(cube.floor_dictionary.get(floor)[y_cord][x_cord] != 0):
            return False
        else:
            return True


    # def assign(self, x_or_o, x_cord, y_cord, z_cord):
    #     if(validate_assignment(x_or_o, x_cord, y_cord, floor, cube)):
    #         cube.floor_dictionary.get(floor)[y_cord][x_cord] = x_or_o

    def players_turn(self, player):
        pass


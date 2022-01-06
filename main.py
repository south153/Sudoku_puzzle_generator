import random

row1, row2, row3, row4, row5, row6, row7, row8, row9 = [], [], [], [], [], [], [], [], []



def create_row(row):
    '''
    Creates row
    :param row:
    :return:
    '''
    no_dups = []
    while len(no_dups) < 9:       # generates random integers while list of no dups is less than 9
        row.append(random.randint(0, 9))   # could use random.sample do make this more efficent instead of looping
        for number in row:
            if number not in no_dups:   # if the given number is not in no dups it
                no_dups.append(number)
    return no_dups


# clean this up with for loop
board = [create_row(row1)] + [create_row(row2)] + [create_row(row3)] + [create_row(row3)] + [create_row(row4)] + [create_row(row5)] + [create_row(row6)] + [create_row(row7)] + [create_row(row8)] + [create_row(row9)]
print(board)


def create_column(board):
    column = [sublist[0] for sublist in board]
    if column






print(create_column(board))





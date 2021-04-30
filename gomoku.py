"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 26, 2020
"""

def is_empty(board):
    for row in board:
        for square in row:
            if square != " ":
                return False
    return True

def get_opposite(col):
    return "w" if col == "b" else "b"

def is_in_range(board, y, x):
    return 0 <= y < len(board) and 0 <= x < len(board[y])

def is_seq(board, y, x, col):
    return is_in_range(board, y, x) and board[y][x] == col

def is_bound(board, y, x, col):
    return not (is_seq(board, y, x, col) or is_seq(board, y, x, " "))

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    col = board[y_end][x_end]
    end_blocked = is_bound(board, y_end+d_y, x_end+d_x, col)
    start_blocked = is_bound(board, y_end-(length*d_y), x_end-(length*d_x), col)

    if start_blocked and end_blocked:
        return "CLOSED"
    elif not start_blocked and not end_blocked:
        return "OPEN"
    return "SEMIOPEN"

def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count, semi_open_seq_count = 0, 0
    y, x = y_start, x_start
    cur_len = 1 if is_seq(board, y, x, col) else 0
    while is_in_range(board, y, x):
        if not is_seq(board, y+d_y, x+d_x, col):
            if cur_len == length:
                result = is_bounded(board, y, x, length, d_y, d_x)
                #print("\t", result, y, x, length, d_y, d_x)
                open_seq_count += 1 if result == "OPEN" else 0
                semi_open_seq_count += 1 if result == "SEMIOPEN" else 0
            cur_len = 0
        else:
            cur_len += 1

        y += d_y
        x += d_x

    return open_seq_count, semi_open_seq_count

def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    y_size = len(board)
    x_size = len(board[0])
    to_check = [[[0], range(x_size), 1, 0],  # vertical
                [range(y_size), [0], 0, 1],  # horizontal
                [[0], range(x_size), 1, 1],
                [range(1, y_size), [0], 1, 1],
                [[0], range(x_size), 1, -1],
                [range(1, y_size), [x_size-1], 1, -1]]

    for ys, xs, d_y, d_x in to_check:
        for y in ys:
            for x in xs:
                opens, semi_opens = detect_row(board, col, y, x, length, d_y, d_x)
                open_seq_count += opens
                semi_open_seq_count += semi_opens
    return open_seq_count, semi_open_seq_count


def search_max(board):
    move_y, move_x, max_score = 0, 0, -100000000000000000000000000000000
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == " ":
                board[y][x] = "b"
                move_score = score(board)
                if move_score > max_score:
                    move_y, move_x, max_score = y, x, move_score
                board[y][x] = " "

    return move_y, move_x

MAX_SCORE = 10000000

def score(board):

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def is_win(board):
    win_len = 5
    draw = True
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == " ":
                draw = False
            for d_y, d_x in ((1, 0), (0, 1), (1, 1), (1, -1)):
                for col in ("w", "b"):
                    if not is_seq(board, y-d_y, x-d_x, col) and all(is_seq(board, y+i*d_y, x+i*d_x, col) for i in range(win_len)) and not is_seq(board, y+(win_len*d_y), x+(win_len*d_x), col):
                        return "White won" if col == "w" else "Black won"
    return "Draw" if draw else "Continue playing"


def print_board(board):
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        #print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            #print("Open rows of length %d: %d" % (i, open))
            #print("Semi-open rows of length %d: %d" % (i, semi_open))




def place_random(board, col):
    import random
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    while(board[y][x] != ' '):
        x = random.randint(0, 7)
        y = random.randint(0, 7)
    board[y][x] = col

def run_games(n_games, a, b, displ):
    board_size = 8
    import gomoku_bib as gbib
    score = [0]*2

    for i in range(n_games):
        board = gbib.pos_to_board(boards[i])

        while True:
            print(score[0], "vs", score[1], end = "\r")
            if is_empty(board):
                move_y = board_height // 2
                move_x = board_width // 2
            else:
                move_y, move_x = a(board, 'b', time=displ)#search_max(board)

            board[move_y][move_x] = "b"
            if displ > 1: print_board(board)

            game_res = is_win(board)
            if game_res in ["White won", "Black won", "Draw"]:
                if game_res == "Black won":
                    score[0] += 1
                if game_res == "White won":
                    score[1] += 1
                break

            move_y, move_x = b(board, "w", time=displ)
            board[move_y][move_x] = "w"
            if displ > 1: print_board(board)

            game_res = is_win(board)
            if game_res in ["White won", "Black won", "Draw"]:
                if game_res == "Black won":
                    score[0] += 1
                if game_res == "White won":
                    score[1] += 1
                break
        if displ: print(score)

        board = gbib.pos_to_board(boards[i])

        while True:
            print(score[0], "vs", score[1], end = "\r")
            if is_empty(board):
                move_y = board_height // 2
                move_x = board_width // 2
            else:
                move_y, move_x = b(board, 'b', time=displ)#search_max(board)

            board[move_y][move_x] = "b"
            if displ > 1: print_board(board)

            game_res = is_win(board)
            if game_res in ["White won", "Black won", "Draw"]:
                if game_res == "Black won":
                    score[1] += 1
                if game_res == "White won":
                    score[0] += 1
                break

            move_y, move_x = a(board, "w", time=displ)
            board[move_y][move_x] = "w"
            if displ > 1: print_board(board)

            game_res = is_win(board)
            if game_res in ["White won", "Black won", "Draw"]:
                if game_res == "Black won":
                    score[1] += 1
                if game_res == "White won":
                    score[0] += 1
                break
        if displ: print(score)
    return score

def play_gomoku(board_size):
    #import mcts
    #import ai
    #import dynamicalphabeta
    #import dynamicalphabeta_new
    #import prow_dynamicalphabeta
    import gomoku_bib as gbib
    import standard_ai
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    place_random(board, "b")
    place_random(board, "w")
    place_random(board, "b")
    place_random(board, "w")

    #dynamicalphabeta_new.move(gbib.pos_to_board(0x10205d00000000080008220008100055), 'w')

    #dynamicalphabeta_new.move(gbib.pos_to_board(0x11c002440040000002238102c000000), 'w')

    while True:
        #print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = standard_ai.move(board, 'b')

        print("Computer move: (%d, %d)" % (move_y, move_x))
        #print(ai.move(board, "b"))
        board[move_y][move_x] = "b"
        print(hex(gbib.make_pos(board, 'w')))
        print_board(board)
        #analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

        import cProfile
        #cProfile.runctx('mcts.move(board, "w")', globals(), locals())
        #cProfile.runctx('dynamicalphabeta_new.move(board, "w")', globals(), locals())
        #move_y, move_x = prow_dynamicalphabeta.move(board, "w")
        #print("My move: (%d, %d)" % (move_y, move_x))
        print(move_y, move_x)
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        #analysis(board)
        print(hex(gbib.make_pos(board, 'w')))
        print_board(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res


def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


boards = {0: 1237940334433286038367502336, 1: 1298074215238169888997549887455232, 2: 4951769601874486838886990080, 3: 40569770967460518397859837509632, 4: 41538374868883083938332760198348800, 5: 9903539203748973677773848644, 6: 10633823967517267022551865554160910336, 7: 1329227995785066988631258889065594880, 8: 42535295865117308089719150572682084352, 9: 4951911273157203306542530560, 10: 159694265067814055736864932096, 11: 5192296868206234185447529728966912, 12: 649195563641881982242048884867584, 13: 633825300704410511673992937472, 14: 10151108322140119380072725479425, 15: 415383748682786210283002656295223296, 16: 5080505921227200929678162395136, 17: 633825375671978427212430835744, 18: 166194064292321787597956557299515392, 19: 5316911983139668213982837010673435136, 20: 2535301200530245849657525665792, 21: 5316911983139672936348195079923433474, 22: 2596148438938820371182281562260484, 23: 41538374869487546848985049471123456, 24: 79228162662414750935523787008, 25: 3169126500570573503741892231232, 26: 162259276829231816891051160895488, 27: 42535295865117312655288871748573855744, 28: 45635421608216258735364882038784, 29: 20769187434139347407680501480226816, 30: 5704427701031643992753591812160, 31: 41538375177763630849589039627042816, 32: 664613997892459118196445752158355456, 33: 309486190414091686076481536, 34: 18926359437218188099584, 35: 604499803305357611106304, 36: 5193564509135056434392762515718144, 37: 88269046595092070261479190168600576, 38: 166153499782599493934321502089379840, 39: 10633824005893408240380639677524213776, 40: 81169252495864390466075568898048, 41: 38686216667593680372107264, 42: 170141183460488574547106980792429969408, 43: 2658455991570133977262535374335377408, 44: 21267688497377861269801760858989133952, 45: 79228181403730269072124837920, 46: 10142442741865121753332803698688, 47: 325152378958540841624641877311488, 48: 85075784027093150695782528963112337408, 49: 2658456308482481802864965044492304896, 50: 664613997892476825917835008721043520, 51: 636301180192685461847905665026, 52: 5316911983139665852798470229994766336, 53: 2658476273979435398630959572418887680, 54: 665263034999774789906032792136843264, 55: 9903520461856994788869406800, 56: 2658455994045711824378796882824003584, 57: 21550060203879899895814846152704, 58: 77673483914778708474331136, 59: 170141193601674033557522515689510141952, 60: 166153499482785890669895114964336640, 61: 1349997183219055185723772054810918928, 62: 309560567685071017407938568, 63: 193428131138340736672497664, 64: 4990445783369198097999593472, 65: 633827717965754070744189371392, 66: 1209516115565733958647808, 67: 39614100146598100275361349632, 68: 21267647932558663411193878708071038976, 69: 159694265067850084259006021632, 70: 5070602401208065511166434115584, 71: 326816170371340462942113103872, 72: 21267647932559258429370722482391089152, 73: 1329228154241240910655854421661974528, 74: 14507109835375824974382080, 75: 1329227995784916463199617419057299456, 76: 2455630575595815205601280, 77: 170141345719746060945050695293895442436, 78: 2417999213190644185956352, 79: 226673591177742970388608, 80: 332306998946833431135759225686327296, 81: 2596148506638670881287533773209600, 82: 324518553960658181687912825881088, 83: 20769227048220567646290782089379844, 84: 5192296860952679267794939050721344, 85: 19342886900810361634033664, 86: 158495010654756413689959546880, 87: 166153816385764541170326256715038784, 88: 324523505418583868304255617106432, 89: 21267647932558654003355527011811459080, 90: 85070591888690940894372331717954371584, 91: 158456325046975423693203701760, 92: 21093705987797737240905141337720832, 93: 79232998217686911299392372736, 94: 40565438177322992545231206875392, 95: 10141205406288745023686259507202, 96: 649037107317443749394262932865024, 97: 31901471898837980949691650921704980496, 98: 332306998951064673810253290982605312, 99: 10141204801899622188285677273088}

if __name__ == '__main__':
    #import baseline
    #import ai
    #import tempfast
    ##import prowfast
    #import tempslow
    #import prowslow
    #import blitz_ai
    #import standard_ai
    #print(run_games(30, standard_ai.move, blitz_ai.move, 1))
    print(play_gomoku(8))
    #print("0:5")
    #print(run_games(15, prowslow.move, ai.move, 0))
    #print("0:8")
    #print(run_games(15, tempslow.move, ai.move, 0))

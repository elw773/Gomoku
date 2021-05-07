from timeit import default_timer as timer
WIN_SCORE = 1000000000000000000000


def bin_to_board(w_bin, b_bin):
    board = []
    i = 0
    for y in range(8):
        board.append([' '] * 8)
        for x in range(8):
            if w_bin >> i & 0x1:
                board[y][x] = "w"
            elif b_bin >> i & 0x1:
                board[y][x] = "b"
            i += 1
    return board


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board


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


def likely_moves(pieces):
    if pieces & 0x70507 << 0 and not (pieces & 0x1 << 9):
        yield 9
    if pieces & 0x70507 << 1 and not (pieces & 0x1 << 10):
        yield 10
    if pieces & 0x70507 << 2 and not (pieces & 0x1 << 11):
        yield 11
    if pieces & 0x70507 << 3 and not (pieces & 0x1 << 12):
        yield 12
    if pieces & 0x70507 << 4 and not (pieces & 0x1 << 13):
        yield 13
    if pieces & 0x70507 << 5 and not (pieces & 0x1 << 14):
        yield 14
    if pieces & 0x70507 << 8 and not (pieces & 0x1 << 17):
        yield 17
    if pieces & 0x70507 << 9 and not (pieces & 0x1 << 18):
        yield 18
    if pieces & 0x70507 << 10 and not (pieces & 0x1 << 19):
        yield 19
    if pieces & 0x70507 << 11 and not (pieces & 0x1 << 20):
        yield 20
    if pieces & 0x70507 << 12 and not (pieces & 0x1 << 21):
        yield 21
    if pieces & 0x70507 << 13 and not (pieces & 0x1 << 22):
        yield 22
    if pieces & 0x70507 << 16 and not (pieces & 0x1 << 25):
        yield 25
    if pieces & 0x70507 << 17 and not (pieces & 0x1 << 26):
        yield 26
    if pieces & 0x70507 << 18 and not (pieces & 0x1 << 27):
        yield 27
    if pieces & 0x70507 << 19 and not (pieces & 0x1 << 28):
        yield 28
    if pieces & 0x70507 << 20 and not (pieces & 0x1 << 29):
        yield 29
    if pieces & 0x70507 << 21 and not (pieces & 0x1 << 30):
        yield 30
    if pieces & 0x70507 << 24 and not (pieces & 0x1 << 33):
        yield 33
    if pieces & 0x70507 << 25 and not (pieces & 0x1 << 34):
        yield 34
    if pieces & 0x70507 << 26 and not (pieces & 0x1 << 35):
        yield 35
    if pieces & 0x70507 << 27 and not (pieces & 0x1 << 36):
        yield 36
    if pieces & 0x70507 << 28 and not (pieces & 0x1 << 37):
        yield 37
    if pieces & 0x70507 << 29 and not (pieces & 0x1 << 38):
        yield 38
    if pieces & 0x70507 << 32 and not (pieces & 0x1 << 41):
        yield 41
    if pieces & 0x70507 << 33 and not (pieces & 0x1 << 42):
        yield 42
    if pieces & 0x70507 << 34 and not (pieces & 0x1 << 43):
        yield 43
    if pieces & 0x70507 << 35 and not (pieces & 0x1 << 44):
        yield 44
    if pieces & 0x70507 << 36 and not (pieces & 0x1 << 45):
        yield 45
    if pieces & 0x70507 << 37 and not (pieces & 0x1 << 46):
        yield 46
    if pieces & 0x70507 << 40 and not (pieces & 0x1 << 49):
        yield 49
    if pieces & 0x70507 << 41 and not (pieces & 0x1 << 50):
        yield 50
    if pieces & 0x70507 << 42 and not (pieces & 0x1 << 51):
        yield 51
    if pieces & 0x70507 << 43 and not (pieces & 0x1 << 52):
        yield 52
    if pieces & 0x70507 << 44 and not (pieces & 0x1 << 53):
        yield 53
    if pieces & 0x70507 << 45 and not (pieces & 0x1 << 54):
        yield 54
    if pieces & (0x30203 << 0) and not (pieces & 0x1 << 8):
        yield 8
    if pieces & (0xc040c0 << 0) and not (pieces & 0x1 << 15):
        yield 15
    if pieces & (0x30203 << 8) and not (pieces & 0x1 << 16):
        yield 16
    if pieces & (0xc040c0 << 8) and not (pieces & 0x1 << 23):
        yield 23
    if pieces & (0x30203 << 16) and not (pieces & 0x1 << 24):
        yield 24
    if pieces & (0xc040c0 << 16) and not (pieces & 0x1 << 31):
        yield 31
    if pieces & (0x30203 << 24) and not (pieces & 0x1 << 32):
        yield 32
    if pieces & (0xc040c0 << 24) and not (pieces & 0x1 << 39):
        yield 39
    if pieces & (0x30203 << 32) and not (pieces & 0x1 << 40):
        yield 40
    if pieces & (0xc040c0 << 32) and not (pieces & 0x1 << 47):
        yield 47
    if pieces & (0x30203 << 40) and not (pieces & 0x1 << 48):
        yield 48
    if pieces & (0xc040c0 << 40) and not (pieces & 0x1 << 55):
        yield 55
    if pieces & (0x705 << 0) and not (pieces & 0x1 << 1):
        yield 1
    if pieces & (0x507000000000000 << 0) and not (pieces & 0x1 << 57):
        yield 57
    if pieces & (0x705 << 1) and not (pieces & 0x1 << 2):
        yield 2
    if pieces & (0x507000000000000 << 1) and not (pieces & 0x1 << 58):
        yield 58
    if pieces & (0x705 << 2) and not (pieces & 0x1 << 3):
        yield 3
    if pieces & (0x507000000000000 << 2) and not (pieces & 0x1 << 59):
        yield 59
    if pieces & (0x705 << 3) and not (pieces & 0x1 << 4):
        yield 4
    if pieces & (0x507000000000000 << 3) and not (pieces & 0x1 << 60):
        yield 60
    if pieces & (0x705 << 4) and not (pieces & 0x1 << 5):
        yield 5
    if pieces & (0x507000000000000 << 4) and not (pieces & 0x1 << 61):
        yield 61
    if pieces & (0x705 << 5) and not (pieces & 0x1 << 6):
        yield 6
    if pieces & (0x507000000000000 << 5) and not (pieces & 0x1 << 62):
        yield 62
    if pieces & 0x302 and not (pieces & 0x1 << 0):
        yield 0
    if pieces & 0xc040 and not (pieces & 0x1 << 7):
        yield 7
    if pieces & 0x203000000000000 and not (pieces & 0x1 << 56):
        yield 56
    if pieces & 0x40c0000000000000 and not (pieces & 0x1 << 63):
        yield 63

#scores = {'a': 0, 'b': -1, 'c': -3, 'd': -3, 'e': 4,
#            'f': 5, 'g': 4, 'h': 3, 'i': -2, 'j': -1, 'k': -3, 'l': 4, 'm': 7, 'n': 6, 'o': 8, 'p': 9, 'q': 2}
#depths = {1: ['a'], 2: ['b', 'c', 'd', 'e'], 3: ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']}
#deepest = {'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q'}
#childrens = {'a': ['b', 'c', 'd', 'e'],
#            'b': ['f', 'g', 'h', 'i'],
#            'c': ['i', 'j', 'k'],
#            'd': ['k', 'l', 'm'],
#            'e': ['m', 'n', 'o', 'p', 'q']}
#
# remember scores to not recalculate
#
# Thread:
#   do go into most likely paths and calculate scores
#   if move is made, remove useless info and keep digging
# move:
#   just run alphabeta and use the scores calculated to make us faster


scores = {}
depths = {}
childrens = {}


def score_delta(my_bin, other_bin, move, me):
    h, w = 8, 8
    pre_score = 0
    post_score = 0

    y = move // 8
    x = move % 8


    for dx, dy in ((0, 1), (1, 0), (1, 1), (1, -1)):
        mf, mb, of, ob = 0, 0, 0, 0
        mfo, mbo, ofo, obo = True, True, True, True
        # my forwards
        i = 1
        while (-1 < y + i*dy < h and -1 < x + i*dx < w) and \
                my_bin & 0x1 << (x + i*dx + (y + i*dy) * 8):
            i += 1
        mf = i-1
        if not (-1 < y + i*dy < h and -1 < x + i*dx < w) or \
                other_bin & 0x1 << (x + i*dx + (y + i*dy) * 8):
            mfo = False

        # my backwards
        i = 1
        while (-1 < y - i * dy < h and -1 < x - i * dx < w) and \
                my_bin & 0x1 << (x - i*dx + (y - i*dy) * 8):
            i += 1
        mb = i-1
        if not (-1 < y - i * dy < h and -1 < x - i * dx < w) or \
                other_bin & 0x1 << (x - i*dx + (y - i*dy) * 8):
            mbo = False

        # other forwards
        i = 1
        while (-1 < y + i * dy < h and -1 < x + i * dx < w) and \
                my_bin & 0x1 << (x + i*dx + (y + i*dy) * 8):
            i += 1
        of = i - 1
        if not (-1 < y + i * dy < h and -1 < x + i * dx < w) or \
                other_bin & 0x1 << (x + i*dx + (y + i*dy) * 8):
            ofo = False

        # other backwards
        i = 1
        while (-1 < y - i * dy < h and -1 < x - i * dx < w) and \
                other_bin & 0x1 << (x - i*dx + (y - i*dy) * 8):
            i += 1
        ob = i - 1
        if not (-1 < y - i * dy < h and -1 < x - i * dx < w) or \
                my_bin & 0x1 << (x - i*dx + (y - i*dy) * 8):
            obo = False
        # score per row is squared, times 10 if open 2 3 9 -10 -1
        pre_score += (mf*mf*mf*(10 if mfo else 1) if mf > 1 else 0) + \
                     (mb*mb*mb*(10 if mbo else 1) if mb > 1 else 0) - \
                     (of*of*of*(10 if ofo else 1)) - \
                     (ob*ob*ob*(10 if obo else 1))

        post_score += ((0 if not mfo and not mbo else ((mf + mb + 1)**3 * (1 if mfo or mbo else 10))) if mf+mb > 0 else 0) - \
                      (of*of*of*(1 if ofo else 0) if of > 1 else 0) - (ob*ob*ob*(1 if obo else 0) if ob > 1 else 0)

        if(mf + mb + 1) == 5:
            return WIN_SCORE  # WE WIN

    return (post_score-pre_score) * (1 if me else -1)


def calc_score(i, position, prev_score, me):  # me is true if this is my move
    #if position in scores:
    #    return scores[position]
    score = score_delta(position, i, me)
    if score != WIN_SCORE and score != -WIN_SCORE:
        score += prev_score
    scores[position] = score
    return score


def deepen_pos(position, me, depth):
    my_bin = position >> 64
    other_bin = position & 0xFFFFFFFFFFFFFFFF

    k = 64 if me else 0

    children = childrens.get(position, set())
    all_bin = my_bin | other_bin
    for i in range(64):
        move = 0x1 << i + k
        if not (position & move):
            n_pos = position | 0x1 << i + k
            deepest.add(n_pos)
            children.add(n_pos)
            sd = score_delta(position, move, me)
            if sd == WIN_SCORE or sd == -WIN_SCORE:
                scores[n_pos] = sd
            else:
                scores[n_pos] = scores[position] + sd
    childrens[position] = children
    deepest.remove(position)


def fast_alphabeta(position, depth, alpha, beta, me):  # me is True if maxing (i is the opponent's move and I am looking for potential me moves)
    if depth == 0 or position not in childrens:
        return scores[position]

    if me:
        best = -WIN_SCORE
        for n_pos in childrens[position]:
            val = alphabeta(n_pos, depth-1, alpha, beta, False)
            best = val if val > best else best
            alpha = best if best > alpha else alpha
            if alpha >= beta:
                return best
        return best
    else:
        best = WIN_SCORE
        for n_pos in childrens[position]:
            val = alphabeta(n_pos, depth - 1, alpha, beta, True)
            best = val if val < best else best
            beta = best if best < beta else beta
            if beta <= alpha:
                return best
        return best


def evaluate(position, me, depth):
    if position not in childrens or depth == 0:
        return scores[position]
    if me:

        return max(evaluate(pos, False, depth-1) for pos in childrens[position])
    else:
        return min(evaluate(pos, True, depth-1) for pos in childrens[position])


def alphabeta(i, my_bin, other_bin, prev_score, depth, alpha, beta, me):  # me is True if maxing (i is the opponent's move and I am looking for potential me moves)
    global n_scores
    score = calc_score(i, (my_bin << 64) | other_bin, prev_score, not me)  # not me since i is the prev move

    if depth == 0 or score == WIN_SCORE or score == -WIN_SCORE:
        n_scores += 1
        return score

    if me:
        new_other_bin = other_bin | (0x1 << i)
        best = -WIN_SCORE
        for n in likely_moves(my_bin | new_other_bin):
            val = alphabeta(n, my_bin, new_other_bin, score, depth-1, alpha, beta, False)
            best = val if val > best else best
            alpha = best if best > alpha else alpha
            if alpha >= beta:
                return best
        return best
    else:
        new_my_bin = my_bin | (0x1 << i)
        best = WIN_SCORE
        for n in likely_moves(new_my_bin | other_bin):
            val = alphabeta(n, new_my_bin, other_bin, score, depth - 1, alpha, beta, True)
            best = val if val < best else best
            beta = best if best < beta else beta
            if beta <= alpha:
                return best
        return best

n_scores = 0
def alphabeta_move(my_bin, other_bin, start_score, depth):
    global n_scores
    n_scores = 0
    start = timer()
    best = -WIN_SCORE
    alpha = -WIN_SCORE
    beta = WIN_SCORE
    move = 0
    for n in likely_moves(my_bin | other_bin):
        score = alphabeta(n, my_bin, other_bin, start_score, depth, alpha, beta, False)
        if(score > best):
            move = n
            best = score
        alpha = best if best > alpha else alpha
        if alpha >= beta:
            break
    print("d_bin_alphabeta\td:", depth, "\tt:", n_scores, timer() - start, (timer() - start) / n_scores)
    move_y, move_x = move // 8, move % 8
    return move_y, move_x


def dynamic_move(board, col):
    my_bin = 0x0000000000000000
    other_bin = 0x0000000000000000

    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == col:
                my_bin |= 0x01 << x + y * 8
            elif board[y][x] != " ":
                other_bin |= 0x01 << x + y * 8

    for pos in deepest:
        deepen_pos(pos, me)

    best = -WIN_SCORE
    move = 0
    pos = (my_bin << 64) | other_bin
    for i in fast_get_rel(my_bin, other_bin):
        val = evaluate(pos | (0x1 << (64+1)), True)
        if val > best:
            move = i
            best = val
    move_y = move // 8
    move_x = move % 8

    return move_y, move_x


def gen_potential_moves_f():
    for y in range(6):
        for x in range(6):
            print("if pieces & 0x70507 << {} and not (pieces & 0x1 << {}):\n\tyield {}".format(x + y * 8, x+1 + (y+1)*8, x+1 + (y+1)*8))
    for y in range(6):
        print("if pieces & (0x30203 << {}) and not (pieces & 0x1 << {}):\n\tyield {}".format(y*8, 0 + (y+1)*8, 0 + (y+1)*8))
        print("if pieces & (0xc040c0 << {}) and not (pieces & 0x1 << {}):\n\tyield {}".format(y*8, 7 + (y+1)*8, 7 + (y+1)*8))
    for x in range(6):
        print("if pieces & (0x705 << {}) and not (pieces & 0x1 << {}):\n\tyield {}".format(x, x+1, x+1))
        print("if pieces & (0x507000000000000 << {}) and not (pieces & 0x1 << {}):\n\tyield {}".format(x, x + 1 + 7*8, x + 1 + 7*8))
    print("if pieces & 0x302 and not (pieces & 0x1 << 0):\n\tyield 0")
    print("if pieces & 0xc040 and not (pieces & 0x1 << 7):\n\tyield 7")
    print("if pieces & 0x203000000000000 and not (pieces & 0x1 << 56):\n\tyield 56")
    print("if pieces & 0x40c0000000000000 and not (pieces & 0x1 << 63):\n\tyield 63")


def move(board, col):
    my_bin = 0x0000000000000000
    other_bin = 0x0000000000000000

    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == col:
                my_bin |= 0x01 << x + y * 8
            elif board[y][x] != " ":
                other_bin |= 0x01 << x + y * 8

    #import cProfile
    #cProfile.runctx('move_y, move_x = alphabeta_move(my_bin, other_bin, 0, 4)', globals(), locals())
    move_y, move_x = alphabeta_move(my_bin, other_bin, 0, 4)
    import ai
    #cProfile.runctx('print(move_y, move_x, "vs", ai.move(board, col))', globals(), locals())
    print(move_y, move_x, "vs", ai.move(board, col))

    if(board[move_y][move_x] != ' '):
        for y in range(8):
            for x in range(8):
                if board[y][x] == ' ':
                    print("I LOST")
                    return y, x

    return move_y, move_x

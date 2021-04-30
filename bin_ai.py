from timeit import default_timer as timer
WIN_SCORE = 1000000000000000000000


def score_delta(y, x, my_bin, other_bin):
    h, w = 8, 8
    pre_score = 0
    post_score = 0

    h, w = 8, 8
    pre_score = 0
    post_score = 0

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

    return post_score-pre_score

    #
    # 0x1       just one
    #
    # 0x3       2 in a row
    # 0x7       3 in a row
    # 0xf       4 in a row
    # 0x1f      5 in a row
    #
    # 0x101         2 vertical
    # 0x10101       3 vertical
    # 0x1010101     4 vertical
    # 0x101010101   5 vertical
    #
    # 0x201         2 down - right
    # 0x40201       3 down - right
    # 0x8040201     4 down - right
    # 0x1008040201  5 down - right
    #
    # 0x102         2 down - left
    # 0x10204       3 down - left
    # 0x1020408     4 down - left
    # 0x102040810   5 down - left
    #
    # hori = {5: 0x1f, 4: 0xf, 3: 0x7, 2: 0x3, 1: 0x1}
    # vert = {5: 0x1010101, 4: 0x1010101, 3: 0x10101, 2: 0x101, 1: 0x1}
    # drdiag = {5: 0x1008040201, 4: 0x8040201, 3: 0x40201, 2: 0x201, 1: 0x1}
    # dldiag = {5: 0x102040810, 4: 0x1020408, 3: 0x10204, 2: 0x102, 1: 0x1}


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


# 0x70507   donut
# 0x30203   open left
# 0x705     open up
# 0x507000000000000 open down
# 0xc040c0  open right
def fast_get_rel(my_bin, other_bin):
    all_bin = my_bin | other_bin
    l = set()
    for y in range(6):
        for x in range(6):
            if all_bin & 0x70507 << x + y * 8:
                l.add(x+1 + (y+1)*8)
    for y in range(6):
        if all_bin & (0x30203 << y*8):
            l.add(0 + (y+1)*8)
        if all_bin & (0xc040c0 << y*8):
            l.add(7 + (y+1)*8)
    for x in range(6):
        if all_bin & (0x705 << x):
            l.add(x+1)
        if all_bin & (0x507000000000000 << x):
            l.add(x + 1 + 7*8)
    if all_bin & 0x302:  # top left
        l.add(0)
    if all_bin & 0xc040:  # top right
        l.add(7)
    if all_bin & 0x203000000000000:  # bottom left
        l.add(7*8)
    if all_bin & 0x40c0000000000000:  # bottom right
        l.add(7*9)
    return l


def rel_alphabeta(y, x, my_bin, other_bin, prev_score, depth, alpha, beta, me):
    delta = 0
    score = prev_score
    if me:
        delta = score_delta(y, x, other_bin, my_bin)
        score = (0 if delta == WIN_SCORE else prev_score) - delta
    else:
        delta = score_delta(y, x, my_bin, other_bin)
        score = (0 if delta == WIN_SCORE else prev_score) + delta

    if depth == 0 or score == WIN_SCORE or score == -WIN_SCORE:
        return score

    if me:
        new_other_bin = other_bin | (0x1 << x + y * 8)
        best = -WIN_SCORE
        for n in fast_get_rel(my_bin, new_other_bin):
            if not (my_bin & 0x1 << n or new_other_bin & 0x1 << n):
                ny = n // 8
                nx = n % 8
                cur = rel_alphabeta(ny, nx, my_bin, new_other_bin, score, depth-1, alpha, beta, False)
                best = cur if cur > best else best
                alpha = best if best > alpha else alpha
                if alpha >= beta:
                    return best
        return best
    else:
        new_my_bin = my_bin | (0x1 << x + y * 8)
        best = WIN_SCORE
        for n in fast_get_rel(new_my_bin, other_bin):
            if not (new_my_bin & 0x1 << n or other_bin & 0x1 << n):
                ny = n // 8
                nx = n % 8
                cur = rel_alphabeta(ny, nx, new_my_bin, other_bin, score, depth - 1, alpha, beta, True)
                best = cur if cur < best else best
                beta = best if best < beta else beta
                if beta <= alpha:
                    return best
        return best


def bin_rel_alphabeta_move(my_bin, other_bin):
    move_x, move_y = 4, 4
    start = timer()
    best = -WIN_SCORE
    alpha = -WIN_SCORE
    beta = WIN_SCORE
    for n in fast_get_rel(my_bin, other_bin):
        if not(my_bin & 0x1 << n or other_bin & 0x1 << n):
            y = n // 8
            x = n % 8
            sd = rel_alphabeta(y, x, my_bin, other_bin, 0, 4, alpha, beta, False)
            #print(sd, y, x)
            if(sd > best):
                move_x, move_y = x, y
                best = sd
            alpha = best if best > alpha else alpha
            if alpha >= beta:
                break
    print(timer() - start)
    return move_y, move_x


def move(board, col):
    my_bin = 0x0000000000000000
    other_bin = 0x0000000000000000

    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == col:
                my_bin |= 0x01 << x + y * 8
            elif board[y][x] != " ":
                other_bin |= 0x01 << x + y * 8
    print(hex(my_bin), hex(other_bin))
    deepen((my_bin << 64) | other_bin, True)

    import cProfile
    cProfile.runctx('bin_rel_alphabeta_move(my_bin, other_bin)', globals(), locals())
    move_y, move_x = bin_rel_alphabeta_move(my_bin, other_bin)

    if(board[move_y][move_x] != ' '):
        for y in range(8):
            for x in range(8):
                if board[y][x] == ' ':
                    print("I LOST")
                    return y, x

    return move_y, move_x


def action(y, x):
    print("\tpass {} {}".format(y, x))


if __name__ == '__main__':
    #print(evaluate('a', True))
    board = make_empty_board(8)
    board[6][7] = 'w'
    board[6][6] = 'w'
    board[7][6] = 'w'
    move(board, 'w')

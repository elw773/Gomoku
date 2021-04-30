from timeit import default_timer as timer
WIN_SCORE = 1000000000000000000000


def score_delta(y, x, my_map, other_map):
    h, w = 8, 8
    pre_score = 0
    post_score = 0

    for dx, dy in ((0, 1), (1, 0), (1, 1), (1, -1)):
        mf, mb, of, ob = 0, 0, 0, 0
        mfo, mbo, ofo, obo = True, True, True, True
        # my forwards
        i = 1
        while (-1 < y + i*dy < h and -1 < x + i*dx < w) and \
                my_map[y + i*dy][x + i*dx]:
            i += 1
        mf = i-1
        if not (-1 < y + i*dy < h and -1 < x + i*dx < w) or \
                other_map[y + i*dy][x + i*dx]:
            mfo = False

        # my backwards
        i = 1
        while (-1 < y - i * dy < h and -1 < x - i * dx < w) and \
                my_map[y - i * dy][x - i * dx]:
            i += 1
        mb = i-1
        if not (-1 < y - i * dy < h and -1 < x - i * dx < w) or \
                other_map[y - i * dy][x - i * dx]:
            mbo = False

        # other forwards
        i = 1
        while (-1 < y + i * dy < h and -1 < x + i * dx < w) and \
                other_map[y + i * dy][x + i * dx]:
            i += 1
        of = i - 1
        if not (-1 < y + i * dy < h and -1 < x + i * dx < w) or \
                my_map[y + i * dy][x + i * dx]:
            ofo = False

        # other backwards
        i = 1
        while (-1 < y - i * dy < h and -1 < x - i * dx < w) and \
                other_map[y - i * dy][x - i * dx]:
            i += 1
        ob = i - 1
        if not (-1 < y - i * dy < h and -1 < x - i * dx < w) or \
                my_map[y - i * dy][x - i * dx]:
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

    #print(y, x, post_score-pre_score, pre_score, post_score)

    return post_score-pre_score


def minimax(y, x, my_map, other_map, prev_score, depth, me):
    delta = 0
    score = prev_score
    if me:
        delta = score_delta(y, x, other_map, my_map)
        score = (0 if delta == WIN_SCORE else prev_score) - delta
    else:
        delta = score_delta(y, x, my_map, other_map)
        score = (0 if delta == WIN_SCORE else prev_score) + delta

    if depth == 0 or score == WIN_SCORE or score == -WIN_SCORE:
        return score

    if me:
        other_map[y][x] = 1
        best = -WIN_SCORE
        for ny in range(len(my_map)):
            for nx in range(len(my_map[ny])):
                if not my_map[ny][nx] and not other_map[ny][nx]:
                    best = max(best, minimax(ny, nx, my_map, other_map, score, depth-1, False))
        other_map[y][x] = 0
        return best
    else:
        my_map[y][x] = 1
        best = WIN_SCORE
        for ny in range(len(my_map)):
            for nx in range(len(my_map[ny])):
                if not my_map[ny][nx] and not other_map[ny][nx]:
                    best = min(best, minimax(ny, nx, my_map, other_map, score, depth-1, True))
        my_map[y][x] = 0
        return best


def relevant_minimax(y, x, my_map, other_map, prev_score, depth, me):
    delta = 0
    score = prev_score
    if me:
        delta = score_delta(y, x, other_map, my_map)
        score = (0 if delta == WIN_SCORE else prev_score) - delta
    else:
        delta = score_delta(y, x, my_map, other_map)
        score = (0 if delta == WIN_SCORE else prev_score) + delta

    if depth == 0 or score == WIN_SCORE or score == -WIN_SCORE:
        return score

    if me:
        other_map[y][x] = 1
        best = -WIN_SCORE
        for ny in range(len(my_map)):
            for nx in range(len(my_map[ny])):
                if not my_map[ny][nx] and not other_map[ny][nx] and any(my_map[ny+dy][nx+dx] or other_map[ny+dy][nx+dx] for dy, dx in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)) if 0 <= ny+dy < 8 and 0 <= nx+dx < 8):
                    best = max(best, relevant_minimax(ny, nx, my_map, other_map, score, depth-1, False))
        other_map[y][x] = 0
        return best
    else:
        my_map[y][x] = 1
        best = WIN_SCORE
        for ny in range(len(my_map)):
            for nx in range(len(my_map[ny])):
                if not my_map[ny][nx] and not other_map[ny][nx] and any(my_map[ny+dy][nx+dx] or other_map[ny+dy][nx+dx] for dy, dx in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)) if 0 <= ny+dy < 8 and 0 <= nx+dx < 8):
                    best = min(best, relevant_minimax(ny, nx, my_map, other_map, score, depth-1, True))
        my_map[y][x] = 0
        return best


def alphabeta(y, x, my_map, other_map, prev_score, depth, alpha, beta, me):
    delta = 0
    score = prev_score
    if me:
        delta = score_delta(y, x, other_map, my_map)
        score = (0 if delta == WIN_SCORE else prev_score) - delta
    else:
        delta = score_delta(y, x, my_map, other_map)
        score = (0 if delta == WIN_SCORE else prev_score) + delta

    if depth == 0 or score == WIN_SCORE or score == -WIN_SCORE:
        return score

    if me:
        other_map[y][x] = 1
        best = -WIN_SCORE
        for ny in range(len(my_map)):
            for nx in range(len(my_map[ny])):
                if not my_map[ny][nx] and not other_map[ny][nx]:
                    best = max(best, alphabeta(ny, nx, my_map, other_map, score, depth-1, alpha, beta, False))
                    alpha = max(alpha, best)
                    if alpha >= beta:
                        other_map[y][x] = 0
                        return best
        other_map[y][x] = 0
        return best
    else:
        my_map[y][x] = 1
        best = WIN_SCORE
        for ny in range(len(my_map)):
            for nx in range(len(my_map[ny])):
                if not my_map[ny][nx] and not other_map[ny][nx]:
                    best = min(best, alphabeta(ny, nx, my_map, other_map, score, depth-1, alpha, beta, True))
                    beta = min(beta, best)
                    if beta <= alpha:
                        my_map[y][x] = 0
                        return best
        my_map[y][x] = 0
        return best


def get_rel(my_map, other_map):
    l = []
    for y in range(8):
        for x in range(8):
            if is_rel(y, x, my_map, other_map):
                l.append((y, x))
    return l

def is_rel(y, x, my_map, other_map):
    return not my_map[y][x] and not other_map[y][x] and \
        any(my_map[y+dy][x+dx] or other_map[y+dy][x+dx] for dy, dx in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)) if 0 <= y+dy < 8 and 0 <= x+dx < 8)

def is_valid_move(y, x, my_map, other_map):
    return (-1 < y < 8) and (-1 < x < 8) and not my_map[y][x] and not other_map[y][x]

def is_valid_movel(y, x, my_map, other_map):
    return (-1 < y < 8) and (-1 < x < 8) and not my_map[x+y*8] and not other_map[x+y*8]

def fast_get_rel(my_map, other_map):
    l = set()
    for y in range(8):
        for x in range(8):
            if my_map[y][x] or other_map[y][x]:
                if is_valid_move(y+1, x+1, my_map, other_map): l.add((y+1, x+1))
                if is_valid_move(y+1, x, my_map, other_map): l.add((y+1, x))
                if is_valid_move(y+1, x-1, my_map, other_map): l.add((y+1, x-1))
                if is_valid_move(y, x+1, my_map, other_map): l.add((y, x+1))
                if is_valid_move(y, x-1, my_map, other_map): l.add((y, x-1))
                if is_valid_move(y-1, x+1, my_map, other_map): l.add((y-1, x+1))
                if is_valid_move(y-1, x, my_map, other_map): l.add((y-1, x))
                if is_valid_move(y-1, x-1, my_map, other_map): l.add((y-1, x-1))
    return l


def fast_is_rel(y, x, my_map, other_map):
    return not my_map[y][x] and not other_map[y][x] and (
        my_map[y+1][x+1] or other_map[y+1][x+1] or
        my_map[y+1][x+0] or other_map[y+1][x+0] or
        my_map[y+1][x-1] or other_map[y+1][x-1] or
        my_map[y][x+1] or other_map[y][x+1] or
        my_map[y][x-1] or other_map[y][x-1] or
        my_map[y-1][x+1] or other_map[y-1][x+1] or
        my_map[y-1][x+0] or other_map[y-1][x+0] or
        my_map[y-1][x-1] or other_map[y-1][x-1]
        )

scores = 0
wins = 0
def rel_alphabeta(y, x, my_map, other_map, prev_score, depth, alpha, beta, me):
    global scores, wins
    delta = 0
    score = prev_score
    if me:
        delta = score_delta(y, x, other_map, my_map)
        score = (0 if delta == WIN_SCORE else prev_score) - delta
    else:
        delta = score_delta(y, x, my_map, other_map)
        score = (0 if delta == WIN_SCORE else prev_score) + delta

    wins += 1
    if depth == 0 or score == WIN_SCORE or score == -WIN_SCORE:
        scores += 1
        return score

    if me:
        other_map[y][x] = 1
        best = -WIN_SCORE
        for ny, nx in fast_get_rel(my_map, other_map):
            cur = rel_alphabeta(ny, nx, my_map, other_map, score, depth-1, alpha, beta, False)
            best = cur if cur > best else best
            alpha = best if best > alpha else alpha
            if alpha >= beta:
                other_map[y][x] = 0
                return best
        other_map[y][x] = 0
        return best
    else:
        my_map[y][x] = 1
        best = WIN_SCORE
        for ny, nx in fast_get_rel(my_map, other_map):
            cur = rel_alphabeta(ny, nx, my_map, other_map, score, depth - 1, alpha, beta, True)
            best = cur if cur < best else best
            beta = best if best < beta else beta
            if beta <= alpha:
                my_map[y][x] = 0
                return best
        my_map[y][x] = 0
        return best


def fast_rel_alphabeta(y, x, my_map, other_map, prev_score, depth, alpha, beta, me):
    delta = 0
    score = prev_score
    if me:
        delta = score_delta(y, x, other_map, my_map)
        score = (0 if delta == WIN_SCORE else prev_score) - delta
    else:
        delta = score_delta(y, x, my_map, other_map)
        score = (0 if delta == WIN_SCORE else prev_score) + delta

    if depth == 0 or score == WIN_SCORE or score == -WIN_SCORE:
        return score

    if me:
        other_map[y][x] = 1
        best = -WIN_SCORE
        for ny, nx in fast_get_rel(my_map, other_map):
            cur = fast_rel_alphabeta(ny, nx, my_map, other_map, score, depth-1, alpha, beta, False)
            best = cur if cur > best else best
            alpha = best if best > alpha else alpha
            if alpha >= beta:
                other_map[y][x] = 0
                return best
        other_map[y][x] = 0
        return best
    else:
        my_map[y][x] = 1
        best = WIN_SCORE
        for ny, nx in fast_get_rel(my_map, other_map):
            cur = fast_rel_alphabeta(ny, nx, my_map, other_map, score, depth - 1, alpha, beta, True)
            best = cur if cur < best else best
            beta = best if best < beta else beta
            if beta <= alpha:
                my_map[y][x] = 0
                return best
        my_map[y][x] = 0
        return best


def minimax_move(my_map, other_map):
    start = timer()
    move_x, move_y = 4, 4
    best = -WIN_SCORE
    for y in range(len(my_map)):
        for x in range(len(my_map[y])):
            if not my_map[y][x] and not other_map[y][x]:
                sd = minimax(y, x, my_map, other_map, 0, 2, False)
                if(sd > best):
                    move_x, move_y = x, y
                    best = sd

    print(timer() - start)
    return move_y, move_x


def rel_minimax_move(my_map, other_map):
    start = timer()
    move_x, move_y = 4, 4
    best = -WIN_SCORE
    for y in range(len(my_map)):
        for x in range(len(my_map[y])):
            if not my_map[y][x] and not other_map[y][x] and any(my_map[y+dy][x+dx] or other_map[y+dy][x+dx] for dy, dx in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)) if 0 <= y+dy < 8 and 0 <= x+dx < 8):
                sd = relevant_minimax(y, x, my_map, other_map, 0, 2, False)
                if(sd > best):
                    move_x, move_y = x, y
                    best = sd
    print(timer() - start)
    return move_y, move_x


def alphabeta_move(my_map, other_map):
    move_x, move_y = 4, 4
    start = timer()
    best = -WIN_SCORE
    alpha = -WIN_SCORE
    beta = WIN_SCORE
    for y in range(len(my_map)):
        for x in range(len(my_map[y])):
            if not my_map[y][x] and not other_map[y][x]:
                sd = alphabeta(y, x, my_map, other_map, 0, 2, alpha, beta, False)
                if(sd > best):
                    move_x, move_y = x, y
                    best = sd
                alpha = max(alpha, best)
                if alpha >= beta:
                    break
    print(timer() - start)
    return move_y, move_x


def rel_alphabeta_move(my_map, other_map):
    global scores
    scores = 0
    move_x, move_y = 4, 4
    start = timer()
    best = -WIN_SCORE
    alpha = -WIN_SCORE
    beta = WIN_SCORE
    for y, x in fast_get_rel(my_map, other_map):
        sd = rel_alphabeta(y, x, my_map, other_map, 0, 3, alpha, beta, False)
        #print("ai", y, x, sd)
        if(sd > best):
            move_x, move_y = x, y
            best = sd
        alpha = best if best > alpha else alpha
        if alpha >= beta:
            break
    #print("ai", scores, timer() - start, (timer() - start) / scores)
    return move_y, move_x


def fast_rel_alphabeta_move(my_map, other_map):
    move_x, move_y = 4, 4
    start = timer()
    best = -WIN_SCORE
    alpha = -WIN_SCORE
    beta = WIN_SCORE
    moves = fast_get_rel(my_map, other_map)
    for y, x in moves:
        sd = fast_rel_alphabeta(y, x, my_map, other_map, 0, 2, alpha, beta, False)
        if(sd > best):
            move_x, move_y = x, y
            best = sd
        alpha = best if best > alpha else alpha
        if alpha >= beta:
            break
    print(timer() - start)
    return move_y, move_x


def other_move(board, col):
    my_map = []
    other_map = []

    for y in range(len(board)):
        my_map.append([0] * len(board[y]))
        other_map.append([0] * len(board[y]))
        for x in range(len(board[y])):
            if board[y][x] == col:
                my_map[y][x] = 1
            elif board[y][x] != " ":
                other_map[y][x] = 1

    move_y, move_x = alphabeta_move(my_map, other_map)

    if(board[move_y][move_x] != ' '):
        for y in range(len(my_map)):
            for x in range(len(my_map[y])):
                if not my_map[y][x] and not other_map[y][x]:
                    print("I LOST")
                    return y, x

    return move_y, move_x

def to_bin(y, x):
    return 0x1 << x + y * 8

i = 0
def move(board, col, **kwargs):
    global i, scores, wins
    i+=1
    # parse board into two bitmaps for my and opponent colour
    my_map = []
    other_map = []
    my_mapl = [0] * 8 * 8
    other_mapl = [0] * 8 * 8

    my_bin = 0x0000000000000000
    other_bin = 0x0000000000000000

    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == col:
                my_bin |= 0x1 << x + y * 8
            elif board[y][x] != " ":
                other_bin |= 0x1 << x + y * 8

    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == col:
                my_mapl[x + y*8] = 1
            elif board[y][x] != " ":
                other_mapl[x + y*8] = 1

    for y in range(len(board)):
        my_map.append([0] * len(board[y]))
        other_map.append([0] * len(board[y]))
        for x in range(len(board[y])):
            if board[y][x] == col:
                my_map[y][x] = 1
            elif board[y][x] != " ":
                other_map[y][x] = 1

    #print(rel_alphabeta_move(my_map, other_map))
    scores, wins = 0, 0
    #import cProfile
    #cProfile.runctx('rel_alphabeta_move(my_map, other_map)', globals(), locals())
    #print("scores", scores, "wins", wins)
    #import cProfile
    #cProfile.runctx('fast_rel_alphabeta_move(my_map, other_map)', globals(), locals())

    move_y, move_x = rel_alphabeta_move(my_map, other_map)
    print("e", wins / (scores+1), "scores", scores, "wins", wins)


    if(board[move_y][move_x] != ' '):
        for y in range(len(my_map)):
            for x in range(len(my_map[y])):
                if not my_map[y][x] and not other_map[y][x]:
                    print("I LOST")
                    return y, x

    return move_y, move_x

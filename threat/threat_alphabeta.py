from timeit import default_timer as timer
import bitboard
from precomputed_rows import wins as win_prows
from precomputed_rows import forces as force_prows
from precomputed_rows import scores as prow_scores

m_scores = {}
o_scores = {}
childrens = {}  # sorted moves for a position
minimax_scores = {}

WINNING_SCORE = 5000
WIN_SCORE = 500
move_start_time = 0
my_turn = 0


def score(m_bb, o_bb):
    score = 0
    m_rotations = bitboard.get_rotations(m_bb)
    o_rotations = bitboard.get_rotations(o_bb)
    # 0
    for r in range(8):
        prow = bitboard.get_prow(m_bb, o_bb, r, True)
        if prow in prow_scores[8]:
            score += prow_scores[8][prow]
    # 90
    for r in range(8):
        prow = bitboard.get_prow(m_rotations[90], o_rotations[90], r, True)
        if prow in prow_scores[8]:
            score += prow_scores[8][prow]
    # 45
    for r in range(6):
        prow = bitboard.get_prow(m_rotations[45], o_rotations[45], r, False)
        if prow in prow_scores[bitboard.row_lengths[r]]:
            score += prow_scores[bitboard.row_lengths[r]][prow]
    # 135
    for r in range(6):
        prow = bitboard.get_prow(m_rotations[135], o_rotations[135], r, False)
        if prow in prow_scores[bitboard.row_lengths[r]]:
            score += prow_scores[bitboard.row_lengths[r]][prow]

    return score


def get_score(pos):
    if pos not in m_scores:
        m_bb, o_bb = bitboard.pos_to_bb(pos)
        m_scores[pos] = score(m_bb, o_bb)
        o_scores[pos] = score(o_bb, m_bb)
    return m_scores[pos] - o_scores[pos]


def score_i(m_bb, o_bb, i):
    score = 0
    r0 = bitboard.get_prow(m_bb, o_bb, bitboard.i_to_row(i, 0), True)
    r90 = bitboard.i_to_row(i, 90)
    r45 = bitboard.i_to_row(i, 45)
    r135 = bitboard.i_to_row(i, 135)
    m_rotations = bitboard.get_rotations(m_bb)
    o_rotations = bitboard.get_rotations(o_bb)
    # 0
    prow = bitboard.get_prow(m_bb, o_bb, r0, True)
    if prow in prow_scores[8]:
        score += prow_scores[8][prow]
    # 90
    prow = bitboard.get_prow(m_rotations[90], o_rotations[90], r90, True)
    if prow in prow_scores[8]:
        score += prow_scores[8][prow]
    # 45
    if r45 is not None:
        prow = bitboard.get_prow(m_rotations[45], o_rotations[45], r45, False)
        if prow in prow_scores[bitboard.row_lengths[r45]]:
            score += prow_scores[bitboard.row_lengths[r45]][prow]
    # 135
    if r135 is not None:
        prow = bitboard.get_prow(m_rotations[135], o_rotations[135], r135, False)
        if prow in prow_scores[bitboard.row_lengths[r135]]:
            score += prow_scores[bitboard.row_lengths[r135]][prow]
    return score


def score_move(pos, i, mtm):  # mtm true if i am moving
    new_m_score = m_scores[pos]
    new_o_score = o_scores[pos]
    m_bb = bitboard.pos_to_m_bb(pos)
    o_bb = bitboard.pos_to_o_bb(pos)

    new_m_score -= score_i(m_bb, o_bb, i)
    new_o_score -= score_i(o_bb, m_bb, i)

    if mtm:
        m_bb = bitboard.place_i(m_bb, i)
    else:
        o_bb = bitboard.place_i(o_bb, i)

    new_m_score += score_i(m_bb, o_bb, i)
    new_o_score += score_i(o_bb, m_bb, i)

    new_pos = bitboard.bb_to_pos(m_bb, o_bb)

    m_scores[new_pos] = new_m_score
    o_scores[new_pos] = new_o_score

    return new_m_score - new_o_score


def get_move_score(pos, i, mtm):
    new_pos = bitboard.pos_place_i(pos, i, mtm)
    if new_pos not in m_scores:
        get_score(pos)
        score_move(pos, i, mtm)
    return m_scores[new_pos] - o_scores[new_pos]


def make_forced_move(board):
    for y in range(8):
        for x in range(8):
            if board[y][x] == ' ':
                print("I LOST")
                return y, x


def get_cur_time():
    return timer() - move_start_time


def make_children(pos, mtm):
    children = []
    c_bb = bitboard.pos_to_c_bb(pos)
    for i in range(64):
        if not bitboard.get_i(c_bb, i):
            new_pos = bitboard.pos_place_i(pos, i, mtm)
            score = get_move_score(new_pos, i, mtm)
            if mtm and score > 5000:  # if this move will make me win
                return [new_pos]
            elif not mtm and score < -5000:
                return [new_pos]
            else:
                children.append(new_pos)
    children.sort(key=lambda c: get_score(c), reverse=mtm)
    return children


def get_children(pos, mtm, max_children):
    if pos not in childrens:
        childrens[pos] = make_children(pos, mtm)
    return childrens[pos][0:max_children]


def minimax(pos, depth, alpha, beta, me):
    if bitboard.is_tie(pos):
        return 0
    score = get_score(pos)
    if score > WIN_SCORE:
        return score
    elif score < -WIN_SCORE:
        return score
    elif depth == 0:
        return score

    if me:
        best = -WIN_SCORE
        children = get_children(pos, True, 9)
        for n_pos in children:
            val = minimax(n_pos, depth-1, alpha, beta, False)
            minimax_scores[n_pos] = val
            best = val if val > best else best
            alpha = best if best > alpha else alpha
            if alpha >= beta:
                # re sort childrens with minimax evaluation
                childrens[pos].sort(key=lambda c: get_score(c) if c not in minimax_scores else 100*minimax_scores[c], reverse=me)
                return best
        childrens[pos].sort(key=lambda c: get_score(c) if c not in minimax_scores else 100*minimax_scores[c], reverse=me)
        return best
    else:
        best = WIN_SCORE
        children = get_children(pos, False, 9)
        for n_pos in children:
            val = minimax(n_pos, depth-1, alpha, beta, False)
            minimax_scores[n_pos] = val
            best = val if val < best else best
            beta = best if best < beta else beta
            if alpha <= beta:
                # re sort childrens with minimax evaluation
                childrens[pos].sort(key=lambda c: get_score(c) if c not in minimax_scores else 100*minimax_scores[c], reverse=me)
                return best
        childrens[pos].sort(key=lambda c: get_score(c) if c not in minimax_scores else 100*minimax_scores[c], reverse=me)
        return best


def move(board, col):
    global move_start_time
    move_start_time = timer()

    head = bitboard.board_to_pos(board, col)
    m_bb, o_bb = bitboard.board_to_bbs(board, col)

    #threats = {}
    # analyze board for threats
    #m_rotations = bitboard.get_rotations(m_bb)
    #o_rotations = bitboard.get_rotations(o_bb)
    #for r in range(8):
    #    prow = bitboard.get_prow(m_bb, o_bb, r, True)
    #    if prow in win_prows:
    #        winning_i = bitboard.rowi_to_i(win_prows[prow], r, 0)
    #        return bitboard.i_to_yx(winning_i)

    alpha = -WIN_SCORE
    beta = WIN_SCORE
    depth = 4
    minimax(head, depth, alpha, beta, True)
    best_pos = get_children(head, True, 1)[0]

    move_bib = bitboard.pos_to_c_bb(head ^ best_pos)

    move_y, move_x = bitboard.move_to_yx(move_bib)

    if(board[move_y][move_x] != ' '):
        move_y, move_x = make_forced_move(board)
    print("threat:", timer() - move_start_time)

    return move_y, move_x


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


if __name__ == '__main__':
    print(len(bitboard.i135))
    board = []
    for i in range(8):
        board.append([" "]*8)
    board[0][0] = ' '
    board[1][1] = ' '
    board[2][2] = 'w'
    board[3][3] = 'w'
    board[4][4] = 'w'
    print_board(board)
    import cProfile
    cProfile.runctx("print(move(board, 'w'))", globals(), locals())

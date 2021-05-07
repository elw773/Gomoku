# stop going deep once time runs out so we can go deeper
# start doing minimax from each of the opponent moves after we are done
from timeit import default_timer as timer
import threading
import bitboard as bb

# mtm means me to move
WIN_SCORE = 50000
MAX_DEPTH = 16
START_DEPTH = 2

childrens = {}  # list of potential moves for a combined board, sorted in terms of bestness for the mover
scores = {}
mmx_scores = {}

move_time_limit = 2
move_stop_time = 0.1996
move_start_time = 0


def get_cur_time():
    return timer() - move_start_time


# calculate the minimax of a position, based on previously calculated postion scores
def quick_alphabeta(pos, depth, alpha, beta, me):
    if depth == 0 or pos not in childrens or scores[pos] > WIN_SCORE or scores[pos] < -WIN_SCORE or bb.is_tie(pos):
        return scores[pos]

    if me:
        best = -WIN_SCORE
        for n_pos in childrens[pos]:
            val = quick_alphabeta(n_pos, depth-1, alpha, beta, False)
            best = val if val > best else best
            alpha = best if best > alpha else alpha
            if alpha >= beta:
                return best
        return best
    else:
        best = WIN_SCORE
        for n_pos in childrens[pos]:
            val = quick_alphabeta(n_pos, depth - 1, alpha, beta, True)
            best = val if val < best else best
            beta = best if best < beta else beta
            if beta <= alpha:
                return best
        return best


def get_score(pos):
    if pos not in scores:
        m_bb = bb.pos_to_m_bb(pos)
        o_bb = bb.pos_to_o_bb(pos)
        scores[pos] = bb.score_bb(m_bb, o_bb) - bb.score_bb(o_bb, m_bb)
    return scores[pos]


def do_placement(pos, i, mtm, pos_score, m_bb, o_bb):
    n_pos = bb.pos_place_i(pos, i, mtm)
    if n_pos not in scores:
        n_m_bb = bb.pos_to_m_bb(n_pos)
        n_o_bb = bb.pos_to_o_bb(n_pos)
        pre_prow_score = bb.score_prow_i(m_bb, o_bb, i) - bb.score_prow_i(o_bb, m_bb, i)
        post_prow_score = bb.score_prow_i(n_m_bb, n_o_bb, i) - bb.score_prow_i(n_o_bb, n_m_bb, i)

        scores[n_pos] = pos_score - pre_prow_score + post_prow_score
    return n_pos


def get_children(pos, mtm):  # mtm true if i am moving
    if pos not in childrens:
        relevant = bb.get_relevant(pos)

        pos_score = get_score(pos)
        m_bb = bb.pos_to_m_bb(pos)
        o_bb = bb.pos_to_o_bb(pos)
        children = [do_placement(pos, i, mtm, pos_score, m_bb, o_bb) for i in range(64) if bb.get_i(relevant, i)]
        #for i in range(64):
        #    if bb.get_i(relevant, i):
        #        n_pos = bb.pos_place_i(pos, i, mtm)
        #        if n_pos not in scores:
        #            n_m_bb, n_o_bb = bb.pos_to_bb(n_pos)
        #            pre_prow_score = bb.score_prow_i(m_bb, o_bb, i) - bb.score_prow_i(o_bb, m_bb, i)
        #            post_prow_score = bb.score_prow_i(n_m_bb, n_o_bb, i) - bb.score_prow_i(n_o_bb, n_m_bb, i)

        #            scores[n_pos] = pos_score - pre_prow_score + post_prow_score
        #        children.append(n_pos)
        children.sort(key=lambda c: scores[c], reverse=mtm)
        childrens[pos] = children

    return childrens[pos]


# me is true if finding the best move for me
# me is false if finding the best move for other
def alphabeta(pos, depth, alpha, beta, me, stop_flag):
    if depth == 0 or stop_flag() or get_score(pos) > WIN_SCORE or get_score(pos) < -WIN_SCORE or bb.is_tie(pos):
        return get_score(pos)

    if me:
        best = -WIN_SCORE
        children = get_children(pos, True)[0:10]
        for n_pos in children:
            val = alphabeta(n_pos, depth-1, alpha, beta, False, stop_flag)
            mmx_scores[n_pos] = val
            if val > best:
                best = val
            if best > alpha:
                alpha = best
            if alpha >= beta:
                #childrens[pos].sort(key=lambda c: scores[c] if c not in mmx_scores else mmx_scores[c], reverse=me)
                return best
        #childrens[pos].sort(key=lambda c: scores[c] if c not in mmx_scores else mmx_scores[c], reverse=me)
        return best
    else:
        best = WIN_SCORE
        children = get_children(pos, False)[0:10]
        for n_pos in children:
            val = alphabeta(n_pos, depth - 1, alpha, beta, True, stop_flag)
            mmx_scores[n_pos] = val
            if val < best:
                best = val
            if best < beta:
                beta = best
            if beta <= alpha:
                #childrens[pos].sort(key=lambda c: scores[c] if c not in mmx_scores else mmx_scores[c], reverse=me)
                return best
        #childrens[pos].sort(key=lambda c: scores[c] if c not in mmx_scores else mmx_scores[c], reverse=me)
        return best


def make_forced_move(board):
    for y in range(8):
        for x in range(8):
            if board[y][x] == ' ':
                return y, x


offtime = True
offtime_pos = 0
offtime_depth = 0


def offtime_computing():
    global offtime_pos, offtime_depth
    while True:
        if offtime:
            children = get_children(offtime_pos, False)[0:10]
            for n_pos in children:
                alphabeta(n_pos, offtime_depth-1, -WIN_SCORE, WIN_SCORE, True, lambda: not offtime)
            offtime_depth += 1


offtime_thread = threading.Thread(target=offtime_computing, daemon=True)
offtime_thread.start()

def move(board, col, **kwargs):
    global s
    global first
    global move_start_time
    global exits
    global offtime
    global offtime_pos, offtime_depth
    offtime = False
    move_start_time = timer()

    head = bb.board_to_pos(board, col)

    depth = START_DEPTH
    children = get_children(head, True)[0:10]
    best_poses = {depth: children[0]}
    #print(get_cur_time())
    while get_cur_time() < move_stop_time and depth < MAX_DEPTH:
        best = -WIN_SCORE
        alpha = -WIN_SCORE
        beta = WIN_SCORE
        #alphabeta(head, depth, alpha, beta, True)
        for n_pos in children:
            val = alphabeta(n_pos, depth-1, alpha, beta, False, lambda: get_cur_time() > move_stop_time)
            mmx_scores[n_pos] = val
            if val > best:
                best = val
                best_poses[depth] = n_pos
            best = val if val > best else best
            alpha = best if best > alpha else alpha
            if alpha >= beta:
                break
        if get_cur_time() < move_stop_time and depth in best_poses:
            depth += 1

        childrens[head].sort(key=lambda c: scores[c] if c not in mmx_scores else mmx_scores[c], reverse=True)

    #alphabeta(head, depth, alpha, beta, True)

    #best_pos = max(childrens[head], key=lambda c: scores[c] if c not in mmx_scores else 100*mmx_scores[c])
    best_pos = best_poses[depth-1] if depth > START_DEPTH else best_poses[START_DEPTH]
    #best_pos = max(children, key=lambda c: scores[c])
    move_y, move_x = bb.move_to_yx(bb.find_move(head, best_pos))

    if(board[move_y][move_x] != ' '):
        move_y, move_x = make_forced_move(board)
    else:
        offtime = True
        offtime_pos = best_pos
        offtime_depth = depth
    if kwargs.get('time', False):
        print("pdab:", "d:", depth-1, "\tt:", get_cur_time(), len(scores), len(childrens))

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
    board = []
    for i in range(8):
        board.append([" "]*8)
    import random
    for i in range(10):
        board[random.randrange(0, 8)][random.randrange(0, 8)] = 'w'
        board[random.randrange(0, 8)][random.randrange(0, 8)] = 'b'
    board = bb.pos_to_board(0x2500860002000003000d201000860300)
    print_board(board)
    #m_bb, o_bb = bb.board_to_bbs(board, 'w')

    print(hex(bb.board_to_pos(board, 'w')))
    #bb.print_bb(bb.get_relevant(bb.board_to_pos(board, 'w')))
    #bb.print_bb(-0x303030303030304)
    #bb.score_bb(m_bb, o_bb)
    import cProfile
    #print(move(board, 'w'))
    cProfile.runctx("print(move(board, 'w'))", globals(), locals())

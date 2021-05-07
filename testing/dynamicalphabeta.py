from timeit import default_timer as timer
import math
import gomoku_bib as gbib
import random

# mtm means me to move
WIN_SCORE = gbib.WIN_SCORE


#terminal = {}  # a set to lookup if a position is a terminal node
#depth = {}  # the depth of each move, so we dont waste time
childrens = {}  # list of potential moves for a combined board, sorted in terms of bestness for the mover
scores = {}
mmx_scores = {}
#alpha = {}
#beta = {}

# calculate the minimax of a position, based on previously calculated postion scores
def quick_alphabeta(pos, depth, alpha, beta, me):
    if depth == 0 or pos not in childrens or scores[pos] == WIN_SCORE or scores[pos] == -WIN_SCORE or gbib.is_tie(pos):
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


def get_children(pos, mtm):  # mtm is true if the children will be the result of my move
    if pos in childrens:
        return childrens[pos]

    m_bib, o_bib = gbib.pos_to_bibs(pos)
    childrens[pos] = gbib.make_children(m_bib, o_bib, mtm, scores[pos], scores)
    return childrens[pos]


# me is true if finding the best move for me
# me is false if finding the best move for other
s = 0
def alphabeta(pos, depth, alpha, beta, me):
    global s
    #print(hex(pos), depth, alpha, beta, me, end = "\r")
    if depth == 0 or scores[pos] == WIN_SCORE or scores[pos] == -WIN_SCORE or gbib.is_tie(pos):
        s += 1
        return scores[pos]

    if me:
        best = -WIN_SCORE
        children = get_children(pos, True)[0:10]
        for n_pos in children:
            val = alphabeta(n_pos, depth-1, alpha, beta, False)
            mmx_scores[n_pos] = val
            best = val if val > best else best
            alpha = best if best > alpha else alpha
            if alpha >= beta:
                childrens[pos].sort(key=lambda c: scores[c] if c not in mmx_scores else 100*mmx_scores[c], reverse=me)
                return best
        childrens[pos].sort(key=lambda c: scores[c] if c not in mmx_scores else 100*mmx_scores[c], reverse=me)
        return best
    else:
        best = WIN_SCORE
        children = get_children(pos, False)[0:10]
        #print(scores[children[0]], "vs", scores[children[-1]])
        #if WIN_SCORE >= scores[children[0]] >= WIN_SCORE - 10000 or -WIN_SCORE <= scores[children[0]] <= -WIN_SCORE + 10000:
        #    gbib.print_board(gbib.pos_to_board(pos))
            #print("Score:", scores[pos])
            #for child in children:
            #    gbib.print_board(gbib.pos_to_board(pos))
            #    print("Score:", scores[pos])
        for n_pos in children:
            val = alphabeta(n_pos, depth - 1, alpha, beta, True)
            mmx_scores[n_pos] = val
            best = val if val < best else best
            beta = best if best < beta else beta
            if beta <= alpha:
                childrens[pos].sort(key=lambda c: scores[c] if c not in mmx_scores else 100*mmx_scores[c], reverse=me)
                return best
        childrens[pos].sort(key=lambda c: scores[c] if c not in mmx_scores else 100*mmx_scores[c], reverse=me)
        return best


def make_forced_move(board):
    for y in range(8):
        for x in range(8):
            if board[y][x] == ' ':
                print("I LOST")
                return y, x

first = True
def move(board, col):
    global s
    global first
    s = 0.0001
    start = timer()

    my_bib, other_bib = gbib.make_bitboards(board, col)

    head = gbib.bibs_to_pos(my_bib, other_bib)
    if first:
        scores[head] = 0
        first = False

    best = -WIN_SCORE
    alpha = -WIN_SCORE
    beta = WIN_SCORE
    depth = 4
    best_pos = head
    children = get_children(head, True)
    #l = len(children)
    #i = 0
    for n_pos in children:
        #print(i, "/", l, hex(n_pos), end = "\r")
        val = alphabeta(n_pos, depth-1, alpha, beta, False)
        if val > best:
            best = val
            best_pos = n_pos
        alpha = best if best > alpha else alpha
        if alpha >= beta:
            break
        #i += 1

    move_bib = gbib.pos_to_cbib(head ^ best_pos)

    move_y, move_x = gbib.move_bib_to_yx(move_bib)

    if(board[move_y][move_x] != ' '):
        move_y, move_x = make_forced_move(board)
    print("dab:", "s:", s, "\tt:", timer() - start, (timer() - start) / s, len(scores), len(childrens))

    return move_y, move_x


if __name__ == '__main__':
    board = gbib.make_empty_board(8)

    board[1][1] = 'w'
    board[2][2] = 'w'
    board[3][3] = 'w'
    board[4][4] = 'w'
    board[5][5] = 'b'
    gbib.print_board(board)
    m_bib, o_bib = gbib.make_bitboards(board, 'w')
    print(gbib.bibs_to_pos(m_bib, o_bib))
    head = gbib.bibs_to_pos(m_bib, o_bib)

    from timeit import default_timer as timer
    start = timer()
    move_y, move_x = move(board, 'w')
    print((timer()-start))
    print(move_y, move_x)
    for child in childrens[head]:
        m_bib, o_bib = gbib.pos_to_bibs(child)
        gbib.print_board(gbib.pos_to_board(child))
        print("Score:", scores[child])

from timeit import default_timer as timer
import math
import gomoku_bib as gbib
import random

# mtm means me to move

WIN_SCORE = 1000000000000000000000

head = 0
parentss = {}  # each pos points to its parents
potential_moves = {}  # list of potential moves as int for a combined board
visited_children = {}  # set for easy lookup
unvisited_children = {}  # list for better iteration
wins = {}  # each node has its wins
visits = {}  # each node stores its visits
scores = {}


def ubc(pos):
    return wins[pos]/visits[pos] + 2 * math.sqrt(math.log(visits[parentss[pos][0]]) / visits[pos])


def random_move(c_bib):
    if c_bib in potential_moves:
        p_moves = potential_moves[c_bib]
    else:
        p_moves = potential_moves[c_bib] = [m for m in gbib.likely_moves(c_bib)]
    n_p_moves = len(p_moves)
    return p_moves[int(random.random() * n_p_moves)]


def rollout(pos, mtm):  # return True for win or tie
    my_bib, other_bib = gbib.pos_to_bibs(pos)
    while not gbib.is_tie(my_bib | other_bib):
        #print_board(gbib.bib_to_board(my_bib, other_bib))
        if mtm:
            if gbib.is_win(other_bib):
                return False
            else:
                move = random_move(my_bib | other_bib)
                my_bib = my_bib | 0x1 << move
        else:
            if gbib.is_win(my_bib):
                return True
            else:
                move = random_move(my_bib | other_bib)
                other_bib = other_bib | 0x1 << move
        mtm = not mtm
    return False


def select(pos, mtm):
    while pos in visited_children and pos not in unvisited_children:  # if the pos already has children that are visited
        pos = max(visited_children[pos], key=lambda p: ubc(p))
        mtm = not mtm
    return pos, mtm


def score(pos, mtm):
    if pos in scores:
        return scores[pos]
    score = scores[pos] = gbib.score(pos, mtm)
    return score


def expand(pos, mtm):
    my_bib, other_bib = gbib.pos_to_bibs(pos)
    if gbib.is_tie(my_bib | other_bib) or gbib.is_win(my_bib) or gbib.is_win(other_bib):
        return pos, mtm
    else:
        if pos not in unvisited_children and pos not in visited_children:  # if i have not created children for this position
            if mtm:
                children = [pos | (0x1 << m + 64) for m in gbib.likely_moves(my_bib | other_bib)]
            else:
                children = [pos | (0x1 << m) for m in gbib.likely_moves(my_bib | other_bib)]
            unvisited_children[pos] = children
            for child in children:
                if child in parentss:
                    parentss[child].append(pos)
                else:
                    parentss[child] = [pos]
        else:
            children = unvisited_children[pos]
        return max(children, key=lambda c: score(c, mtm)), not mtm  # if we choose the best one to expand on, profit
        #return children[int(random.random() * len(children))], mtm


def add_to_visited(parent, pos):
    if parent not in visited_children:
        visited_children[parent] = set()
    visited_children[parent].add(pos)


def remove_from_unvisited(parent, pos):
    if parent in unvisited_children:
        if pos in unvisited_children[parent]:
            unvisited_children[parent].remove(pos)
        if not unvisited_children[parent]:  # if there are no more unvisited children
            del unvisited_children[parent]


def backpropogate(pos, mtm, res):
    if pos == head:
        if pos in visits:
            visits[pos] += 1
            wins[pos] += 1 if (mtm == res) else 0
        else:
            visits[pos] = 1
            wins[pos] = 1 if (mtm == res) else 0
        return
    parents = parentss[pos]
    if pos in visits:
        visits[pos] += 1
        wins[pos] += 1 if (mtm == res) else 0
    else:
        visits[pos] = 1
        wins[pos] = 1 if (mtm == res) else 0
    for parent in parents:
        add_to_visited(parent, pos)
        remove_from_unvisited(parent, pos)
        backpropogate(parent, not mtm, res)


def make_forced_move(board):
    for y in range(8):
        for x in range(8):
            if board[y][x] == ' ':
                print("I LOST")
                return y, x


def move(board, col):
    global head
    start = timer()

    my_bib, other_bib = gbib.make_bitboards(board, col)

    #gbib.good_moves(my_bib, other_bib)  # NEW

    head = gbib.bibs_to_pos(my_bib, other_bib)
    parentss[head] = []
    i = 0
    selected = set()
    while (timer() - start) < 1.98:
        pos, mtm = select(head, True)
        selected.add(pos)
        pos, mtm = expand(pos, mtm)
        res = rollout(pos, mtm)
        backpropogate(pos, mtm, res)
        i += 1

    best_pos = max(list(visited_children[head]), key=lambda p: visits[p])

    move_bib = gbib.pos_to_cbib(head ^ best_pos)

    move_y, move_x = gbib.move_bib_to_yx(move_bib)

    if(board[move_y][move_x] != ' '):
        move_y, move_x = make_forced_move(board)

    print("mcts:", i, "\t", timer() - start)
    #print("parents", len(parentss))
    #print("children", len(visited_children))
    #print("p move", len(potential_moves))

    return move_y, move_x


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


if __name__ == '__main__':
    board = make_empty_board(8)
    board[0][0] = 'b'
    board[1][1] = 'w'
    print(move(board, 'w'))

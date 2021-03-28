def likely_moves(c_bib):
    if c_bib & 0x70507 << 0 and not (c_bib & 0x1 << 9):
        yield 9
    if c_bib & 0x70507 << 1 and not (c_bib & 0x1 << 10):
        yield 10
    if c_bib & 0x70507 << 2 and not (c_bib & 0x1 << 11):
        yield 11
    if c_bib & 0x70507 << 3 and not (c_bib & 0x1 << 12):
        yield 12
    if c_bib & 0x70507 << 4 and not (c_bib & 0x1 << 13):
        yield 13
    if c_bib & 0x70507 << 5 and not (c_bib & 0x1 << 14):
        yield 14
    if c_bib & 0x70507 << 8 and not (c_bib & 0x1 << 17):
        yield 17
    if c_bib & 0x70507 << 9 and not (c_bib & 0x1 << 18):
        yield 18
    if c_bib & 0x70507 << 10 and not (c_bib & 0x1 << 19):
        yield 19
    if c_bib & 0x70507 << 11 and not (c_bib & 0x1 << 20):
        yield 20
    if c_bib & 0x70507 << 12 and not (c_bib & 0x1 << 21):
        yield 21
    if c_bib & 0x70507 << 13 and not (c_bib & 0x1 << 22):
        yield 22
    if c_bib & 0x70507 << 16 and not (c_bib & 0x1 << 25):
        yield 25
    if c_bib & 0x70507 << 17 and not (c_bib & 0x1 << 26):
        yield 26
    if c_bib & 0x70507 << 18 and not (c_bib & 0x1 << 27):
        yield 27
    if c_bib & 0x70507 << 19 and not (c_bib & 0x1 << 28):
        yield 28
    if c_bib & 0x70507 << 20 and not (c_bib & 0x1 << 29):
        yield 29
    if c_bib & 0x70507 << 21 and not (c_bib & 0x1 << 30):
        yield 30
    if c_bib & 0x70507 << 24 and not (c_bib & 0x1 << 33):
        yield 33
    if c_bib & 0x70507 << 25 and not (c_bib & 0x1 << 34):
        yield 34
    if c_bib & 0x70507 << 26 and not (c_bib & 0x1 << 35):
        yield 35
    if c_bib & 0x70507 << 27 and not (c_bib & 0x1 << 36):
        yield 36
    if c_bib & 0x70507 << 28 and not (c_bib & 0x1 << 37):
        yield 37
    if c_bib & 0x70507 << 29 and not (c_bib & 0x1 << 38):
        yield 38
    if c_bib & 0x70507 << 32 and not (c_bib & 0x1 << 41):
        yield 41
    if c_bib & 0x70507 << 33 and not (c_bib & 0x1 << 42):
        yield 42
    if c_bib & 0x70507 << 34 and not (c_bib & 0x1 << 43):
        yield 43
    if c_bib & 0x70507 << 35 and not (c_bib & 0x1 << 44):
        yield 44
    if c_bib & 0x70507 << 36 and not (c_bib & 0x1 << 45):
        yield 45
    if c_bib & 0x70507 << 37 and not (c_bib & 0x1 << 46):
        yield 46
    if c_bib & 0x70507 << 40 and not (c_bib & 0x1 << 49):
        yield 49
    if c_bib & 0x70507 << 41 and not (c_bib & 0x1 << 50):
        yield 50
    if c_bib & 0x70507 << 42 and not (c_bib & 0x1 << 51):
        yield 51
    if c_bib & 0x70507 << 43 and not (c_bib & 0x1 << 52):
        yield 52
    if c_bib & 0x70507 << 44 and not (c_bib & 0x1 << 53):
        yield 53
    if c_bib & 0x70507 << 45 and not (c_bib & 0x1 << 54):
        yield 54
    if c_bib & (0x30203 << 0) and not (c_bib & 0x1 << 8):
        yield 8
    if c_bib & (0xc040c0 << 0) and not (c_bib & 0x1 << 15):
        yield 15
    if c_bib & (0x30203 << 8) and not (c_bib & 0x1 << 16):
        yield 16
    if c_bib & (0xc040c0 << 8) and not (c_bib & 0x1 << 23):
        yield 23
    if c_bib & (0x30203 << 16) and not (c_bib & 0x1 << 24):
        yield 24
    if c_bib & (0xc040c0 << 16) and not (c_bib & 0x1 << 31):
        yield 31
    if c_bib & (0x30203 << 24) and not (c_bib & 0x1 << 32):
        yield 32
    if c_bib & (0xc040c0 << 24) and not (c_bib & 0x1 << 39):
        yield 39
    if c_bib & (0x30203 << 32) and not (c_bib & 0x1 << 40):
        yield 40
    if c_bib & (0xc040c0 << 32) and not (c_bib & 0x1 << 47):
        yield 47
    if c_bib & (0x30203 << 40) and not (c_bib & 0x1 << 48):
        yield 48
    if c_bib & (0xc040c0 << 40) and not (c_bib & 0x1 << 55):
        yield 55
    if c_bib & (0x705 << 0) and not (c_bib & 0x1 << 1):
        yield 1
    if c_bib & (0x507000000000000 << 0) and not (c_bib & 0x1 << 57):
        yield 57
    if c_bib & (0x705 << 1) and not (c_bib & 0x1 << 2):
        yield 2
    if c_bib & (0x507000000000000 << 1) and not (c_bib & 0x1 << 58):
        yield 58
    if c_bib & (0x705 << 2) and not (c_bib & 0x1 << 3):
        yield 3
    if c_bib & (0x507000000000000 << 2) and not (c_bib & 0x1 << 59):
        yield 59
    if c_bib & (0x705 << 3) and not (c_bib & 0x1 << 4):
        yield 4
    if c_bib & (0x507000000000000 << 3) and not (c_bib & 0x1 << 60):
        yield 60
    if c_bib & (0x705 << 4) and not (c_bib & 0x1 << 5):
        yield 5
    if c_bib & (0x507000000000000 << 4) and not (c_bib & 0x1 << 61):
        yield 61
    if c_bib & (0x705 << 5) and not (c_bib & 0x1 << 6):
        yield 6
    if c_bib & (0x507000000000000 << 5) and not (c_bib & 0x1 << 62):
        yield 62
    if c_bib & 0x302 and not (c_bib & 0x1 << 0):
        yield 0
    if c_bib & 0xc040 and not (c_bib & 0x1 << 7):
        yield 7
    if c_bib & 0x203000000000000 and not (c_bib & 0x1 << 56):
        yield 56
    if c_bib & 0x40c0000000000000 and not (c_bib & 0x1 << 63):
        yield 63

# -0xc3c3c3c3c3c3c3c4 all but 2 side bits
# -0x8181818181818182 all but side bits
# -0xc0c0c0c0c0c0c0c1 all but 2 right most bits
# -0x303030303030304 all but 2 left most bits
# -0x101010101010102  all but leftmost bits
# -0x8080808080808081 all but rightmost bits
# -0xffff000000010000 all but 2 top and bot bits
# -0xff00000000000100 all but top and bot
# -0xffffc3c3c3c40000 all but outside 2 bits

def hori_2(bib):
    return bib & (bib >> 1) & -0x8080808080808081

def vert_2(bib):
    return bib & (bib >> 8)

def diagu_2(bib):
    return bib & (bib >> 7) & -0x8080808080808081

def diagd_2(bib):
    return bib & (bib >> 9) & -0x8080808080808081

def hori_3(bib):
    return bib & (bib >> 1) & (bib << 1) & -0x8181818181818182

def vert_3(bib):
    return bib & (bib >> 8) & (bib << 8)

def diagu_3(bib):
    return bib & (bib >> 7) & (bib << 7) & -0x8181818181818182

def diagd_3(bib):
    return bib & (bib >> 9) & (bib << 9) & -0x8181818181818182

def hori_5(bib):
    return bib & (bib >> 1) & (bib >> 2) & (bib << 1) & (bib << 2) & -0xc3c3c3c3c3c3c3c4

def vert_5(bib):
    return bib & (bib >> 8) & (bib >> 16) & (bib << 8) & (bib << 16)

def diagu_5(bib):
    return bib & (bib >> 7) & (bib >> 14) & (bib << 7) & (bib << 14) & -0xc3c3c3c3c3c3c3c4

def diagd_5(bib):
    return bib & (bib >> 9) & (bib >> 18) & (bib << 9) & (bib << 18) & -0xc3c3c3c3c3c3c3c4

def is_tie(c_bib):
    return c_bib == 0xffffffffffffffff

WIN_SCORE = 1000000000000000000000


def count_bits(a):
    return bin(a).count('1')


def count_open_semi_open(bib, c_bib, b_shift, f_shift, b_mask, f_mask):
    b = bib & ((c_bib << b_shift) | b_mask)
    f = bib & ((c_bib >> f_shift) | f_mask)
    o = bib & ~b & ~f
    s = b ^ f
    n_o = 0
    n_s = 0
    if o:
        n_o += count_bits(o)
    if s:
        n_s += count_bits(s)
    return n_o, n_s

# 0x101010101010101 all bits in col 0
# 0x4040404040404040 bits in col 6
# 0x202020202020202 all bits in col 1
# 0x2020202020202020 all bits in col 5
# 0xff all bits in row 0
# 0xff00 all bits in row 1
# 0xff0000000000 all bits in row 5
# 0xff000000000000 all bits in row 6
# 0xff00000000000000 all bits in row 7
def score_bib(my_bib, other_bib):
    o_2, s_2, o_3, s_3, o_4, s_4 = 0, 0, 0, 0, 0, 0
    # Horizontal
    c_bib = my_bib | other_bib
    o_hori_2 = my_bib & (my_bib >> 1) & -0x8080808080808081
    o_hori_3 = o_hori_2 & (my_bib << 1) & -0x101010101010102
    o_hori_4 = o_hori_3 & (my_bib >> 2) & -0xc0c0c0c0c0c0c0c1

    o, s = count_open_semi_open(o_hori_2, c_bib, 1, 2, 0x101010101010101, 0x4040404040404040)
    o_2 += o
    s_2 += s

    o, s = count_open_semi_open(o_hori_3, c_bib, 2, 2, 0x202020202020202, 0x4040404040404040)
    o_3 += o
    s_3 += s

    o, s = count_open_semi_open(o_hori_4, c_bib, 2, 3, 0x202020202020202, 0x2020202020202020)
    o_4 += o
    s_4 += s

    # vertical
    o_vert_2 = my_bib & (my_bib >> 8)
    o_vert_3 = o_vert_2 & (my_bib << 8)
    o_vert_4 = o_vert_3 & (my_bib >> 8)

    o, s = count_open_semi_open(o_vert_2, c_bib, 8, 16, 0xff, 0xff000000000000)
    o_2 += o
    s_2 += s

    o, s = count_open_semi_open(o_vert_3, c_bib, 16, 16, 0xff00, 0xff000000000000)
    o_3 += o
    s_3 += s

    o, s = count_open_semi_open(o_vert_4, c_bib, 16, 24, 0xff00, 0xff0000000000)
    o_4 += o
    s_4 += s

    # diagu
    o_diagu_2 = my_bib & (my_bib >> 7) & -0x8080808080808081
    o_diagu_3 = o_diagu_2 & (my_bib << 7) & -0x101010101010102
    o_diagu_4 = o_diagu_3 & (my_bib >> 14) & -0xc0c0c0c0c0c0c0c1

    o, s = count_open_semi_open(o_diagu_2, c_bib, 7, 14, 0x101010101010101, 0x4040404040404040)
    o_2 += o
    s_2 += s

    o, s = count_open_semi_open(o_diagu_3, c_bib, 14, 14, 0x202020202020202, 0x4040404040404040)
    o_3 += o
    s_3 += s

    o, s = count_open_semi_open(o_diagu_4, c_bib, 14, 21, 0x202020202020202, 0x2020202020202020)
    o_4 += o
    s_4 += s

    # diagd
    o_diagd_2 = my_bib & (my_bib >> 9) & -0x8080808080808081
    o_diagd_3 = o_diagd_2 & (my_bib << 9) & -0x101010101010102
    o_diagd_4 = o_diagd_3 & (my_bib >> 18) & -0xc0c0c0c0c0c0c0c1

    o, s = count_open_semi_open(o_diagd_2, c_bib, 9, 18, 0x101010101010101, 0x4040404040404040)
    o_2 += o
    s_2 += s

    o, s = count_open_semi_open(o_diagd_3, c_bib, 18, 18, 0x202020202020202, 0x4040404040404040)
    o_3 += o
    s_3 += s

    o, s = count_open_semi_open(o_diagd_4, c_bib, 18, 27, 0x202020202020202, 0x2020202020202020)
    o_4 += o
    s_4 += s

    return s_2 + 2 * o_2 + 10 * s_3 + 50 * o_3 + 50 * s_4 + 500 * o_4


def score(pos, mtm):  # mtm is true if i am scoring for me, if i just moved
    if mtm:
        my_bib, other_bib = pos_to_bibs(pos)
    else:
        other_bib, my_bib = pos_to_bibs(pos)
    if is_win(my_bib):
        return WIN_SCORE
    return score_bib(my_bib, other_bib) - score_bib(other_bib, my_bib)


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


def is_win(bib):  # if the pos has a win due to the move
    temp = hori_5(bib)
    if temp and not hori_2(temp):
        return True
    temp = vert_5(bib)
    if temp and not vert_2(temp):
        return True
    temp = diagu_5(bib)
    if temp and not diagu_2(temp):
        return True
    temp = diagd_5(bib)
    if temp and not diagd_2(temp):
        return True


def make_bitboards(board, col):
    my_bib = 0x0000000000000000
    other_bib = 0x0000000000000000

    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == col:
                my_bib |= 0x01 << x + y * 8
            elif board[y][x] != " ":
                other_bib |= 0x01 << x + y * 8
    return my_bib, other_bib


def bib_to_board(w_bib, b_bib):
    board = []
    i = 0
    for y in range(8):
        board.append([' '] * 8)
        for x in range(8):
            if w_bib >> i & 0x1:
                board[y][x] = "w"
            elif b_bib >> i & 0x1:
                board[y][x] = "b"
            i += 1
    return board


def pos_to_board(pos):
    m, o = pos_to_bibs(pos)
    return bib_to_board(m, o)


def bibs_to_pos(my_bib, other_bib):
    return (my_bib << 64) | other_bib


def move_bib_to_yx(move_bib):
    move = 0
    while not move_bib & 0x1:
        move += 1
        move_bib = move_bib >> 1
    return move // 8, move % 8


def pos_to_bibs(pos):
    return pos >> 64, pos & 0xFFFFFFFFFFFFFFFF


def pos_to_cbib(pos):
    return (pos >> 64) | (pos & 0xFFFFFFFFFFFFFFFF)


if __name__ == '__main__':
    board = make_empty_board(8)
    board[5][2] = 'w'
    board[5][1] = 'w'

    my_bib, other_bib = make_bitboards(board, 'w')
    print_board(bib_to_board(my_bib, other_bib))
    score_bib(my_bib, other_bib)

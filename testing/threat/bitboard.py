rotations = {}

def count_bits(a):
    return bin(a).count('1')


def board_to_bbs(board, col):
    m_bb = 0x0000000000000000
    o_bb = 0x0000000000000000

    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == col:
                m_bb |= 0x01 << x + y * 8
            elif board[y][x] != " ":
                o_bb |= 0x01 << x + y * 8
    get_rotations(m_bb)
    get_rotations(o_bb)
    return m_bb, o_bb


def board_to_pos(board, col):
    pos = 0x00000000000000000000000000000000

    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == col:
                pos |= 0x01 << (x + y * 8) + 64
            elif board[y][x] != " ":
                pos |= 0x01 << (x + y * 8)
    return pos


def bb_to_pos(m_bb, o_bb):
    return (m_bb << 64) | o_bb


def pos_to_m_bb(pos):
    return pos >> 64


def pos_to_o_bb(pos):
    return pos & 0xFFFFFFFFFFFFFFFF


def pos_to_bb(pos):
    return pos_to_m_bb(pos), pos & pos_to_o_bb(pos)


def pos_to_c_bb(pos):
    return pos_to_m_bb(pos) | pos_to_o_bb(pos)


def move_to_yx(move):
    i = 0
    while not move & 0x1 and i < 64:
        i += 1
        move = move >> 1
    if i >= 64:
        return 0, 0
    return i_to_yx(i)


def i_to_yx(i):
    return i // 8, i % 8


def print_bb(bb):
    s = "*"
    for i in range(7):
        s += str(i%10) + "|"
    s += str((7)%10)
    s += "*\n"

    for i in range(8):
        s += str(i%10)
        for j in range(8-1):
            s += ('X' if (1 & bb >> (i*8 + j)) else ' ') + "|"
        s += 'X' if (1 & bb >> (i*8 + 7)) else ' '

        s += "*\n"
    s += (8*2 + 1)*"*"

    print(s)


def yx_to_i(y, x):
    return (y*8 + x)


def yx_to_move(y, x):
    return 1 << yx_to_i(y, x)


def get_i(bb, i):
    return 1 & (bb >> i)


def place_i(bb, i):
    rotations = get_rotations(bb)
    bb |= 1 << i
    if bb not in rotations:
        r_90 = rotations[90] | 1 << i90[i]
        r_45 = rotations[45]
        if 0 <= (i // 8) + (i % 8) - 4 <= 6:
            r_45 |= 1 << i45[i]
        r_135 = rotations[135]
        if 0 <= (i // 8) - (i % 8) + 3 <= 6:
            r_135 |= 1 << i135[i]
        rotations[bb] = {90: r_90, 45: r_45, 135: r_135}
    return bb


def pos_place_i(pos, i, mtm):
    m_bb = pos_to_m_bb(pos)
    o_bb = pos_to_o_bb(pos)
    if mtm:
        m_bb = place_i(m_bb, i)
    else:
        o_bb = place_i(o_bb, i)
    return bb_to_pos(m_bb, o_bb)


def i_to_row(i, angle):
    if angle == 0:
        return i//8
    elif angle == 90:
        return i % 8
    elif angle == 45:
        row = (i // 8) + (i % 8) - 4
        if 0 <= row <= 6:
            return row
        else:
            return None
    elif angle == 135:
        row = (i // 8) - (i % 8) + 3
        if 0 <= row <= 6:
            return row
        else:
            return None


row_lengths = {0: 5, 1: 6, 2: 7, 3: 8, 4: 7, 5: 6, 6: 5}
row45_masks = {0: 0x1f, 1: 0x3f, 2: 0x7f, 3: 0xff, 4: 0x7f, 5: 0x3f, 6: 0x1f}
row45_starts = {0: 0, 1: 5, 2: 11, 3: 18, 4: 24, 5: 31, 6: 38}
row0_start_i = {0: 0, 1: 8, 2: 16, 3: 24, 4: 32, 5: 40, 6: 48, 7: 56}
row90_start_i = {0: 56, 1: 57, 2: 58, 3: 59, 4: 60, 5: 61, 6: 62, 7: 63}
row45_start_i = {0: 32, 1: 40, 2: 48, 3: 56, 4: 57, 5: 58, 6: 59}
row135_start_i = {0: 3, 1: 2, 2: 1, 3: 0, 4: 8, 5: 16, 6: 24}
i90 = {0: 7, 1: 15, 2: 23, 3: 31, 4: 39, 5: 47, 6: 55, 7: 63, 8: 6, 9: 14, 10: 22, 11: 30, 12: 38, 13: 46, 14: 54, 15: 62, 16: 5, 17: 13, 18: 21, 19: 29, 20: 37, 21: 45, 22: 53, 23: 61, 24: 4, 25: 12, 26: 20, 27: 28, 28: 36, 29: 44, 30: 52, 31: 60, 32: 3, 33: 11, 34: 19, 35: 27, 36: 35, 37: 43, 38: 51, 39: 59, 40: 2, 41: 10, 42: 18, 43: 26, 44: 34, 45: 42, 46: 50, 47: 58, 48: 1, 49: 9, 50: 17, 51: 25, 52: 33, 53: 41, 54: 49, 55: 57, 56: 0, 57: 8, 58: 16, 59: 24, 60: 32, 61: 40, 62: 48, 63: 56}
i45 = {32: 0, 25: 1, 18: 2, 11: 3, 4: 35, 40: 5, 33: 6, 26: 7, 19: 8, 12: 9, 5: 10, 48: 11, 41: 12, 34: 13, 27: 14, 20: 15, 13: 16, 6: 17, 56: 18, 49: 19, 42: 20, 35: 21, 28: 22, 21: 23, 14: 24, 7: 25, 57: 26, 50: 27, 43: 28, 36: 29, 29: 30, 22: 31, 15: 32, 58: 33, 51: 34, 44: 35, 37: 36, 30: 37, 23: 38, 59: 39, 52: 40, 45: 41, 38: 42, 31: 43}
i135 = {3: 0, 12: 1, 21: 2, 30: 3, 39: 4, 2: 5, 11: 6, 20: 7, 29: 8, 38: 9, 47: 10, 1: 11, 10: 12, 19: 13, 28: 14, 37: 15, 46: 16, 55: 17, 0: 18, 9: 19, 18: 20, 27: 21, 36: 22, 45: 23, 54: 24, 63: 25, 8: 26, 17: 27, 26: 28, 35: 29, 44: 30, 53: 31, 62: 32, 16: 33, 25: 34, 34: 35, 43: 36, 52: 37, 61: 38, 24: 39, 33: 40, 42: 41, 51: 42, 60: 43}

def rowi_to_i(rowi, r, angle):
    if angle == 0:
        return row0_start_i[r] + rowi
    elif angle == 90:
        return row90_start_i[r] - rowi*8
    elif angle == 45:
        return row45_start_i[r] - rowi*7
    elif angle == 135:
        return row135_start_i[r] + rowi*9


def get_rotations(bb):
    if bb not in rotations:
        rotations[bb] = {90: rotate_90(bb), 45: rotate_45(bb), 135: rotate_135(bb)}
    return rotations[bb]


def get_row(bb, r, square):
    if square:
        return (bb >> r*8) & 0xff
    else:
        return bb >> row45_starts[r] & row45_masks[r]


def get_prow(m_bb, o_bb, r, square):
    if square:
        return (get_row(m_bb, r, square) << 8) | get_row(o_bb, r, square)
    else:
        return (get_row(m_bb, r, square) << row_lengths[r]) | get_row(o_bb, r, square)


def rotate_90(bb):
    r_bb = 0x0
    for i in range(64):
        r_bb |= get_i(bb, i) << i90[i]
    return r_bb


def rotate_45(bb):
    r_bb = 0x0
    for i in i45:
        r_bb |= get_i(bb, i) << i45[i]
    return r_bb


def rotate_135(bb):
    r_bb = 0x0
    for i in i135:
        r_bb |= get_i(bb, i) << i135[i]
    return r_bb


def is_tie(pos):
    return pos_to_c_bb(pos) == 0xffffffffffffffff




if __name__ == '__main__':
    bb = 0xff00f00100ff2007
    print_bb(bb)
    print_bb(rotate_90(bb))
    print_bb(rotate_45(bb))
    print_bb(rotate_135(bb))

    i135 = {key-1: i135[key] for key in i135}
    print(i135)

    s = "*"
    for i in range(7):
        s += str(i%10) + "|"
    s += str((7)%10)
    s += "*\n"

    for i in range(8):
        s += str(i%10)
        for j in range(8-1):
            s += str(i*8+j) + "\t|"
        s += str(i*8+7)

        s += "*\n"
    s += (8*2 + 1)*"*"

    print(s)

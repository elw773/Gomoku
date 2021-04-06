WIN_SCORE = 1000000000

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


def get_twos(bib, c_bib):
    return (((bib << 1 & bib << 2) & -0x303030303030304) | ((bib >> 1 & bib >> 2) & -0xc0c0c0c0c0c0c0c1) |
            ((bib << 9 & bib << 18) & -0x303030303030304) | ((bib >> 9 & bib >> 18) & -0xc0c0c0c0c0c0c0c1) |
            ((bib >> 7 & bib >> 14) & -0x303030303030304) | ((bib << 7 & bib << 14) & -0xc0c0c0c0c0c0c0c1) |
            (bib << 8 & bib << 16) | (bib >> 8 & bib >> 16)) & ~c_bib

def get_threes(bib, c_bib):
    return (((bib << 1 & bib << 2 & bib << 3) & -0x707070707070708) | ((bib >> 1 & bib >> 2 & bib >> 3) & -0xe0e0e0e0e0e0e0e1) |
            ((bib << 9 & bib << 18 & bib << 27) & -0x707070707070708) | ((bib >> 9 & bib >> 18 & bib >> 27) & -0xe0e0e0e0e0e0e0e1) |
            ((bib >> 7 & bib >> 14 & bib >> 21) & -0x707070707070708) | ((bib << 7 & bib << 14 & bib << 21) & -0xe0e0e0e0e0e0e0e1) |
            (bib << 8 & bib << 16 & bib << 24) | (bib >> 8 & bib >> 16 & bib >> 24)) & ~c_bib

def get_fours(bib, c_bib):
    return (((bib << 1 & bib << 2 & bib << 3 & bib << 4) & -0xf0f0f0f0f0f0f10) | ((bib >> 1 & bib >> 2 & bib >> 3 & bib >> 4) & -0xf0f0f0f0f0f0f0f1) |
            ((bib << 9 & bib << 18 & bib << 27 & bib << 36) & -0xf0f0f0f0f0f0f10) | ((bib >> 9 & bib >> 18 & bib >> 27 & bib >> 36) & -0xf0f0f0f0f0f0f0f1) |
            ((bib >> 7 & bib >> 14 & bib >> 21 & bib >> 28) & -0xf0f0f0f0f0f0f10) | ((bib << 7 & bib << 14 & bib << 21 & bib << 28) & -0xf0f0f0f0f0f0f0f1) |
            (bib << 8 & bib << 16 & bib << 24 & bib << 32) | (bib >> 8 & bib >> 16 & bib >> 24 & bib >> 32)) & ~c_bib

# Scores:
ors = {2: 2, 3: 50, 4: 500}
sors = {2: 1, 3: 10, 4: 100}
#do_direction(None, m_bib, o_bib, 1, 0x8080808080808080, 0x101010101010101, True)
# scores the effect of each move on a_bib
def do_direction(move_scores, a_bib, o_bib, shift, rs_mask, ls_mask, atm, score_sign):  # atm true: placing on a_bib
    c_bib = a_bib | o_bib

    f_1 = a_bib >> shift & ~rs_mask & ~c_bib
    b_1 = a_bib << shift & ~ls_mask & ~c_bib
    f_2 = f_1 & a_bib >> (shift * 2) & ~(rs_mask >> shift) & ~c_bib
    b_2 = b_1 & a_bib << (shift * 2) & ~(ls_mask << shift) & ~c_bib
    f_3 = f_2 & a_bib >> (shift * 3) & ~(rs_mask >> (shift * 2)) & ~c_bib
    b_3 = b_2 & a_bib << (shift * 3) & ~(ls_mask << (shift * 2)) & ~c_bib
    f_4 = f_3 & a_bib >> (shift * 4) & ~(rs_mask >> (shift * 3)) & ~c_bib
    b_4 = b_3 & a_bib << (shift * 4) & ~(ls_mask << (shift * 3)) & ~c_bib
    f_1 = f_1 & ~f_2
    b_1 = b_1 & ~b_2
    f_2 = f_2 & ~f_3
    b_2 = b_2 & ~b_3
    f_3 = f_3 & ~f_4
    b_3 = b_3 & ~b_4
    f_4 = f_4 & (o_bib >> (shift * 5) | ~c_bib >> (shift * 5) | rs_mask >> (shift * 4))
    b_4 = b_4 & (o_bib << (shift * 5) | ~c_bib << (shift * 5) | rs_mask >> (shift * 4))

    o_f_0 = ~c_bib >> shift & ~rs_mask & ~c_bib
    c_f_0 = (o_bib >> shift & ~rs_mask & ~c_bib) | rs_mask
    o_b_0 = ~c_bib << shift & ~ls_mask & ~c_bib
    c_b_0 = (o_bib >> shift & ~ls_mask & ~c_bib) | ls_mask
    o_f_1 = f_1 & ~(c_bib >> (shift * 2)) & ~(rs_mask >> (shift))
    c_f_1 = f_1 & ~o_f_1
    o_b_1 = b_1 & ~(c_bib << (shift * 2)) & ~(ls_mask << (shift))
    c_b_1 = b_1 & ~o_b_1
    o_f_2 = f_2 & ~(c_bib >> (shift * 3)) & ~(rs_mask >> (shift * 2))
    c_f_2 = f_2 & ~o_f_2
    o_b_2 = b_2 & ~(c_bib << (shift * 3)) & ~(ls_mask << (shift * 2))
    c_b_2 = b_2 & ~o_b_2
    o_f_3 = f_3 & ~(c_bib >> (shift * 4)) & ~(rs_mask >> (shift * 3))
    c_f_3 = f_3 & ~o_f_3
    o_b_3 = b_3 & ~(c_bib << (shift * 4)) & ~(ls_mask << (shift * 3))
    c_b_3 = b_3 & ~o_b_3
    o_f_4 = f_4 & ~(c_bib >> (shift * 5)) & ~(rs_mask >> (shift * 4))
    c_f_4 = f_4 & ~o_f_4
    o_b_4 = b_4 & ~(c_bib << (shift * 5)) & ~(ls_mask << (shift * 4))
    c_b_4 = b_4 & ~o_b_4

    if atm:
        o_2 = (o_b_0 & o_f_1) | (o_f_0 & o_b_1)
        s_2 = (o_b_0 & c_f_1) | (o_f_0 & c_b_1) | (c_b_0 & o_f_1) | (c_f_0 & o_b_1)
        o_3 = (o_b_0 & o_f_2) | (o_f_0 & o_b_2) | \
                (o_b_1 & o_f_1)
        s_3 = (o_b_0 & c_f_2) | (o_f_0 & c_b_2) | (c_b_0 & o_f_2) | (c_f_0 & o_b_2) | \
                (c_b_1 & o_f_1) | (o_b_1 & c_f_1)
        o_4 = (o_b_0 & o_f_3) | (o_f_0 & o_b_3) | \
                (o_b_1 & o_f_2) | (o_f_1 & o_b_2)
        s_4 = (o_b_0 & c_f_3) | (o_f_0 & c_b_3) | (c_b_0 & o_f_3) | (c_f_0 & o_b_3) | \
                (c_b_1 & o_f_2) | (c_f_1 & o_b_2) | (o_b_1 & c_f_2) | (o_f_1 & c_b_2)
        win = ((c_b_0 | o_b_0) & f_4) | ((c_f_0 | o_f_0) & b_4) | \
                (b_1 & f_3) | (f_1 & b_3) | \
                (b_2 & f_2)
        for i in range(64):
            move = 0x1 << i
            move_scores[i] += score_sign * \
                                ((ors[2] if o_2 & move else 0) +
                                (sors[2] if s_2 & move else 0) +
                                (ors[3] if o_3 & move else 0) +
                                (sors[3] if s_3 & move else 0) +
                                (ors[4] if o_4 & move else 0) +
                                (sors[4] if s_4 & move else 0) +
                                (5*WIN_SCORE if win & move else 0)) - \
                                ((ors[2] if o_f_2 & move else 0) +  # we need to subtract the score that the rows made before
                                (ors[2] if o_b_2 & move else 0) +
                                (sors[2] if c_f_2 & move else 0) +
                                (sors[2] if c_b_2 & move else 0) +
                                (ors[3] if o_f_3 & move else 0) +
                                (ors[3] if o_b_3 & move else 0) +
                                (sors[3] if c_f_3 & move else 0) +
                                (sors[3] if c_b_3 & move else 0) +
                                (ors[4] if o_f_4 & move else 0) +
                                (ors[4] if o_b_4 & move else 0) +
                                (sors[4] if c_f_4 & move else 0) +
                                (sors[4] if c_b_4 & move else 0))
    else:
        for i in range(64):
            move = 0x1 << i
            move_scores[i] -= score_sign * \
                            ((ors[2] - sors[2] if o_f_2 & move else 0) +
                            (ors[2] - sors[2] if o_b_2 & move else 0) +
                            (sors[2] if c_f_2 & move else 0) +
                            (sors[2] if c_b_2 & move else 0) +
                            (ors[3] - sors[3] if o_f_3 & move else 0) +
                            (ors[3] - sors[3] if o_b_3 & move else 0) +
                            (sors[3] if c_f_3 & move else 0) +
                            (sors[3] if c_b_3 & move else 0) +
                            (ors[4] - sors[4] if o_f_4 & move else 0) +
                            (ors[4] - sors[4] if o_b_4 & move else 0) +
                            (sors[4] if c_f_4 & move else 0) +
                            (sors[4] if c_b_4 & move else 0))


# -0xff81818181818200 all bits except outside
# -0xffffc3c3c3c40000 all bits except outside 2
def make_children(m_bib, o_bib, mtm, prev_score, scores):  # mtm true if i am moving
    c_bib = m_bib | o_bib
    move_scores = [prev_score] * 64
    #sign = 1 #if mtm else -1
    # TODO: masks are all wrong for diagonals
    # top and right 0x80808080808080ff
    # bottom and left 0xff01010101010101
    # top and left 0x1010101010101ff
    # bottom and right 0xff80808080808080
    # horizontal
    do_direction(move_scores, m_bib, o_bib, 1, 0x8080808080808080, 0x101010101010101, mtm, 1)
    do_direction(move_scores, o_bib, m_bib, 1, 0x8080808080808080, 0x101010101010101, not mtm, -1)
    # diagu
    do_direction(move_scores, m_bib, o_bib, 7, 0x80808080808080ff, 0xff01010101010101, mtm, 1)
    do_direction(move_scores, o_bib, m_bib, 7, 0x80808080808080ff, 0xff01010101010101, not mtm, -1)
    # diagd
    do_direction(move_scores, m_bib, o_bib, 9, 0xff80808080808080, 0x1010101010101ff, mtm, 1)
    do_direction(move_scores, o_bib, m_bib, 9, 0xff80808080808080, 0x1010101010101ff, not mtm, -1)
    # vertical
    do_direction(move_scores, m_bib, o_bib, 8, 0xff00000000000000, 0xff, mtm, 1)
    do_direction(move_scores, o_bib, m_bib, 8, 0xff00000000000000, 0xff, not mtm, -1)

    children = []
    for i in range(64):
        if (~c_bib) & (0x1 << i):
            if mtm:
                child = bibs_to_pos(m_bib | 0x1 << i, o_bib)
            else:
                child = bibs_to_pos(m_bib, o_bib | 0x1 << i)
            score = move_scores[i]
            if score >= WIN_SCORE:
                score = WIN_SCORE
            elif score <= -WIN_SCORE:
                score = -WIN_SCORE
            scores[child] = score
            children.append(child)
    children.sort(key=lambda c: scores[c], reverse=mtm)
    return children


    #c_bib = m_bib | o_bib
    #ones = (((c_bib << 1 | c_bib << 9 | c_bib >> 7) & -0x101010101010102) |
    #            ((c_bib >> 1 | c_bib >> 9 | c_bib << 7) & -0x8080808080808081) |
    #            (c_bib << 8 | c_bib >> 8)) & ~c_bib
    #m_twos = ((c_bib << 2 | c_bib << 18 | c_bib >> 14) & -0x303030303030304) | \
    #            ((c_bib >> 2 | c_bib >> 18 | c_bib << 14) & -0xc0c0c0c0c0c0c0c1) | \
    #            (c_bib << 16 | c_bib >> 16)
    #m_fours = get_fours(m_bib, c_bib)
    #m_threes = get_threes(m_bib, c_bib)
    #m_twos = get_twos(m_bib, c_bib)

    #o_fours = get_fours(o_bib, c_bib)
    #o_threes = get_threes(o_bib, c_bib)
    #o_twos = get_twos(m_bib, c_bib)

    #threes = m_threes & o_threes
    #twos = m_twos & o_twos

    #pos = bibs_to_pos(m_bib, o_bib)
    #children = []
    #if mtm:
#    for i in range(64):
    #        move = 0x1 << i
    #        if move & ones:
    #            child = pos | move << 64
    #            children.append(child)
    #            if move & m_fours & is_win(my_bib | move):
    #                scores[child] = WIN_SCORE
    #                continue
    #            if move & threes:
    #                scores[child] = score + 1000
    #            if move & twos:
    #                scores[child] = score + 500
    #            else:
    #                scores[child] = score + 10
    # TODO: you need to store individual directions to properly calculate score change
    #children.sort(reverse=True, key=lambda c: scores[c])
    #return children

    #print("good moves", count_bits(c_bib), count_bits(useful_ones), count_bits(twos), count_bits(useful_twos))

# -0xc3c3c3c3c3c3c3c4 all but 2 side bits
# -0x8181818181818182 all but side bits
# -0xc0c0c0c0c0c0c0c1 all but 2 right most bits
# -0x303030303030304 all but 2 left most bits
# -0x101010101010102  all but leftmost bits
# -0x8080808080808081 all but rightmost bits
# -0xffff000000010000 all but 2 top and bot bits
# -0xff00000000000100 all but top and bot
# -0xffffc3c3c3c40000 all but outside 2 bits
# -0x707070707070708 all but left 3 most
# -0xe0e0e0e0e0e0e0e1 all but right 3 most bits
# -0xf0f0f0f0f0f0f10 all but left 4 bits
# -0xf0f0f0f0f0f0f0f1 all but right 4 bits
# 0xffffffffffffffff all bits
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
def score_bib(m_bib, o_bib):
    if is_win(m_bib):
        return WIN_SCORE
    o_2, s_2, o_3, s_3, o_4, s_4 = 0, 0, 0, 0, 0, 0
    # Horizontal
    c_bib = m_bib | o_bib
    o_hori_2 = m_bib & (m_bib >> 1) & -0x8080808080808081
    o_hori_3 = o_hori_2 & (m_bib << 1) & -0x101010101010102
    o_hori_4 = o_hori_3 & (m_bib >> 2) & -0xc0c0c0c0c0c0c0c1

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
    o_vert_2 = m_bib & (m_bib >> 8)
    o_vert_3 = o_vert_2 & (m_bib << 8)
    o_vert_4 = o_vert_3 & (m_bib >> 8)

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
    o_diagu_2 = m_bib & (m_bib >> 7) & -0x8080808080808081
    o_diagu_3 = o_diagu_2 & (m_bib << 7) & -0x101010101010102
    o_diagu_4 = o_diagu_3 & (m_bib >> 14) & -0xc0c0c0c0c0c0c0c1

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
    o_diagd_2 = m_bib & (m_bib >> 9) & -0x8080808080808081
    o_diagd_3 = o_diagd_2 & (m_bib << 9) & -0x101010101010102
    o_diagd_4 = o_diagd_3 & (m_bib >> 18) & -0xc0c0c0c0c0c0c0c1

    o, s = count_open_semi_open(o_diagd_2, c_bib, 9, 18, 0x101010101010101, 0x4040404040404040)
    o_2 += o
    s_2 += s

    o, s = count_open_semi_open(o_diagd_3, c_bib, 18, 18, 0x202020202020202, 0x4040404040404040)
    o_3 += o
    s_3 += s

    o, s = count_open_semi_open(o_diagd_4, c_bib, 18, 27, 0x202020202020202, 0x2020202020202020)
    o_4 += o
    s_4 += s

    return (s_2*sors[2]) + (o_2*ors[2]) + (s_3*sors[3]) + (o_3*ors[3]) + (s_4*sors[4]) + (o_4*ors[4])


def score(pos, mtm):  # mtm is true if i am scoring for me, if i just moved
    if mtm:
        m_bib, o_bib = pos_to_bibs(pos)
    else:
        o_bib, m_bib = pos_to_bibs(pos)
    if is_win(m_bib):
        return WIN_SCORE
    return score_bib(m_bib, o_bib) - score_bib(o_bib, m_bib)


def score_move(move, m_bib, o_bib):
    pass


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
    return False


def make_bitboards(board, col):
    m_bib = 0x0000000000000000
    o_bib = 0x0000000000000000

    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == col:
                m_bib |= 0x01 << x + y * 8
            elif board[y][x] != " ":
                o_bib |= 0x01 << x + y * 8
    return m_bib, o_bib


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


def bibs_to_pos(m_bib, o_bib):
    return (m_bib << 64) | o_bib


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
    import random
    board = make_empty_board(8)
    for i in range(10):
        board[random.randrange(0, 8)][random.randrange(0, 8)] = 'w'
        board[random.randrange(0, 8)][random.randrange(0, 8)] = 'b'
    #board[1][1] = 'w'
    #board[0][1] = 'w'
    #board[0][2] = 'w'
    print_board(board)
    m_bib, o_bib = make_bitboards(board, 'w')
    score = score_bib(m_bib, o_bib) - score_bib(o_bib, m_bib)
    print(score)
    #print_board(bib_to_board(m_bib, o_bib))
    #do_direction(None, m_bib, o_bib, 1, 0x8080808080808080, 0x101010101010101, True)
    from timeit import default_timer as timer
    start = timer()
    #scores = {}
    #for i in range(1000):
#        children = make_children(m_bib, o_bib, False, score, scores)
#        #is_win(m_bib)
#    print((timer()-start)/1000.0)
#    for child in children:
#        m_bib, o_bib = pos_to_bibs(child)
#        if scores[child] != score_bib(m_bib, o_bib) - score_bib(o_bib, m_bib):
#            print_board(pos_to_board(child))
#            print("Score:", scores[child], "vs", score_bib(m_bib, o_bib) - score_bib(o_bib, m_bib))

    start = timer()
    x = 7
    y = 5
    for i in range(1000):
        c = x << 5
    print((timer()-start)/1000.0, c)

    start = timer()
    x = 7
    y = 5
    for i in range(1000):
        c = x * (2**5)
    print((timer()-start)/1000.0, c)

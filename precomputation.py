prow_scores = {}
WIN_SCORE = 100000


def is_row_win(bib):
    return ~(bib << 1) & bib & (bib >> 1) & (bib >> 2) & (bib >> 3) & (bib >> 4) & ~(bib >> 5)


def minimax(explored, l, m_bib, o_bib, me, depth):
    c_bib = m_bib | o_bib
    if me:
        res = -2
        if is_row_win(o_bib):
            explored[m_bib << l | o_bib] = (-2, depth)
            return -1
        elif c_bib == 2**l - 1:
            explored[m_bib << l | o_bib] = (0, depth)
            return 0
        for i in range(l):
            if (0x1 << i) & ~c_bib:
                res = max(minimax(explored, l, m_bib | (0x1 << i), o_bib, False, depth + 1), res)
    else:
        res = 2
        if is_row_win(m_bib):
            explored[m_bib << l | o_bib] = (1, depth)
            return 1
        elif c_bib == 2**l - 1:
            explored[m_bib << l | o_bib] = (0, depth)
            return 0
        for i in range(l):
            if (0x1 << i) & ~c_bib:
                res = min(minimax(explored, l, m_bib, o_bib | (0x1 << i), True, depth + 1), res)

    return res


def score_row(l, m_bib, o_bib):
    c_bib = m_bib | o_bib

    explored = {}
    minimax(explored, l, m_bib, o_bib, False, 1)  # calculate score based on other player going
    if is_row_win(o_bib):
        score = -WIN_SCORE
    elif is_row_win(m_bib):
        score = WIN_SCORE
    elif c_bib == 2**l - 1:
        score = 0
    else:
        score = sum(explored[prow][0]/(explored[prow][1]**3) for prow in explored)  # best
        #score = sum(explored[prow][0]/(explored[prow][1]**3) for prow in explored)
        #score = sum(explored[row][0]/len(explored) for row in explored)  # bad
    if score != 0:
        prow_scores[1 << (2*l) | m_bib << l | o_bib] = score


def compute_rows():
    i = 0
    for l in range(5, 9):
        for m_bib in range(2**l):
            for o_bib in range(2**l):
                if not m_bib & o_bib:
                    score_row(l, m_bib, o_bib)

    print("prow_scores =", prow_scores)

if __name__ == '__main__':
    #score_row(8, 0b10000000, 0b01110000)
    #score_row(8, 0b10000000, 0b00111000)
    #score_row(8, 0b10000000, 0b00011100)
    #score_row(8, 0b00000000, 0b00011000)
    compute_rows()

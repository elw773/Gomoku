# Death:
#   immediate 5
#       0wwwwX0
#       0wwwXw0
#       0wwXww0
#       0wXwww0
#       0Xwwww0
#   open 4
#       0wwwX0
#       0wwXw0
#       0wXww0
#       0Xwww0
#       bww0wX0wwb
#       bww0Xw0wwb
#       bwww0X0wwwb
# Forcing:
#   simple 4
#       bwwwX0
#       0Xwwwb
#       ww0Xw  # edges cannot be w
#       wwX0w
#       wX0ww
#       w0Xww
#   open 3
#       00wwX00
#       00wXw00
#       00Xww00
#       0w0wX0w0
#       0w0Xw0w0
#       w0w0X0w0w
#   broken 3
#       0w0Xw0
#       0wX0w0
#       b0wwX00
#       b0wXw00
#       00Xww0b
#       00wXw0b
def is_row_win(bib):
    return ~(bib << 1) & bib & (bib >> 1) & (bib >> 2) & (bib >> 3) & (bib >> 4) & ~(bib >> 5)


def minimax(explored, l, m_bib, o_bib, me, depth):
    c_bib = m_bib | o_bib
    if me:
        res = -2
        if is_row_win(o_bib):
            explored[m_bib << l | o_bib] = -1
            return -1
        elif c_bib == 2**l - 1:
            explored[m_bib << l | o_bib] = 0
            return 0
        for i in range(l):
            if (0x1 << i) & ~c_bib:
                res = max(minimax(explored, l, m_bib | (0x1 << i), o_bib, False, depth - 1), res)
    else:
        res = 2
        if is_row_win(m_bib):
            explored[m_bib << l | o_bib] = 1
            return 1
        elif c_bib == 2**l - 1:
            explored[m_bib << l | o_bib] = 0
            return 0
        for i in range(l):
            if (0x1 << i) & ~c_bib:
                res = min(minimax(explored, l, m_bib, o_bib | (0x1 << i), True, depth - 1), res)

    return res


wins = {5: {}, 6: {}, 7: {}, 8: {}}  # value is the position to move to
forces = {5: {}, 6: {}, 7: {}, 8: {}}
scores = {5: {}, 6: {}, 7: {}, 8: {}}  # score is computed if i am about to move


def score_row(l, m_bib, o_bib):
    c_bib = m_bib | o_bib
    win = False
    explored = {}
    for i in range(l):
        if (0x1 << i) & ~c_bib:
            res = minimax(explored, l, m_bib | (0x1 << i), o_bib, False, 0)
            if res == 1:
                win = True
                if m_bib << l | o_bib in wins[l]:
                    wins[l][m_bib << l | o_bib].add(i)
                else:
                    wins[l][m_bib << l | o_bib] = {i}
    if not win:
        for i in range(l):
            if (0x1 << i) & ~c_bib:
                if minimax(explored, l, (m_bib | (0x1 << i)), o_bib, True, 0) == 1:
                    if m_bib << l | o_bib in forces[l]:
                        forces[l][m_bib << l | o_bib].add(i)
                    else:
                        forces[l][m_bib << l | o_bib] = {i}
    explored = {}
    minimax(explored, l, m_bib, o_bib, False, 0)  # calculate score based on other player going
    #if win:
    #    score = 1000
    if is_row_win(o_bib):
        score = -100
    elif is_row_win(m_bib):
        score = 100
    elif c_bib == 2**l - 1:
        score = 0
    else:
        score = sum(explored[row]/len(explored) for row in explored)
    if score != 0:
        scores[l][m_bib << l | o_bib] = score


def compute_rows():
    i = 0
    for l in range(5, 9):
        for m_bib in range(2**l):
            for o_bib in range(2**l):
                if not m_bib & o_bib:
                    #print(bin(m_bib << l | o_bib))
                    score = score_row(l, m_bib, o_bib)
                    i += 1

    for l in range(5, 9):
        for prow in scores[l]:
            if scores[l][prow] == 1:
                scores[l][prow] = 1000
            elif scores[l][prow] == -1:
                scores[l][prow] = -1000

    print("wins =", wins)
    print("forces =", forces)
    print("scores =", scores)

if __name__ == '__main__':
    compute_rows()

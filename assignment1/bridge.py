

def pairs(group):
    players = list(group)
    for i in range(len(players)):
        for j in range(i+1, len(players)):
            yield {players[i], players[j]}

def make_move(left, right, total_time, moving_right, message):
    if not left:
        print(message)
        print("====================================")
        print("Total Time: {} min".format(total_time))
        print("====================================")
        return
    if moving_right:
        for mv_right in pairs(left):
            make_move(
                left - mv_right, 
                right | mv_right, 
                total_time + max(mv_right), 
                False,
                message + "{} moved right\n\t{} | {}\n".format(
                    mv_right, left, right)
            )
    else:
        for p in right:
            mv_left = {p}
            make_move(
                left | mv_left, 
                right - mv_left, 
                total_time + max(mv_left), 
                True,
                message + "{} moved left\n\t{} | {}\n".format(
                    mv_left, left, right)
            )
        

def main():
    players = {1,2,7,10} # const
    make_move(players, set(), 0, True, "")
if __name__ == '__main__':
    main()
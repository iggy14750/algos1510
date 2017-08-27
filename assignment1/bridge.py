

def pairs(group):
    players = list(group)
    for i in range(len(players)):
        for j in range(i+1, len(players)):
            yield {players[i], players[j]}

def make_move(left, right, total_time, moving_right, message):
    if not left: # If there is no one on the left of the bridge...
        print(message, end = '') # Display the resuls from this configuration.
        print("====================================")
        print("Total Time: {} min".format(total_time))
        print("====================================\n")
        return
    if moving_right:
        for mv_right in pairs(left): # For all pairs which can cross from left...
            next_left = left - mv_right # These people will not be on left side,
            next_right = right | mv_right # ...but they will be on the right side.
            next_time = total_time + max(mv_right) # The time taken will increase.
            next_message = message + "{} moved right\n\t{} | {}\n".format(
                mv_right, left, right) # Record the move.
            make_move(next_left, next_right, next_time, False, next_message) # Make next move.
    else:
        for p in right:   # Choose one person to cross back.
            mv_left = {p} # Make a party out of them.
            next_left = left | mv_left
            next_right = right - mv_left
            next_time = total_time + max(mv_left)
            next_message = message + "{} moved left\n\t{} | {}\n".format(
                mv_left, left, right)
            make_move(next_left, next_right, next_time, True, next_message)
        

def main():
    players = {1,2,7,10} # const
    make_move(players, set(), 0, True, "")
if __name__ == '__main__':
    main()
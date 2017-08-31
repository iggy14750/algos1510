import random

MIN_NO_WORDS = 4
MAX_NO_WORDS = 16
MIN_WORD_LEN = 1
MAX_WORD_LEN = 5
LINE_LEN = 5
BIG_NUM = 1000000000000000000000

def next_case():
    n = random.randint(4, 16)
    res = []
    for _ in range(n):
        res.append(random.randint(MIN_WORD_LEN, MAX_WORD_LEN))
    return res
    
def next_config(x):
    # Input: a list<list<int>> where each list 
    # represents a line break.
    # Output: list<list<int>> which has moved to
    # the next binary number of line breaks.
    # Ex: 00101 -> 00110
    for i in reversed(range(len(x))):
        if len(x[i]) > 1:
            elem = x[i].pop()
            try:
                x[i+1].insert(0, elem)
            except:
                x.append([elem])
            while len(x) > i+2:
                stuff = x.pop(i+2)
                for s in stuff:
                    x[i+1].append(s)
            return x
            
def evaluate(case):
    summed = map(sum, case)
    error = 0
    for line in summed:
        if line > LINE_LEN:
            return BIG_NUM
        error += LINE_LEN - line
    return error
            
def opt(i):
    # Imagine a hole for a line break in between
    # every word. The exaustive solution is to 
    # toggle all combinations of these line breaks.
    # If a configuration is impossible, skip over it.
    n = len(i)
    case = [i.copy()]
    best = BIG_NUM
    while len(case) != n:
        next_config(case)
        error = evaluate(case)
        if error < best:
            best = error
    return best
    

def A(i):
    lines = [0]
    for word in i:
        if lines[-1] + word <= LINE_LEN:
            lines[-1] += word
        else:
            lines.append(word)
    return sum(map(lambda x: LINE_LEN - x, lines))
        
def main(num):
    for _ in range(num):
        x = next_case()
        if opt(x) < A(x):
            print(x)
        elif opt(x) > A(x):
            print("Hey, Opt is not optimal!!")
            print(x)

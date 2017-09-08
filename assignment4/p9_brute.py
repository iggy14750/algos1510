
from random import randint

MIN = 0
MAX = 32
LEN = 4

class better_list(list):
    def __sub__(self, index):
        other = better_list(self.copy())
        del other[index]
        return other

def permutations(x):
    # generator which produces all 
    # permutations of the input list
    def __gen__(partial, allowed):
        if len(partial) == len(x):
            yield partial
        for i, elem in enumerate(allowed):
            yield from __gen__(partial + [elem], allowed - i)
    yield from __gen__([], better_list(x))

def total_difference(one, two):
    if len(one) != len(two):
        raise KeyError
    total = 0
    for i in range(len(one)):
        total += abs(one[i] - two[i])
    return total

def gen_list(n):
    res = [0]*n
    for i in range(n):
        res[i] = randint(MIN, MAX)
    return res

class Result:
    def __init__(self, p, s):
        self.s = s
        self.p = p
        self.diff = total_difference(p, s)
    def __str__(self):
        return "{} {} | {}".format(self.p, self.s, self.diff)
    def __lt__(self, other):
        return self.diff < other.diff

def optimal(p, s):
    best = Result(p, s)
    for ski in permutations(s):
        temp = Result(p, ski)
        if temp < best:
            best = temp
    return best

def sorter(p, s):
    p = sorted(p)
    s = sorted(s)
    return Result(p, s)

def best_pair(p, s):
    # returns a tuple of indicies
    # representing the best pair from p and s
    best_p = 0
    best_s = 0
    for i, person in enumerate(p):
        for j, ski in enumerate(s):
            if abs(person - ski) < abs(p[best_p] - s[best_s]):
                best_p = i
                best_s = j
    return (best_p, best_s)

def picker(p, s):
    s = s.copy()
    p = p.copy()
    better_s = []
    better_p = []
    while s:
        pi, si = best_pair(p, s)
        better_s.append(s.pop(si))
        better_p.append(p.pop(pi))
    return Result(better_p, better_s)

def main(num_cases):
    for _ in range(num_cases):
        p = gen_list(LEN)
        s = gen_list(LEN)
        
        print("opt: " + str(optimal(p, s)))
        print("pck: " + str(picker(p, s)))
        print("srt: " + str(sorter(p, s)))
        print("===========================================\n")

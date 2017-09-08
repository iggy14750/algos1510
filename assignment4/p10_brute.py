
MAX_RELEASE = 2
MIN_LENGTH = 4
MAX_LENGTH = 16

class Job:
    def __init__(self, r, x):
        self.release = r
        self.length = x
        self.time_run = 0
    def __len__(self):
        return self.length
    def time_left():
        return self.length - self.time_run
    def run():
        self.time_run += 1
    def __str__(self):
        return "{} | {} | {} | {}".format(
            self.release,
            self.length,
            self.time_run,
            self.time_left()
        )

def pick_sjf(jobs):
    best = jobs[0]
    for j in jobs:
        if len(j) < len(best):
            best = j
    return best

def pick_srpt(jobs):
    # jobs: list<Job>
    best = jobs[0]
    for j in jobs:
        if j.time_left() < best.time_left():
            best = j
    return best

from random import randint
def gen_jobs(num):
    jobs = []
    for _ in range(num):
        jobs.append(Job(
            randint(0, MAX_RELEASE),
            randint(MIN_LENGTH, MAX_LENGTH)))
    return jobs

def get_runnable(jobs, t):
    r = []
    for j in jobs:
        if j.release <= t:
            r.append(j)
    return r

def main(num_jobs):
    jobs = gen_jobs(num_jobs)
    check_done = lambda jobs: (filter(lambda x: (x.time_left() > 0), jobs))
    t = 0
    while jobs:
        runnable = get_runnable(jobs, t)
        jobs = check_done(jobs)
        if runnable:
            smallest_job = pick_sjf(runnable)
            least_time = pick_srpt(runnable)
            smallest_job.run()
            least_time.run()
            print("release | length | time_run | time_left ")
            print(smallest_job)
            print(least_time)
            print("======================================\n")
        else:
            print("None runnable\n")
        t += 1
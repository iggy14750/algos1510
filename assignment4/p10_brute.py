
MAX_RELEASE = 12
MIN_LENGTH = 4
MAX_LENGTH = 100
NUM_JOBS = 16
LOG_FILE = 'jobs.log'

def deep_copy(jobs):
    other = []
    for j in jobs:
        other.append(Job(j.release, j.length))
    return other

class logger:
    def __init__(self, name):
        self.f = open(name, 'w')
        self.message = []
    def write(self, s):
        self.message.append(s)
    def close(self, write = False):
        if write:
            for m in self.message:
                self.f.write(m + "\n")
        self.f.close()

def main(num_jobs):
    log = logger(LOG_FILE)
    jobs_sm = gen_jobs(num_jobs)
    jobs_ls = deep_copy(jobs_sm)
    
    # I want to see what I started with.
    print("==============================================")
    print("=============== BEGINNING JOBS ===============")
    print("==============================================")
    print("release | length | time_run | time_left ")
    # print("Smallest Job First:")
    for j in jobs_sm:
        print(j)
    # print("Smallest Remaining Processing Time:")
    # for j in jobs_ls:
    #     print(j)
    print("==============================================\n")


    log.write("==============================================")
    log.write("=============== BEGINNING JOBS ===============")
    log.write("==============================================")
    log.write("release | length | time_run | time_left ")
    # log.write("Smallest Job First:")
    for j in jobs_sm:
        log.write(str(j))
    # log.write("Smallest Remaining Processing Time:")
    # for j in jobs_ls:
    #     log.write(str(j))
    log.write("==============================================\n")

    small_time = 0
    least_time = 0
    t = 0
    while jobs_sm or jobs_ls:
        if not jobs_sm:
            print("Small won!\n")
            log.write("Small won!\n")
        else:
            small_time += 1
        if not jobs_ls:
            print("Least won!\n")
            log.write("Least won!\n")
        else:
            least_time += 1
        runnable_sm = get_runnable(jobs_sm, t)
        runnable_ls = get_runnable(jobs_ls, t)
        log.write("release | length | time_run | time_left ")
        if runnable_sm:
            job = pick_sjf(runnable_sm)
            job.run()
            log.write(str(job))
        if runnable_ls:
            job = pick_srpt(runnable_ls)
            job.run()
            log.write(str(job))
        log.write("======================================\n")
        t += 1
        jobs_sm = check_done(jobs_sm)
        jobs_ls = check_done(jobs_ls)
    print("==============================================")
    print("=================== REPORT ===================")
    print("==============================================")
    print("Smallest Job First: {}".format(small_time))
    print("Samllest Remaining Processing Time: {}".format(least_time))
    log.write("==============================================")
    log.write("=================== REPORT ===================")
    log.write("==============================================")
    log.write("Smallest Job First: {}".format(small_time))
    log.write("Samllest Remaining Processing Time: {}".format(least_time))
    log.close(write = True)#small_time != least_time)

class Job:
    def __init__(self, r, x):
        self.release = r
        self.length = x
        self.time_run = 0
    def __len__(self):
        return self.length
    def time_left(self):
        return self.length - self.time_run
    def run(self):
        self.time_run += 1
    def __repr__(self):
        return str(self)
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

def check_done(jobs):
    nd = []
    for j in jobs:
        if j.time_left() > 0:
            nd.append(j)
    return nd

if __name__ == '__main__':
    main(NUM_JOBS)
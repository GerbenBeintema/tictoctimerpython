import time

class Tictoctimer(object):
    '''A simple object to measure time used in a program in a user defined way:

    Usage:
    t = Tictoctimer()
    t.start()
    t.tic('part1')
    time.sleep(1)
    t.toc('part1')
    t.tic('part2')
    time.sleep(2)
    t.toc('part2')
    t.pause()
    print(t.percent()) #prints an overview like: part1 33.5%, part2 66.5%, others 0.0%
    '''
    def __init__(self):
        self.time_acc = 0
        self.timer_running = False
        self.start_times = dict()
        self.acc_times = dict()

    @property
    def time_elapsed(self):
        if self.timer_running:
            return self.time_acc + time.time() - self.start_t
        else:
            return self.time_acc
    
    def start(self):
        self.timer_running = True
        self.start_t = time.time()
        
    def pause(self):
        self.time_acc += time.time() - self.start_t
        self.timer_running = False
    
    def tic(self,name):
        self.start_times[name] = time.time()
    
    def toc(self,name):
        if self.acc_times.get(name) is None:
            self.acc_times[name] = time.time() - self.start_times[name]
        else:
            self.acc_times[name] += time.time() - self.start_times[name]

    def percent(self):
        elapsed = self.time_elapsed
        R = sum([item for key,item in self.acc_times.items()])
        return ', '.join([key + f' {item/elapsed:.1%}' for key,item in self.acc_times.items()]) +\
                f', others {1-R/elapsed:.1%}'
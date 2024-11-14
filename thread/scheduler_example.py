import sched
import time
import threading

def loop(sch: sched.scheduler, delay:int):
    print("loop.", threading.current_thread())
    sch.enter(delay=delay,priority=0,action=loop,argument=(sch,delay))


if __name__ == "__main__":
    s = sched.scheduler()
    s.enter(delay=5, priority=0,action=loop,argument=(s, 5))
    s.run()
    time.sleep(30)




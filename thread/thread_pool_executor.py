from concurrent.futures import ThreadPoolExecutor, Future
import time
import threading


def run():
    print("before sleep.", threading.current_thread().name)
    time.sleep(5)
    print("after sleep.", threading.current_thread().name)
    return threading.current_thread().name


def example_01():
    f: Future
    with ThreadPoolExecutor(thread_name_prefix="simple-thread", max_workers=5) as executor:
        f = executor.submit(run)
    if f is not None:
        try:
            print(f.result(timeout=3))
            print("finish result.", threading.current_thread().name)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    example_01()

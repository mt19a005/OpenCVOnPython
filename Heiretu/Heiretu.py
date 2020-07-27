# main.py
import concurrent.futures as confu
import time
import asd

# クラス変数出力
def printing():
    while 1:
        time.sleep(1)
        with asd.dsa.a.get_lock():
            print("printing = ", asd.dsa.a.value)
            # print(asd.dsa.a.get_lock())

# クラス変数変更
def task():
    with asd.dsa.a.get_lock():
        asd.dsa.a.value += 1
        print("task = ", asd.dsa.a.value)


def initializer(x):
    asd.dsa.a = x


def main():
    # -   -   -   -   処理開始    -   -   -   - #
    with confu.ProcessPoolExecutor(
        initializer=initializer, initargs=(asd.dsa.a,), 
        max_workers=2
    ) as executor:
        executor.submit(printing)
        for i in range(50):
            executor.submit(task)
            time.sleep(3)

    # -   -   -   -   並列処理が終わった後    -   -   -   - #
    # print(asd.dsa.a)


if __name__ == "__main__":
    main()
import math


#V1
"""
iを１づつ増やし照合する。
{num % i, i++}
"""
def is_prime_v1(num: int) -> bool:
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


#V2
"""
素数の照合を√iまでにする。
{num % √i, i++}
"""
def is_prime_v2(num: int) -> bool:
    if num <= 1:
        return False

    for i in range(2, math.floor(math.sqrt(num) + 1)):
        if num % i == 0:
            return False

    # math関数を使わず行う場合
    # i = 2
    # while i * i <= num:
    #     if num % i == 0:
    #         return False
    #     i += 1 

    return True


#V3
"""
2の倍数(偶数)をあらかじめ照合対象から除く。
{num % 2, False}
"""
def is_prime_v3(num: int) -> bool:
    if num <= 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False


    for i in range(3, math.floor(math.sqrt(num) + 1), 2):
        if num % i == 0:
            return False

    # math関数を使わず行う場合
    # i = 3
    # while i * i <= num:
    #     if num % i == 0:
    #         return False
    #     i += 2 

    return True


#V4
"""
素数は 6k ± 1(k ≥ 6)かつ 6k ± 1 ≤ √n で割り切れないものである。
{num % 6√num ± 1, num + 6}
"""
def is_prime_v4(num: int) -> bool:
    if num <= 1:
        return False

    if num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False


    for i in range(5, math.floor(math.sqrt(num) + 1), 6):
        if num % i == 0 or num % (i+2) == 0:
            return False
    
    # 中央値(6)を取り±1を取るバージョン
    # for i in range(6, math.floor(math.sqrt(num) + 1), 6):
    #     if num % (i-1) == 0 or num % (i+1) == 0:
    #         return False

    # math関数を使わず行う場合
    # i = 5
    # while i * i <= num:
    #     if num % i == 0 or num % (i+2) == 0:
    #         return False
    #     i += 6 

    return True



if __name__ == '__main__':
    import time
    import random

    numbers = [random.randint(0, 1000) for _ in range(100000)]

    start = time.time()
    for num in numbers:
        is_prime_v1(num)
    print('v1', time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v2(num)
    print('v2', time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v3(num)
    print('v3', time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v4(num)
    print('v4', time.time() - start)
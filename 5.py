import hashlib
import time

start_time = time.time()
hexdigest = '99d34ef0758574e8b62f31fb250d0cef'
for i in range(0, 100000):
    hash = hashlib.md5(str(i).encode()).hexdigest()
    if hash == hexdigest:
        print('Хеш найден!')
        print('Значение:', str(i))
        print('Время:', time.time() - start_time)

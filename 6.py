import hashlib
import time

start_time = time.time()
hexdigest = 'd7be17ff5d777d13391ddbd9b15ed6f5'
for i in range(0, 1000000):
    hash = hashlib.md5(str(i).encode()).hexdigest()
    if hash == hexdigest:
        print('Хеш найден!')
        print('Значение:', str(i))
        print('Время:', time.time() - start_time)

import hashlib
import time

start_time = time.time()
hexdigest = '1a6562590ef19d1045d06c4055742d38288e9e6dcd71ccde5cee80f1d5a774eb'
for i in range(0, 100):
    hash = hashlib.sha256(str(i).encode()).hexdigest()
    if hash == hexdigest:
        print('Хеш найден!')
        print('Значение:', str(i))
        print('Время:', time.time() - start_time)

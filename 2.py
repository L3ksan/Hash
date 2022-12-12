import hashlib
import time

start_time = time.time()
hexdigest = 'b543b2a3edcc48cc0f9d7159522673384b34fbce51920d75df4d0c184dd89b18'
for i in range(0, 1000):
    hash = hashlib.sha256(str(i).encode()).hexdigest()
    if hash == hexdigest:
        print('Хеш найден!')
        print('Значение:', str(i))
        print('Время:', time.time() - start_time)

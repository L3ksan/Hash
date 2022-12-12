import hashlib
import time

start_time = time.time()
hexdigest = '28568ee9ca159d43e5ac8868907c2f7e05398258b6e459ade680d5e9aaf4c38d'
for i in range(0, 10000):
    hash = hashlib.sha256(str(i).encode()).hexdigest()
    if hash == hexdigest:
        print('Хеш найден!')
        print('Значение:', str(i))
        print('Время:', time.time() - start_time)

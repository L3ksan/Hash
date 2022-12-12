import hashlib
import time

start_time = time.time()
hexdigest = '5ba44691fa3aa75abc12ea51186f37f9c6a249636930d66fb065ce20f3b97a588167f9b3cbeee76f492f64bb9fe50c200cb548209382e0d00d283735ec89a792'
for i in range(0, 100000):
    hash = hashlib.sha512(str(i).encode()).hexdigest()
    if hash == hexdigest:
        print('Хеш найден!')
        print('Значение:', str(i))
        print('Время:', time.time() - start_time)

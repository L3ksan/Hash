import hashlib
import time
import os

time_start = time.time()
hash_to_find = 'c40fecd8bfc8869e3b8a43ee78c0c98a4a974c7e'
hash_value = ''
for i in range(520000, 1000000):
    print('Время:', time.time() - time_start)
    print('Значение:', str(i))
    hash = hashlib.sha1(str(i).encode()).hexdigest()
    if hash == hash_to_find:
        hash_value = str(i)
        break
    os.system('CLS')
os.system('CLS')
print('Хеш найден!')
print('Значение:', hash_value)
print('Время:', time.time() - time_start)
input('Нажмите Enter для завершения программы')

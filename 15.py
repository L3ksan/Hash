import hashlib
import time
import os

start_time = time.time()
hexdigest = '768cbabf1566ab3f64976c46749dbde67aad329ea8109d1d8277c4fd15b2c486a1a0b1d68b043b9340fafa66cbac09cb48f96798abffcecb40ab3bed6e27e695'
alphabet = '01234MNOWXYZ'
hash_value = ''
find = False
for c1 in alphabet:
    if find == True: break
    for c2 in alphabet:
        if find == True: break
        for c3 in alphabet:
            if find == True: break
            for c4 in alphabet:
                if find == True: break
                for c5 in alphabet:
                    if find == True: break
                    for c6 in alphabet:
                        if find == True: break
                        for c7 in alphabet:
                            if find == True: break
                            for c8 in alphabet:
                                if find == True: break
                                for c9 in alphabet:
                                    if find == True: break
                                    for c10 in alphabet:
                                        not_hashed = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10

                                        hash = hashlib.sha512(str(not_hashed).encode()).hexdigest()
                                        if hash == hexdigest:
                                            hash_value = str(not_hashed)
                                            find = True
                                            break
                                        # os.system('CLS')
    print('15. Hash finding:', hexdigest)
    print('Time:', time.time() - start_time)
    print('Value:', not_hashed)
os.system('CLS')
print('Hash found')
print('Time:', time.time() - start_time)
print('Value:', hash_value)
f = open('ex15.txt', 'w')
f.write('Time:' + str(time.time() - start_time) + '\n')
f.write('Value:' + hash_value + '\n')
f.close()
input('Нажмите Enter для завершения программы')

import shlex
fio = input("FIO > " )
place = input("place > " )
print(shlex.join(["register", fio, place]))

from multiprocessing import Pool
from hashlib import sha256

def boil_eggs(i):
    sha256(b'Just something...' * 100_000_000)
    print(f"Boiling eggs {i}...")
    return i

print(Pool().map(boil_eggs, [0, 1, 2]))

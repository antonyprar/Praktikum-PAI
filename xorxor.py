# xorxor.py
def bxor(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

k1 = bytes.fromhex("3c3f0193af37d2ebbc50cc6b91d27cf61197")
k21 = bytes.fromhex("ff76edcad455b6881b92f726987cbf30c68c")
k23 = bytes.fromhex("611568312c102d4d921f26199d39fe973118")
k1234 = bytes.fromhex("91ec5a6fa8a12f908f161850c591459c3887")
f45 = bytes.fromhex("0269dd12fe3435ea63f63aef17f8362cdba8")

KEY1 = k1
KEY2 = bxor(k21, KEY1)
KEY3 = bxor(k23, KEY2)
KEY4 = bxor(k1234, bxor(KEY1, bxor(KEY3, KEY2)))

inter = bxor(f45, KEY4)

prefix = b"cry{"
KEY5_4 = bxor(inter[:4], prefix)

rep = (KEY5_4 * ((len(inter) // len(KEY5_4)) + 1))[:len(inter)]
flag = bxor(inter, rep)

print("KEY5 (4 bytes hex):", KEY5_4.hex())

try:
    print("Recovered FLAG:", flag.decode())
except Exception:
    print("FLAG (hex):", flag.hex())

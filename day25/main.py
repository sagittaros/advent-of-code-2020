import itertools as it

# cardkey = 5764801
# doorkey = 17807724
cardkey = 5099500
doorkey = 7648211
subject = 7


def transform(val, sub):
    val *= sub
    return val % 20201227


def guess(m):
    val = 1
    for i in it.count(start=1):
        val = transform(val, subject)
        if val == m:
            return i


cn = guess(cardkey)
dn = guess(doorkey)
assert cn
assert dn

v = 1
for _ in range(dn):
    v = transform(v, cardkey)

print(v)

v = 1
for _ in range(cn):
    v = transform(v, doorkey)

print(v)

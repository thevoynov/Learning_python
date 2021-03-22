i = 5

while i <= 15:
    print(i)
    i = i + 2

for i in range(5):
    print(i)

for b in [0, 1, 2, 3, 4]:
    print(b)

a_dict = {"one": 1, "two": 2, "three": 3}
keys = sorted(a_dict.keys())
for key in a_dict:
    print(key)
for key in keys:
    print(key)
import sys
names = []
sys.getrefcount(names)
print(sys.getrefcount(names))
import keyword
print(keyword.kwlist)
help()
# Data Tipleri
# Text Type
x = "Salam men Axudov Babacan"
print(x)
print(type(x))

# Numeratic Type (int)
y = 31
print(y)
print(type(y))

# Numeratic Type (float)
z = 4.5
print(z)
print(type(z))

#Complex
a = 8j
print(a)
print(type(a))

# Ardicilliqlar (list)
e = ["kivi","armud","nar"]
print(e)
print(type(e))

# Ardicilliqlar (tuple)
r = ["kivi","armud","nar"]
print(r)
print(type(r))

# # range
t = range(12)
print(t)
print(type(t))

# bool
d = True
print(d)
print(type(d))

# Global Deyisen
w = "Axundov"
def myFunc():
    w = "Babacan"
    print("Menim adim " + w)
myFunc()
print("Menim adim " + w)

# Operatorlar (Riyazi Operatorlar)

n = 9
m = 2

print(n + m)
print(n - m)
print(n * m)
print(n / m)
print(n % m)
print(n ** m)
print(n // m)

# Operatorlar (Teyinat Operatorlar)
f = 5
print(f)
f += 5
print(f)
f -= 5
print(f)
f *= 5
print(f)
f /= 5
print(f)
f %= 2
print(f)
f //= 5
print(f)
f **= 5
print(f)

# Operatorlar (Muqayise Operatorlar)
u = 73
i = 68
print(u == i)
print(u != i)
print(u > i)
print(u < i)
print(u <= i)
print(u >= i)

# Operatorlar (Mentiqi Operatorlar)
s = 8
print(s > 7 and s < 9)
print(s > 6 or s > 220)
print(not(s > 6 or s > 220))

# Sert Operatoru (if else)
g = 73
h = 34
if g > h:
  print("g boyukdur h-dan")
elif g == h:
  print("g ve h beraberdir")
else:
  print("g kicikdir -dan")
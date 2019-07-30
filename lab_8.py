print("*")
print("*")
print("*")
print("*")
print("*")

c1 = "@"
c2 = "$"
def stars(n,c):
    print(c * n)
    return ""
print(stars(5,"*"))
print(stars(9,"&"))
print(stars(15,"%"))
print(stars(21,c1))
print(stars(6,c2))

def rec(a,b,c):
    for st in range(a):
        stars(b,c)
    return ""

print(rec(2,11,"^"))

def special_draw_2d(n, m, border, fill):
    print(m* border)
    for fl in range(n-2):
        print(border + fill*(m-2) + border)
    print(m* border)
    return " "

print(special_draw_2d(32, 7, "!", "@"))
print(special_draw_2d(12, 22, "0", "^"))

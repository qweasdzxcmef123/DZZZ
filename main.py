a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
cord1 = max(a1, a2)**2 - min(a1, a2)**2
cord2 = max(b1, b2)**2 - min(b1, b2)**2
cord3 = max(c1, c2)**2 - min(c1, c2)**2
cord4 = (cord1 + cord2 + cord3)**0.5
print(cord4)
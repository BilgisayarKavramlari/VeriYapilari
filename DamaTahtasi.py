# Dama tahtası kodlaması

n = int(input("Dama tahtasının kenar uzunluğu kaç olsun?: "))
print()

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()

# OUTPUT:
Dama tahtasının kenar uzunluğu kaç olsun?: 5

0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 

# OUTPUT2:
Dama tahtasının kenar uzunluğu kaç olsun?: 8

0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 

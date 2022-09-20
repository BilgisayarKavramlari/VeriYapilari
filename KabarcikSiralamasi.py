numberList = [2, 3, 6, 3, 4, 1, 9, 8, 2, 6]

print("Liste:", numberList)
print()

n = len(numberList)

for i in range(n-1):
    sort_flag = True
    
    for j in range(n-1, i, -1):
        if numberList[j-1] > numberList[j]:
            sort_flag = False
            
            temp = numberList[j-1]
            numberList[j-1] = numberList[j]
            numberList[j] = temp
    
    if sort_flag:
        break

print("Sıralanmış liste:", numberList)

"""
OUTPUT:

Liste: [2, 3, 6, 3, 4, 1, 9, 8, 2, 6]

Sıralanmış liste: [1, 2, 2, 3, 3, 4, 6, 6, 8, 9]
"""

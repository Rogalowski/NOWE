
# [08:18] Karol Kołodziejczyk - Trener
#     Napiszcie funkcję, która za pomocą rekursji (NIE PĘTLI), wyświetli wszystkie liczby parzyste, mniejsze niż 20.
 
# def even(x):
#     if x % 2 == 0 and x >= 0:
#         print(x)
#     elif x < 0:
#         return x
#     return even(x-1)

# even(20)

# def even(x):
#     if x > 0:
#         print(x)
#     else:
#         return x
#     even(x-2)

# even(20)

def even(x):
    if x > 0:
        print(x)
        even(x-2)

even(20)
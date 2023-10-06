# Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
# return eden fonksiyon yazınız.

l = [2, 13, 18, 93, 22]

def even_or_odd(l):
    even_list=[]
    odd_list=[]
    for nums in l:
        if nums % 2 == 0:
            even_list.append(nums)
        else:
            odd_list.append(nums)

    return even_list, odd_list

even_list, odd_list = even_or_odd(l)
print(even_list)
print(odd_list)
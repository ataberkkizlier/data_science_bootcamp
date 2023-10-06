# Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer
# kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python","miuul"])

def fark(kume1, kume2):
    if kume1.issuperset(kume2):
        return kume1.intersection(kume2)
    else:
        return kume2.difference(kume1)


print(fark(kume1, kume2))
# Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime
# ayırınız.

text = "The goal is to turn data into information, and information into insight."

# Tüm harfleri büyült.
text = text.upper()

# Virgül ve nokta yerine space koy.
text = text.replace(",", " ").replace(".", " ")

# Kelimeleri ayır
words = text.split()

# Print
print(words)
# Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer
# almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

#for ders_bilgileri in zip(ders_kodu, kredi, kontenjan):
 # if ders_bilgileri[1] == 3:
  #  print(f"Kredisi {ders_bilgileri[1]} olan {ders_bilgileri[0]} kodlu dersin kontenjani {ders_bilgileri[2]} kisidir.")
  #elif ders_bilgileri[1] == 4:
   # print(f"Kredisi {ders_bilgileri[1]} olan {ders_bilgileri[0]} kodlu dersin kontenjani {ders_bilgileri[2]} kisidir.")
  #elif ders_bilgileri[1]==2:
   # print(f"Kredisi {ders_bilgileri[1]} olan {ders_bilgileri[0]} kodlu dersin kontenjani {ders_bilgileri[2]} kisidir.")
list(zip(kredi, ders_kodu, kontenjan))
for item in list(zip(kredi, ders_kodu, kontenjan)):
  print(f"Kredisi {item[0]} olan {item[1]} kodlu dersin kontenjani {item[2]} kisidir.")
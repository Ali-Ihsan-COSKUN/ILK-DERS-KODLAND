meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "AGGRO":"Agresifleşmek/sinirlenmek",
            "SHEESH":"Onaylamamak",
            "ROFL":"Bir şakaya karşılık cevap",
            "CREEPY":"Korkunç"
            }
while True :
  word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
  if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(meme_dict[word])
    print()
  else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("Sözlükte bu kelime bulunmamakta yeniden deneyiniz.")
    print()

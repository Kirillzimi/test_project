meme_dict = {
            "CRINGE": "Что-то очень странное или стыдное",
            "LOL": "Что-то очень смешное",
            "ROFL": "шутка",
            "SHISH": "одобрение или восторг",
            "KRIPOVI": "страшный, пугающий",
            "AGRITSA": "злиться"
            }

word = input("Введите непонятное слово (большими буквами!): ")
word = word.upper()

if word in meme_dict.keys():
    print(meme_dict[word])
    # Что делать, если слово нашлось?
else:
    print("Input not found")

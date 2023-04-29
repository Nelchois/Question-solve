character = input()
ani_dic = {"Pokemon": "Pikachu", "Digimon": "Agumon", "Yugioh": "Black Magician"}
print(ani_dic.get(character, "I don't know"))
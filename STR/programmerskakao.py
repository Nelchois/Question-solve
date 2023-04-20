example_line = input()
Eng_number = {"0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
for i,j in Eng_number.items():
    if j in example_line:
        example_line = example_line.replace(j,i)
print(int(example_line))

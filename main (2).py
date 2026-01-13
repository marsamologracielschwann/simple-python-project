words=("tesla","schwann","schleiden","einstein","galilie","haytham")
hints={
"tesla":"Famous inventor related to electricity",
"schwann":"Scientist who helped develop cell theory",
"schleiden":"Botanist involved in cell theory",
"einstein":"Scientist known for relativity",
"galilie":"Astronomer who supported heliocentrism",
"haytham":"A historical character name"}
art={0:("   ","   ","   "),
     1:(" o ","   ","   "),
     2:(" o "," | ","   "),
     3:(" o ","/| ","   "),
     4:(" o ","/|\\","   "),
     5:(" o ","/|\\","/  "),
     6:(" o ","/|\\","/ \\")}

print("Welcome to Hangman Word Guessing Game!")
print("Guess the word correctly. Fighting!")
for word in words:
    g,w=[],0; print("\n Hint:",hints[word])
    while True:
        for l in art[w]: print(l)
        show=" ".join(c if c in g else "_" for c in word); print("\nWord:",show)
        guess=input("Guess letter or word: ").lower()
        if len(guess)>1: w+= guess!=word
        else: g+=[guess] if guess not in g else []; w+= guess not in word
        if "_" not in show or guess==word: break
        if w==6:
            for l in art[6]: print(l)
            print(" Game Over! Word was:",word); exit()
print("\n Congrats! You've guessed all the words!")
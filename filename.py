# Hangman Word Guessing Game 

words = ("tesla", "schwann", "schleiden", "einstein", "galilie", "haytham", "mendeleev", "leary", "pasteur", "curie")

hints = {
    "tesla": "Famous inventor related to electricity",
    "schwann": "Scientist who helped develop cell theory",
    "schleiden": "Botanist involved in cell theory",
    "einstein": "Scientist known for relativity",
    "galilie": "Astronomer who supported heliocentrism",
    "haytham": "A historical character name",
    "mendeleev": "created the Periodic Table of Elements",
    "leary": "researched the effects of psychedelics on human consciousness",
    "pasteur": "discovered that microorganisms cause disease",
    "curie": "discovered radioactivity and advanced cancer treatment using radiation"
}

hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\")
}

hint_chances = 3   # 🔑 TOTAL hints allowed

print("🎮 Welcome to Hangman!")
print("You may guess ONE letter or the WHOLE word.")
print("Hints available:", hint_chances)

for secret_word in words:
    guessed_letters = []
    wrong_guesses = 0

    print("\n--- NEW WORD ---")

    while True:
        # Show hangman
        for line in hangman_art[wrong_guesses]:
            print(line)

        # Show word structure
        display_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )
        print("\nWord:", display_word)

        # Show hint structure
        if hint_chances > 0:
            print("Hint:", ", ".join("_" for _ in secret_word))
            print("Hints left:", hint_chances)
        else:
            print("Hint: ❌ No hints remaining")

        guess = input("\nEnter letter, word, or 'hint': ").lower().strip()

        # HINT LOGIC (LIMITED TO 3)
        if guess == "hint":
            if hint_chances > 0:
                print("💡 Hint:", hints[secret_word])
                hint_chances -= 1
                wrong_guesses += 1
            else:
                print("❌ No hints left!")
            continue

        # WHOLE WORD GUESS
        if len(guess) > 1:
            if guess == secret_word:
                print("🎉 Correct! Moving to next word.")
                break
            else:
                print("❌ Wrong word!")
                wrong_guesses += 1

        # LETTER GUESS
        else:
            if guess in guessed_letters:
                print("Already guessed.")
                continue

            guessed_letters.append(guess)

            if guess not in secret_word:
                print("❌ Wrong letter!")
                wrong_guesses += 1

        # Win by letters
        if all(letter in guessed_letters for letter in secret_word):
            print("🎉 You guessed the word!")
            break

        # Game over
        if wrong_guesses == 6:
            for line in hangman_art[6]:
                print(line)
            print("💀 Game Over! The word was:", secret_word)
            exit()

print("\n🏁 End of game. Thanks for playing!")

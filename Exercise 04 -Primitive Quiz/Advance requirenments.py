countries_capitals = [
    ("France", "Paris"),
    ("Germany", "Berlin"),
    ("Spain", "Madrid"),
    ("Italy", "Rome"),
    ("United Kingdom", "London"),
    ("Portugal", "Lisbon"),
    ("Netherlands", "Amsterdam"),
    ("Belgium", "Brussels"),
    ("Sweden", "Stockholm"),
    ("Poland", "Warsaw"),
]

score = 0
for country, capital in countries_capitals:
    answer = input(f"What is the capital of {country}? ").strip().lower()
    if answer == capital.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. The correct answer is {capital}.")

print(f"\nQuiz complete. You scored {score} out of {len(countries_capitals)}.")
# filepath: c:\Users\user\Documents\GitHub\Assessment1\fall-2025-code-lab-1-assignement-1-programming-skills-portfolio-Programming-Skills-Portfolio-Fall25\Exercise 04 -Primitive Quiz\quiz.py
countries_capitals = [
    ("France", "Paris"),
    ("Germany", "Berlin"),
    ("Spain", "Madrid"),
    ("Italy", "Rome"),
    ("United Kingdom", "London"),
    ("Portugal", "Lisbon"),
    ("Netherlands", "Amsterdam"),
    ("Belgium", "Brussels"),
    ("Sweden", "Stockholm"),
    ("Poland", "Warsaw"),
]

score = 0
for country, capital in countries_capitals:
    answer = input(f"What is the capital of {country}? ").strip().lower()
    if answer == capital.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. The correct answer is {capital}.")

print(f"\nQuiz complete. You scored {score} out of {len(countries_capitals)}.")
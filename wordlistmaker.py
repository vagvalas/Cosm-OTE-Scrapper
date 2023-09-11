import itertools

# Define the Greek alphabet in all caps
alphabet = ['Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω']

# Generate all possible 3-letter combinations of the Greek alphabet
combinations = itertools.product(alphabet, repeat=3)

# Convert the combinations to a list of strings
wordlist = ["".join(c) for c in combinations]

# Save the resulting wordlist to a file
with open('wordlist.txt', 'w', encoding='utf-8') as file:
    for word in wordlist:
        file.write(word + '\n')

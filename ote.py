import requests
import urllib.parse
import json
import csv
import itertools
import sys

# Define the Greek alphabet in all caps
alphabet = ['Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω']
print("Should i use ALL Greek Alphabet, or do you wanna specify your wordlist? ")

while True:
    choice_wl = input("Press A for ALL, or C for custom or Q to quit:")
    if choice_wl == "A":
        print("Using all Alphabet:")
        print(alphabet)
        # Generate all possible 3-letter combinations of the Greek alphabet
        combinations = itertools.product(alphabet, repeat=3)

        # Convert the combinations to a list of strings
        wordlist = ["".join(c) for c in combinations]
        break
    elif choice_wl == "C":
        filename = input("Enter the filename of the list of words: ")
        with open(filename, 'r', encoding='utf-8') as f:
            wordlist = [line.strip() for line in f]
        break
    elif choice_wl == "Q":
        print("Quitting the program.")
        sys.exit()
    else:
        print("Invalid option. Please try again.")

allnames = len(wordlist)

url_template = 'https://www.11888.gr/search/white_pages/?query={}&location={}&page={}'

# Prompt the user for the name of the file containing the list of words


location = input("Vale tin topothesia me tin morfi 'Kallithea, Attiki': ")


filenamecsv = input("Enter a filename for the CSV file: ")
if not filenamecsv.endswith('.csv'):
    filenamecsv += '.csv'

with open(filenamecsv, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([
        'word', 'lastname', 'firstname', 'street1', 'number1',
        'phone', 'residential', 'subregion', 'municipality',
        'postal_code', 'provider', 'detailed_url'
    ])

    for i, word in enumerate(wordlist):
        encoded_word = urllib.parse.quote(word, safe='')
        encoded_location = urllib.parse.quote(location, safe='')
        url = url_template.format(encoded_word, location, 0)
        response = requests.get(url)
        data = json.loads(response.text)

        number_of_pages = data['data']['total_pages']
        if number_of_pages == 0:
            print(round((i / allnames) * 100, 2), "% ", "skipping", i + 1, "name", word, "has no data")
            continue
        else:
            for currentpage in range(number_of_pages):
                url = url_template.format(encoded_word, location, currentpage)
                response = requests.get(url)
                data = json.loads(response.text)
                print(round((i / allnames) * 100, 2), "% ", word, 'name', i + 1, 'of', allnames, 'total of', currentpage + 1, '/', number_of_pages, 'pages')

                results = data.get('data', {}).get('results', [])
                for result in results:
                    lastname = result['name'].get('last', '')
                    firstname = result['name'].get('first', '')
                    street1 = result['address'].get('street1', '')
                    number1 = result['address'].get('number1', '')
                    postal_code = result['address'].get('postal_code', '')
                    subregion = result['address'].get('subregion', {}).get('name', '')
                    municipality = result['address'].get('municipality', {}).get('name', '')
                    detailed_url = "https://11888.gr" + result.get('detail_url', '')

                    # Get phones (first one if exists)
                    phones = result.get('phones', [])
                    phone = phones[0].get('number', '') if phones else ''
                    residential = phones[0].get('type', '') if phones else ''

                    # Get all providers
                    providers = [phone.get('provider', '') for phone in phones if 'provider' in phone]
                    providers_str = ', '.join(providers)

                    writer.writerow([
                        word, lastname, firstname, street1, number1,
                        phone, residential, subregion, municipality,
                        postal_code, providers_str, detailed_url
                    ])

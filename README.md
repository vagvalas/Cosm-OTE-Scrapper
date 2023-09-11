# Cosm-OTE-Scrapper

# About
An advanced python script for scrapping greek telephone pages.

# Uses
Whenever you walk out of a street, and you know the address but not who or which phone number is there (if you want to contact with this person for a reason)
you can scan the Green phone catalog, in the specific area, and reverse find the address you want, and then lookup if the phone is registered.

# How it developed

Ote main provider here in Greece has an open catalog with all (accepted by them to be public) phone numbers.
With a minimum of 3 letters you can fetch a list for a single area, returnig a JSON file with all infos.
Then it just request all possible combinations, (should just remove duplicates sometime), and exporting in a CSV file.

# How to use it
Just brute-force all letters in an area, and then search for the address.
If you want more specific search you can limit the search letters range, by making a wordlist using wordlistmaker.py in this repo.

# Final Thoughts
Maybe remove duplicates at the end,
and in the future to add a GUI, or/and a search feauture afterwards.
(maybe) a kill-switch when it find the address i'm looking for to stop fetching more data.

#!/usr/bin/env python3

import os
from itertools import product

# === Wordlist Wizard: Python Edition ===
# Author: Your Name
# License: MIT

OUTPUT_DIR = "output"
ROCKYOU_PATH = "/usr/share/wordlists/rockyou.txt"  # Adjust if needed

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("🧙 Welcome to Wordlist Wizard (Python Edition) 🧙")
print("Let's collect some information...")

# Collect inputs
fname = input("Enter target's first name: ").strip()
lname = input("Enter target's last name: ").strip()
keyword = input("Enter a pet name or keyword: ").strip()
number = input("Enter a favorite number or year (e.g., 1990): ").strip()
symbol = input("Enter a special symbol (e.g., !, @, $): ").strip()

# Base components
base_words = [fname, lname, keyword]
extras = [number, symbol]

# Start building combinations
candidates = set()

# Basic inputs and combos
candidates.update(base_words)
candidates.update([
    fname + lname,
    lname + fname,
    fname + number,
    lname + number,
    keyword + number,
    keyword + symbol,
    fname.capitalize() + number,
    lname.capitalize() + symbol,
    fname.lower() + lname.lower() + number,
    fname.upper() + number + symbol,
])

# Create extra combinations (fname+lname+number, etc.)
for combo in product(base_words, repeat=2):
    if combo[0] != combo[1]:
        candidates.add("".join(combo) + number)

# Ask about merging with rockyou
merge = input("Do you want to merge with rockyou.txt? (y/n): ").lower().startswith('y')
if merge:
    try:
        with open(ROCKYOU_PATH, "r", encoding="latin1") as rock:
            for line in rock:
                candidates.add(line.strip())
        print(f"✅ Merged with {ROCKYOU_PATH}")
    except FileNotFoundError:
        print("⚠️ Could not find rockyou.txt. Skipping merge.")

# Final output
final_list = sorted(set(filter(None, candidates)))
output_file = os.path.join(OUTPUT_DIR, "custom_wordlist.txt")

with open(output_file, "w") as out:
    for word in final_list:
        out.write(word + "\n")

print(f"\n✅ Wordlist saved to: {output_file}")
print(f"✅ Total entries: {len(final_list)}")

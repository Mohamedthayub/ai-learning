
from pathlib import Path
import re

filename = input("Enter the file name: ")
filePath = Path(filename)

if filePath.is_file():
    with open(filePath, 'r', encoding='utf-8') as file:
        text = file.read()

        # Count sentences
        totalSentences = re.split(r'[.!?]+(?:\s+|$)', text.strip())
        sentences = [s for s in totalSentences if s.strip()]
        sentence_count = len(sentences)

        # Count lines
        line_count = len(text.splitlines())

        # Count words
        words = text.split()
        word_count = len(words)

        # Count alphabetic characters
        letter_count = sum(1 for char in text if char.isalpha())

        print(f"Total lines      : {line_count}")
        print(f"Total sentences  : {sentence_count}")
        print(f"Total words      : {word_count}")
        print(f"Total characters : {letter_count}")

else:
    print("File does not exist")

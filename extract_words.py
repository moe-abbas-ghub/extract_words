#!/usr/bin/env python3
from collections import Counter
import string
import sys
import argparse

def most_used_words(filename, num_words=10, stopwords_file="stopwords.txt"):
  """
  This function takes a text file and returns a list of the most used words,
  excluding words listed in a stopwords file (default: stopwords.txt) and numbers.

  Args:
      filename: Path to the text file.
      num_words: Number of most used words to return (default: 10).
      stopwords_file: Path to the file containing stopwords (default: stopwords.txt).

  Returns:
      A list of tuples containing (word, count).
  """
  # Load stopwords from a separate file
  with open(stopwords_file, 'r') as f:
    stopwords = set(line.strip() for line in f)

  # Read the text file
  with open(filename, 'r') as f:
    text = f.read()

  # Preprocess text: lowercase, remove punctuation and digits, split into words
  words = [word.lower() for word in text.translate(str.maketrans('', '', string.punctuation + string.digits)).split()]

  # Filter out stopwords and numbers
  words = [word for word in words if word not in stopwords and not word.isdigit()]

  # Count word frequency
  word_counts = Counter(words)

  # Return the most common words
  return word_counts.most_common(num_words)

# Set up argument parser
parser = argparse.ArgumentParser(description='Analyze word usage in a text file.')
parser.add_argument('filename', help='Path to the text file to analyze.')
parser.add_argument('--stopwords', default="stopwords.txt", help='Path to the stopwords file (default: stopwords.txt).')
parser.add_argument('--num_words', default=10, type=int, help='Number of most used words to return (default: 10).')

# Parse arguments
args = parser.parse_args()
filename = args.filename
stopwords_file = args.stopwords
num_words = args.num_words

# Read the text file with error handling
try:
  with open(filename, 'r') as f:
    text = f.read()
  print(f"Successfully read {filename}")
except FileNotFoundError:
  print(f"Error: The file {filename} was not found.")
  sys.exit(1)
except Exception as e:
  print(f"An unexpected error occurred while reading the file: {e}")
  sys.exit(1)

# Analyze and print results
most_common = most_used_words(filename, num_words, stopwords_file)
print("Most Used Words (excluding stopwords and numbers):")
for word, count in most_common:
  print(f"{word}: {count}")

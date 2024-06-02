from collections import Counter
import string

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

# Example usage
filename = "your_text_file.txt"  # Replace with your actual filename
stopwords_file = "stopwords.txt"  # You can modify this path

most_common = most_used_words(filename, num_words=25, stopwords_file=stopwords_file)  # Adjust num_words as desired

print("Most Used Words (excluding stopwords and numbers):")
for word, count in most_common:
  print(f"{word}: {count}")

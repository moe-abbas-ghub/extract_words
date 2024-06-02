# README

## Overview
This Python script analyzes word usage in a text file. It identifies the most frequently used words, excluding stopwords (common words like "the", "a", "an") and numbers. The script takes the text file path, stopwords file path (optional), and the desired number of most used words as command-line arguments.

## Functionality
1. Reads Text File: The script opens the specified text file and reads its contents.
2. Preprocesses Text: It converts all words to lowercase, removes punctuation and digits, and splits the text into individual words.
3. Filters Stopwords: Words listed in a separate stopwords file (default: stopwords.txt) are excluded from the analysis.
4. Counts Word Frequency: The script counts the occurrences of each unique word.
5. Returns Most Used Words: It returns a list containing the most frequently used words (excluding stopwords and numbers) along with their respective counts.

## Usage
1. Save Script: Save the script as extract_words.py.
2. Run Script: Open a terminal or command prompt and navigate to the directory where you saved the script.
3. Provide Arguments: Run the script using the following command syntax, replacing <filename> with the actual path to your text file:
```
python extract_words.py <filename> [--stopwords <stopwords_file>] [--num_words <number>]
```

## Arguments:
- <filename> (required): Path to the text file you want to analyze.
- --stopwords (optional): Path to the file containing stopwords (default: stopwords.txt). You can modify this path if your stopwords are in a different location.
- --num_words (optional): Number of most used words to return (default: 10). You can adjust this value to see a different number of top words.

## Example Usage:
```
python extract_words.py your_text_file.txt --num_words=20
```
This command will analyze the file your_text_file.txt and print the 20 most used words (excluding stopwords and numbers).

## Additional Notes
The script assumes the stopwords file contains one stopword per line.
Make sure you have Python 3.7 or higher installed on your system.
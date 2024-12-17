import sys
import os
import logging
from collections import Counter

# Core libraries (assumed available in the packaged .exe)
import nltk
import customtkinter as ctk
import PyPDF2
import pypandoc
from textstat import textstat
from docx import Document
from bs4 import BeautifulSoup  # For HTML file parsing

def syllable_count(word):
    """Estimate syllable count for a word."""
    vowels = "aeiouy"
    word = word.lower()
    if word[0] in vowels:
        count = 1
    else:
        count = 0
    count += sum(1 for i in range(1, len(word)) if word[i] in vowels and word[i - 1] not in vowels)
    return count if count > 0 else 1


def read_file(file_path):
    """Read content from different file types."""
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    try:
        if ext == ".txt":
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        elif ext == ".docx":
            doc = Document(file_path)
            return "\n".join([para.text for para in doc.paragraphs])
        elif ext == ".pdf":
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                return "\n".join([page.extract_text() for page in reader.pages])
        elif ext in [".rtf", ".odt"]:
            return pypandoc.convert_file(file_path, 'plain')
        elif ext == ".html":
            with open(file_path, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'html.parser')
                return soup.get_text()
        else:
            raise ValueError(f"Unsupported file type: {ext}")
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {str(e)}")
        return f"Error reading file: {str(e)}"


def analyze_text(file_path):
    try:
        text = read_file(file_path)

        if text.startswith("Error"):
            return text

        if not text.strip():
            return "Error: The file appears to be empty or contains no readable text."

        # Clean text and tokenize
        words = nltk.word_tokenize(text.lower())
        sentences = nltk.sent_tokenize(text)

        words = [word for word in words if word.isalnum()]
        stop_words = set(nltk.corpus.stopwords.words('english'))
        filtered_words = [word for word in words if word not in stop_words]

        # Metrics
        total_words = len(words)
        distinct_words = len(set(words))
        word_frequencies = Counter(filtered_words)
        avg_word_length = sum(len(word) for word in filtered_words) / len(filtered_words) if filtered_words else 0
        avg_sentence_length = total_words / len(sentences) if sentences else 0
        total_syllables = sum(syllable_count(word) for word in words)
        lexical_density = distinct_words / total_words if total_words else 0

        # Readability Scores
        flesch_reading_ease = textstat.flesch_reading_ease(text)
        flesch_kincaid_grade = textstat.flesch_kincaid_grade(text)

        # Complexity Metrics
        sentence_lengths = [len(nltk.word_tokenize(sentence)) for sentence in sentences]
        most_common_sentence_lengths = Counter(sentence_lengths).most_common(5)

        # Punctuation Analysis
        punctuation_counts = Counter(char for char in text if char in ".,!?;:'\"")

        metadata = {
            "Total Words": total_words,
            "Distinct Words": distinct_words,
            "Lexical Density": round(lexical_density, 2),
            "Average Word Length": round(avg_word_length, 2),
            "Average Sentence Length (words)": round(avg_sentence_length, 2),
            "Total Syllables": total_syllables,
            "Flesch Reading Ease": round(flesch_reading_ease, 2),
            "Flesch-Kincaid Grade Level": round(flesch_kincaid_grade, 2),
            "Most Common Sentence Lengths": most_common_sentence_lengths,
            "Punctuation Counts": dict(punctuation_counts),
            "Top 10 Frequent Words": word_frequencies.most_common(10)
        }

        return metadata
    except Exception as e:
        logging.error(f"Error analyzing file {file_path}: {str(e)}")
        return f"Error: {str(e)}"


def export_results(metadata, output_file="analysis_results.txt"):
    """Export analysis results to a file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for key, value in metadata.items():
                file.write(f"{key}: {value}\n")
        print(f"Results exported to {output_file}")
    except Exception as e:
        logging.error(f"Error exporting results: {str(e)}")
        print(f"Error exporting results: {str(e)}")

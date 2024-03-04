from mrjob.job import MRJob
import re

class AverageRating(MRJob):
    # Parses each line of input data and extracts the product name and calculated 
    # unique word count for customer reviews. The input data is in CSV format with columns for date, 
    # rating, review, and product. This filters out the header row, splits the 
    # CSV data, and calculates the word count for review text using the get_word_count()
    # method before yielding the product name and score.
    def mapper(self, _, line):
        if line.lower().startswith('date'):  # Skip header row
            return

        # Input data is in CSV format with columns: date, rating, review, product
        data = line.strip().split('|')
        product = data[2]
        word_count = self.get_word_count(data[3])
        yield product, word_count

    def reducer(self, product, word_count):
        word_count_list = list(word_count) 
        total_word_count = sum(word_count_list)
        total_reviews = len(word_count_list)
        average_words_per_review = round(total_word_count / total_reviews) if total_reviews > 0 else 0
        yield product, average_words_per_review

    def clean_text(self, text):
        text = re.sub(r'\W', ' ', text) 
        text = re.sub(r'\s+', ' ', text)  
        text = re.sub(r'-\s*', '', text)
        return text.lower()

    def get_word_count(self, text):
        refined_text = self.clean_text(text)
        unique_words = {word:1 for word in refined_text.split(" ")}
        return len(unique_words.keys())


if __name__ == '__main__':
    AverageRating.run()

import os
import ebooklib
from ebooklib import epub
import re
import csv

# Set the path to the directory containing the books
books_dir = '/path-for-the-epubs/'

# Create a CSV file to write the text to
with open('dataset_book.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # Iterate over all the files in the books directory
    for file_name in os.listdir(books_dir):
        # Check if the file is an ePub file
        if file_name.endswith('.epub'):
            # Open the ePub file
            book = epub.read_epub(os.path.join(books_dir, file_name))

            # Iterate over all the chapters in the book
            for item in book.get_items():
                if item.get_type() == ebooklib.ITEM_DOCUMENT:
                    # Extract the text from the chapter
                    chapter = item.get_content().decode('utf-8')

                    # Remove HTML tags and other non-text content
                    chapter = re.sub('<[^<]*?>', '', chapter)
                    chapter = re.sub('\n', ' ', chapter)
                    chapter = re.sub('&#13;', '', chapter)
                    chapter = re.sub('&nbsp;', ' ', chapter)
                    chapter = re.sub('&amp;', '&', chapter)

                    # Write the text to the CSV file
                    writer.writerow([chapter])

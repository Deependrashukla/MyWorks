import pdfplumber
import re
import requests
import os
import sqlite3

# Function to download PDF from a URL
def download_pdf(url, local_path):
    response = requests.get(url)
    print("Response generated")
    with open(local_path, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded PDF from {url} to {local_path}")

# Function to extract text from the PDF
def extract_text_from_pdf(pdf_path):
    print("Extracting PDF text")
    full_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"
    return full_text


# Function to clean special characters and fix word concatenation
def clean_text(text):
    print("Cleaning text")

    # Remove all dots (single and multiple)
    text = re.sub(r'\.{1,}', '', text)
    
    # Fix concatenated words (use regex lookahead and lookbehind)
    text = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', text)  # Lowercase followed by Uppercase
    text = re.sub(r'(?<=[a-z])(?=\d)', ' ', text)    # Lowercase followed by a digit
    text = re.sub(r'(?<=[A-Z])(?=[A-Z][a-z])', ' ', text)  # Uppercase followed by Uppercase then Lowercase

    # Remove non-alphanumeric characters except for basic punctuation
    cleaned_text = re.sub(r'[^A-Za-z0-9\s,!?\']', '', text)
    
    # Replace multiple spaces with a single space
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    return cleaned_text



# Function to split the text into chunks of a specific size (e.g., 1000 words)
def split_into_chunks(text, chunk_size=1000):
    print("Splitting text into chunks")
    words = text.split()
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

# Function to store chunks in an SQLite database
def store_chunks_in_db(chunks, db_path='chunks.db'):
    print("Storing chunks in database")
    # Connect to SQLite database (or create it)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create a table to store the chunks
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book_chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chunk_index INTEGER,
            chunk_text TEXT
        )
    ''')
    
    # Insert each chunk with its index into the database
    for i, chunk in enumerate(chunks):
        cursor.execute('''
            INSERT INTO book_chunks (chunk_index, chunk_text)
            VALUES (?, ?)
        ''', (i+1, chunk))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print(f"Stored {len(chunks)} chunks in the database.")

# Example usage
pdf_url = 'https://ia903202.us.archive.org/31/items/python_ebooks_2020/deep_learning_illustrated_artificial_intelligenceNetworkArtificial.pdf'
local_pdf_path = 'temp_dlbook.pdf'

# Step 1: Download the PDF from the URL
download_pdf(pdf_url, local_pdf_path)

# Step 2: Extract text from the downloaded PDF
book_text = extract_text_from_pdf(local_pdf_path)
print("Extracted text from book")

# Step 3: Clean the extracted text
cleaned_text = clean_text(book_text)

# Step 4: Split the cleaned text into chunks
chunks = split_into_chunks(cleaned_text, chunk_size=1000)  # You can adjust chunk_size

# Step 5: Store each chunk in the SQL database
store_chunks_in_db(chunks, db_path='book_chunks.db')

# Step 6: Delete the temporary PDF file
os.remove(local_pdf_path)
print(f"Deleted temporary file {local_pdf_path}")





################################ Run to check the database #################################
import sqlite3

conn = sqlite3.connect('book_chunks.db')
cursor = conn.cursor()

# Query all chunks
cursor.execute('SELECT * FROM book_chunks')
rows = cursor.fetchall()

for row in rows:
    if row[1] == 3:
        print(f"Index: {row[1]}, Text: {row[2][:500]}")  # Print the first 100 characters of each chunk

conn.close()

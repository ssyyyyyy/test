# I will now adjust the Python code to handle the new requirements:
# 1. Each name is separated by a comma.
# 2. The output format should be "Lastname,Firstname..........page1,page2"

# First, let's read the content of the new document
with open(r"C:\Users\Administrator\Desktop\doc.txt", "r", encoding="gbk") as file:
    doc_content = file.read()

# Now, let's process the content to extract authors and their corresponding page numbers
import re
from collections import defaultdict

# Splitting the text into individual papers
papers = doc_content.strip().split("\n\n")

# Creating a dictionary to store authors and their corresponding page numbers
authors_dict = defaultdict(set)

# Function to format author name as "Lastname, Firstname"
def format_author_name(name):
    parts = name.split(" ")
    if len(parts) == 2:
        return f"{parts[1]},{parts[0]}"
    return name

# Iterating through each paper
for paper in papers:
    lines = paper.split("\n")
    if len(lines) < 2:
        continue

    # Extracting page number and authors
    page_number = re.findall(r'\d+', lines[0])[-1]  # Assuming the last number is the page number
    authors = lines[1].split(", ")

    # Adding page number to each author in the dictionary
    for author in authors:
        if author:  # Check if author name is not empty
            formatted_author = format_author_name(author)
            authors_dict[formatted_author].add(page_number)

# Formatting the output
formatted_output = []
for author, pages in authors_dict.items():
    pages_string = ",".join(sorted(pages, key=int))
    formatted_output.append(f"{author}..................{pages_string}")

# Joining all formatted strings
final_output = "\n".join(formatted_output)

with open(r'C:\Users\Administrator\Desktop\output.txt', 'w') as f:
    f.write(final_output)

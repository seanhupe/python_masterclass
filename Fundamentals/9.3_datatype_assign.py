# 1. List Manipulation

fruits = ["apple", "banana", "cherry", "date"]
fruits.append("elderberry")
fruits.remove("banana")
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

#-----------------------------------------------------------------------------
# 2. Dictionary Basics
student = {
    "name": "John Doe",
    "age": "25",
    "major": "Computer Science",
}

print(student)

student["major"] = "Electrical Engineering"
print(student)

student["Year"] = "Senior"
print(student)

print(student.keys())
print(student.values())


#-----------------------------------------------------------------------------
# 3. List of Dictionaries
# create list of Dicts: each Dict represents a Book and has the following keys: title, author, year
books = [
    {
        "title": "Find a Damn Job",
        "author": "Sean Hupe",
        "year": "2024",
    }
]
print(books)

# Add a book to the list
books.append({"title": "Moby Dick", "author": "Herman Melville", "year": 1851})
# books.append({"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813})
# books.append({"title": "IT", "author": "Steven King", "year": 1978})
print(books)

# Print the title of the second book in the list

# Iterate over the list and print out each Book Title and Author
for book in books:
    print(f"Title: {book['title']}, author: {book['author']}")

#-----------------------------------------------------------------------------
# 4. Dictionary containing a List

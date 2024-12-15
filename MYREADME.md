# Project: Magazine Management System

## Description
The Magazine Management System is a Python-based application designed to manage relationships between *Authors, **Articles, and **Magazines*. It provides methods to perform CRUD operations and retrieve meaningful insights such as contributors, associated articles, and more using SQL joins and object-oriented principles.

---

## Features

### Models

1. *Author*
   - Represents an author in the system.
   - Methods:
     - articles(): Retrieves all articles written by the author.
     - magazines(): Retrieves all magazines associated with the author.

2. *Article*
   - Represents an article written by an author and published in a magazine.
   - Properties:
     - author: Returns the author of the article.
     - magazine: Returns the magazine where the article is published.

3. *Magazine*
   - Represents a magazine in the system.
   - Methods:
     - articles(): Retrieves all articles published in the magazine.
     - contributors(): Retrieves all authors who contributed articles to the magazine.
     - article_titles(): Returns a list of all article titles published in the magazine.
     - contributing_authors(): Returns a list of authors with more than 2 articles published in the magazine.

### Database Connection
- A SQLite database is used for data persistence.
- The Connection class manages all interactions with the database.

### Tests
- Unit tests are provided to ensure the integrity of the models and their relationships.

---

## Installation

### Prerequisites
- Python 3.8+
- SQLite3

### Steps
1. Clone the repository:
   bash
   git clone https://github.com/ShirleenChebet/Moringa-FT09-phase-3-code-challenge.git
   cd Moringa-FT09-phase-3-code-challenge
   

2. Set up a virtual environment:
   bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   

3. Install dependencies:
   bash
   pip install -r requirements.txt
   

4. Set up the database:
   bash
   python setup_database.py
   

---

## Usage

### Running the Application
1. Run the main application:
   bash
   python app.py
   

2. Use the provided methods to manage authors, articles, and magazines.

### Running Tests
- To run all unit tests:
  bash
  pytest
  

---

## Example Code

### Creating a Magazine
python
from models.magazine import Magazine

magazine = Magazine(id=1, name="Tech Weekly")
print(magazine.name)  # Output: Tech Weekly


### Fetching Articles by an Author
python
from models.author import Author

author = Author(id=1, name="John Doe")
articles = author.articles()
for article in articles:
    print(article.title)


### Contributors to a Magazine
python
from models.magazine import Magazine

magazine = Magazine(id=1, name="Tech Weekly")
contributors = magazine.contributors()
for contributor in contributors:
    print(contributor.name)


---

## Project Structure

magazine-management-system/
├── app.py                 # Main entry point for the application
├── models/                # Directory containing model definitions
│   ├── author.py          # Author model
│   ├── article.py         # Article model
│   └── magazine.py        # Magazine model
├── database/
│   └── connection.py      # Database connection management
├── tests/                 # Directory containing test cases
│   └── test_models.py     # Unit tests for models
├── setup_database.py      # Script to initialize the database
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation


---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contributions
Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.

---

## Contact
- *Author*: Shirleen Chebet
- *Email*: shirleen.chebet@student.moringaschool.com
- *GitHub*: [shirleenChebet](https://github.com/ShirleenChebet

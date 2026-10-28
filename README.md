# AI Engineer Learning

I am a beginner learning Python step by step by following a 6-month AI Engineer roadmap. This repository contains my practice code and projects.

## Week 1: Python Fundamentals — Completed

Practice files:

- `01_variables_and_types.py` — variables and basic data types
- `02_input_and_calculations.py` — user input and arithmetic operations
- `03_marks_checker.py` — `if`, `elif`, and `else` conditions
- `04_multiplication_table.py` — `for` loop and `range`
- `05_while_loop.py` — `while` loop and countdown
- `06_number_guessing_game.py` — number guessing game with hints

## Week 2: Functions & Data Structures — Completed

Practice files:

- `01_functions.py` — functions, arguments, return values, and scope
- `02_lists.py` — lists, indexing, updating, adding, counting, and looping
- `03_dictionaries.py` — key-value pairs
- `04_tuples.py` — tuples and indexing
- `05_sets.py` — unique values and adding items
- `06_student_marks_analyzer.py` — average, highest and lowest marks, and pass/fail result
- `07_todo_list.py` — add and display tasks

## Week 3: Writing Real Python Code — Completed

Practice files:

- `01_modules_and_imports.py` — using the built-in `math` and `random` modules
- `02_file_handling.py` — writing to and reading from a text file
- `03_error_handling.py` — handling invalid input with `try` and `except`
- `04_debugging_practice.py` — finding and fixing a variable name error
- `05_csv_reader.py` — reading student marks from a CSV file and calculating the average, highest, and lowest marks
- `students.csv` — sample student marks data
- `learning_note.txt` — text file used for file handling practice

## Week 4: Git and GitHub

- `Week-04/01_git_branch_practice.md` — Git branches aur basic workflow practice

## Week 5: Data Handling with Pandas — Completed

- `Week-05/01_pandas_intro.py` — DataFrames, CSV loading, filtering, sorting, grouping, and basic data exploration
- `Week-05/02_excel_reader.py` — exporting CSV data to Excel and reading Excel files
- `Week-05/03_student_data_analysis.py` — analyzing student marks with Pandas
- `Week-05/04_iris_dataset_analysis.py` — exploring the Iris dataset with Pandas
- `Week-05/students.csv` — sample student marks data
- `Week-05/students.xlsx` — generated Excel workbook
- `Week-05/iris.csv` — UCI Iris dataset

Iris dataset source: R. A. Fisher (1936), [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/53/iris), CC BY 4.0.

## Week 6: Data Cleaning & Preparation

- `messy_students.csv` — sample data with a missing mark and duplicate row
- `01_inspect_messy_data.py` — inspect missing values and duplicate rows
- `02_clean_student_data.py` — remove missing and duplicate records; add a pass/fail feature
- `03_fill_missing_marks.py` — fill a missing mark using the average
- `04_student_data_cleaning_project.py` — clean data, create features, scale marks, and save the final CSV
- `final_cleaned_students.csv` — final cleaned dataset

## Week 7: Text Processing Basics

- `01_text_basics.py` — lowercase, punctuation removal, tokenization, and stopwords
- `02_stemming.py` — reducing words with Porter stemming
- `03_lemmatization.py` — converting words to dictionary base forms
- `04_text_cleaning_pipeline.py` — text-cleaning pipeline using NLTK
- NLTK data setup: `python -m nltk.downloader stopwords wordnet`

## Week 8: Embeddings & Similarity

- `01_vectors.py` — representing words with number vectors
- `02_cosine_similarity.py` — comparing vectors using cosine similarity
- `03_bag_of_words.py` — creating word-count vectors and comparing text
- `04_real_embeddings.py` — generating sentence embeddings with a pretrained model
- `05_semantic_search.py` — finding the closest sentence to a query

The first run downloads the public model and requires an internet connection. The examples use CPU and do not require a GPU.
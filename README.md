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

Practice files:

- `Week-04/01_git_branch_practice.md` — Git branches and basic workflow practice

## Week 5: Data Handling with Pandas — Completed

Practice files:

- `Week-05/01_pandas_intro.py` — DataFrames, CSV loading, filtering, sorting, grouping, and basic data exploration
- `Week-05/02_excel_reader.py` — exporting CSV data to Excel and reading Excel files
- `Week-05/03_student_data_analysis.py` — analyzing student marks with Pandas
- `Week-05/04_iris_dataset_analysis.py` — exploring the Iris dataset with Pandas
- `Week-05/students.csv` — sample student marks data
- `Week-05/students.xlsx` — generated Excel workbook
- `Week-05/iris.csv` — UCI Iris dataset

Iris dataset source: R. A. Fisher (1936), [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/53/iris), CC BY 4.0.

## Week 6: Data Cleaning & Preparation

Practice files:

- `messy_students.csv` — sample data with a missing mark and duplicate row
- `01_inspect_messy_data.py` — inspect missing values and duplicate rows
- `02_clean_student_data.py` — remove missing and duplicate records; add a pass/fail feature
- `03_fill_missing_marks.py` — fill a missing mark using the average
- `04_student_data_cleaning_project.py` — clean data, create features, scale marks, and save the final CSV
- `final_cleaned_students.csv` — final cleaned dataset

## Week 7: Text Processing Basics

Practice files:

- `01_text_basics.py` — lowercase, punctuation removal, tokenization, and stopwords
- `02_stemming.py` — reducing words with Porter stemming
- `03_lemmatization.py` — converting words to dictionary base forms
- `04_text_cleaning_pipeline.py` — text-cleaning pipeline using NLTK

NLTK data setup:

```bash
python -m nltk.downloader stopwords wordnet
```

## Week 8: Embeddings & Similarity

Practice files:

- `01_vectors.py` — representing words with number vectors
- `02_cosine_similarity.py` — comparing vectors using cosine similarity
- `03_bag_of_words.py` — creating word-count vectors and comparing text
- `04_real_embeddings.py` — generating sentence embeddings with a pretrained model
- `05_semantic_search.py` — finding the closest sentence to a query

The first run downloads the public model and requires an internet connection.

The scripts automatically use CUDA when a compatible NVIDIA GPU is available; otherwise, they fall back to CPU. The downloaded model is cached for future runs.

## Week 9: Machine Learning Foundations — Completed

### Concepts Covered

- Supervised and unsupervised learning
- Training and testing datasets
- Data splitting using `train_test_split()`
- Introduction to Logistic Regression
- Training models using `model.fit()`
- Making predictions using `model.predict()`
- Evaluating models using accuracy score

### Practice Projects

- `Week-09/01_train_test_split.py` — splitting student data into training and testing datasets
- `Week-09/02_student_ml_project.py` — preparing and displaying student training and testing data
- `Week-09/03_train_student_model.py` — training a Logistic Regression model and predicting student results

### Libraries Used

- Scikit-learn

### Key Learning

Built a basic student pass/fail prediction model using study hours as input features.

Note: This project uses a very small sample dataset for learning purposes. Its accuracy is not representative of real-world performance.

## Week 10: Core Machine Learning Algorithms — Completed

### Concepts Covered

- Linear Regression for predicting numerical values
- Logistic Regression for classification
- K-Nearest Neighbors (KNN) classification
- Decision Tree classification
- Training and testing machine learning models
- Comparing different machine learning algorithms using accuracy score
- Making predictions with trained models

### Practice Projects

- `Week-10/01_linear_regression.py` — predicting student marks based on study hours using Linear Regression
- `Week-10/02_logistic_regression.py` — predicting student pass/fail results using Logistic Regression
- `Week-10/03_knn_classifier.py` — classifying student results using K-Nearest Neighbors
- `Week-10/04_decision_tree.py` — predicting student results using a Decision Tree classifier
- `Week-10/05_compare_models.py` — comparing Logistic Regression, KNN, and Decision Tree models
- `Week-10/06_student_performance_prediction.py` — combined student performance prediction project using multiple machine learning algorithms

### Libraries Used

- Scikit-learn
- NumPy (used internally by Scikit-learn)

### Key Learning

Learned how different machine learning algorithms work and built a student performance prediction project using study hours to predict marks and pass/fail results.

Note: These projects use small sample datasets for learning purposes. Their predictions and accuracy scores are not representative of real-world performance.

## Week 11: Model Evaluation — Completed

### Concepts Covered

- Accuracy, Precision, Recall, and F1 Score
- Confusion Matrix
- 5-Fold Cross-validation
- Model Error Analysis
- Evaluating machine learning model performance
- Identifying and analysing incorrect predictions

### Practice Projects

- `Week-11/01_model_evaluation_metrics.py` — calculating accuracy, precision, recall, F1 score, and confusion matrix
- `Week-11/02_cross_validation.py` — evaluating model performance using 5-fold cross-validation
- `Week-11/03_model_error_analysis.py` — identifying incorrect predictions and calculating accuracy and error rate
- `Week-11/04_model_evaluation_report.py` — complete model evaluation project combining evaluation metrics, confusion matrix, cross-validation, and error analysis

### Libraries Used

- Scikit-learn

### Key Learning

Learned how to evaluate machine learning models beyond accuracy, measure performance across multiple folds, interpret confusion matrices, and investigate incorrect predictions.

Built a complete student performance model evaluation report using Logistic Regression.

Note: The final project uses a small sample dataset for learning purposes. Its evaluation results are not representative of real-world model performance.

## Learning Progress

This repository documents my journey from Python fundamentals to AI engineering concepts through hands-on practice and projects.

More weeks and projects will be added as I progress through the 6-month AI Engineer roadmap.
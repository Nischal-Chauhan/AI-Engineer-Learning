**# AI Engineer Learning**



I am a beginner learning Python step by step by following a 6-month AI

Engineer roadmap. This repository contains my practice code and

projects.



**## Week 1: Python Fundamentals --- Completed**



**### Practice Files**



\-   `01\_variables\_and\_types.py` --- variables and basic data types

\-   `02\_input\_and\_calculations.py` --- user input and arithmetic

    operations

\-   `03\_marks\_checker.py` --- if, elif, and else conditions

\-   `04\_multiplication\_table.py` --- for loop and range

\-   `05\_while\_loop.py` --- while loop and countdown

\-   `06\_number\_guessing\_game.py` --- number guessing game with hints



**## Week 2: Functions \& Data Structures --- Completed**



**### Practice Files**



\-   `01\_functions.py` --- functions, arguments, return values, and scope

\-   `02\_lists.py` --- lists, indexing, updating, adding, counting, and

    looping

\-   `03\_dictionaries.py` --- key-value pairs

\-   `04\_tuples.py` --- tuples and indexing

\-   `05\_sets.py` --- unique values and adding items

\-   `06\_student\_marks\_analyzer.py` --- average, highest and lowest

    marks, and pass/fail result

\-   `07\_todo\_list.py` --- add and display tasks



**## Week 3: Writing Real Python Code --- Completed**



**### Practice Files**



\-   `01\_modules\_and\_imports.py` --- using the built-in `math` and

    `random` modules

\-   `02\_file\_handling.py` --- writing to and reading from a text file

\-   `03\_error\_handling.py` --- handling invalid input with `try` and

    `except`

\-   `04\_debugging\_practice.py` --- finding and fixing a variable name

    error

\-   `05\_csv\_reader.py` --- reading student marks from a CSV file and

    calculating the average, highest, and lowest marks

\-   `students.csv` --- sample student marks data

\-   `learning\_note.txt` --- text file used for file handling practice



**## Week 4: Git and GitHub**



**### Practice**



\-   `Week-04/01\_git\_branch\_practice.md` --- Git branches and basic

    workflow practice



**## Week 5: Data Handling with Pandas --- Completed**



**### Practice Files**



\-   `Week-05/01\_pandas\_intro.py` --- DataFrames, CSV loading, filtering,

    sorting, grouping, and basic data exploration

\-   `Week-05/02\_excel\_reader.py` --- exporting CSV data to Excel and

    reading Excel files

\-   `Week-05/03\_student\_data\_analysis.py` --- analysing student marks

    with Pandas

\-   `Week-05/04\_iris\_dataset\_analysis.py` --- exploring the Iris dataset

    with Pandas

\-   `Week-05/students.csv` --- sample student marks data

\-   `Week-05/students.xlsx` --- generated Excel workbook

\-   `Week-05/iris.csv` --- Iris dataset



Iris dataset source: R. A. Fisher (1936), \[UCI Machine Learning

Repository](https://archive.ics.uci.edu/dataset/53/iris), CC BY 4.0.



**## Week 6: Data Cleaning \& Preparation**



**### Practice Files**



\-   `Week-06/messy\_students.csv` --- sample data with a missing mark and

    duplicate row

\-   `Week-06/01\_inspect\_messy\_data.py` --- inspecting missing values and

    duplicate rows

\-   `Week-06/02\_clean\_student\_data.py` --- removing missing and

    duplicate records and adding a pass/fail feature

\-   `Week-06/03\_fill\_missing\_marks.py` --- filling missing marks using

    the average

\-   `Week-06/04\_student\_data\_cleaning\_project.py` --- complete data

    cleaning project, feature creation, scaling, and saving the final

    CSV

\-   `Week-06/final\_cleaned\_students.csv` --- final cleaned dataset



**## Week 7: Text Processing Basics**



**### Practice Files**



\-   `Week-07/01\_text\_basics.py` --- lowercase, punctuation removal,

    tokenization, and stopwords

\-   `Week-07/02\_stemming.py` --- reducing words with Porter stemming

\-   `Week-07/03\_lemmatization.py` --- converting words to dictionary

    base forms

\-   `Week-07/04\_text\_cleaning\_pipeline.py` --- text-cleaning pipeline

    using NLTK



**### NLTK Data Setup**



``` bash

python -m nltk.downloader stopwords wordnet

```



**## Week 8: Embeddings \& Similarity**



**### Practice Files**



\-   `Week-08/01\_vectors.py` --- representing words with number vectors

\-   `Week-08/02\_cosine\_similarity.py` --- comparing vectors using cosine

    similarity

\-   `Week-08/03\_bag\_of\_words.py` --- creating word-count vectors and

    comparing text

\-   `Week-08/04\_real\_embeddings.py` --- generating sentence embeddings

    with a pretrained model

\-   `Week-08/05\_semantic\_search.py` --- finding the closest sentence to

    a query



The first run downloads the public model and requires an internet

connection.



The scripts automatically use CUDA when a compatible NVIDIA GPU is

available; otherwise, they fall back to CPU. The downloaded model is

cached for future runs.



**## Week 9: Machine Learning Foundations --- Completed**



**### Concepts Covered**



\-   Supervised and unsupervised learning

\-   Training and testing datasets

\-   Data splitting using `train\_test\_split()`

\-   Introduction to Logistic Regression

\-   Training models using `model.fit()`

\-   Making predictions using `model.predict()`

\-   Evaluating models using accuracy score



**### Practice Projects**



\-   `Week-09/01\_train\_test\_split.py` --- splitting student data into

    training and testing datasets

\-   `Week-09/02\_student\_ml\_project.py` --- preparing and displaying

    student training and testing data

\-   `Week-09/03\_train\_student\_model.py` --- training a Logistic

    Regression model and predicting student results



**### Libraries Used**



\-   Scikit-learn



**### Key Learning**



Built a basic student pass/fail prediction model using study hours as

input features.



Note: This project uses a very small sample dataset for learning

purposes. Its accuracy is not representative of real-world performance.



**## Week 10: Core Machine Learning Algorithms --- Completed**



**### Concepts Covered**



\-   Linear Regression for predicting numerical values

\-   Logistic Regression for classification

\-   K-Nearest Neighbors (KNN) classification

\-   Decision Tree classification

\-   Training and testing different machine learning models

\-   Comparing model predictions and performance

\-   Making predictions using trained models



**### Practice Projects**



\-   `Week-10/01\_linear\_regression.py` --- learning numerical prediction

    using Linear Regression

\-   `Week-10/02\_logistic\_regression.py` --- classification using

    Logistic Regression

\-   `Week-10/03\_knn\_classifier.py` --- classification using K-Nearest

    Neighbors

\-   `Week-10/04\_decision\_tree.py` --- classification using Decision Tree

\-   `Week-10/05\_compare\_models.py` --- comparing different machine

    learning algorithms

\-   `Week-10/06\_student\_performance\_prediction.py` --- predicting

    student performance using study hours



**### Libraries Used**



\-   Pandas

\-   NumPy

\-   Scikit-learn



**### Key Learning**



Learned how different machine learning algorithms work and built a

student performance prediction project using study hours to predict

marks and pass/fail results.



Note: These projects use small sample datasets for learning purposes.

Their predictions and accuracy scores are not representative of

real-world performance.



**## Week 11: Model Evaluation --- Completed**



**### Concepts Covered**



\-   Accuracy, Precision, Recall, and F1 Score

\-   Confusion Matrix

\-   5-Fold Cross-validation

\-   Model Error Analysis

\-   Evaluating machine learning model performance

\-   Identifying and analysing incorrect predictions



**### Practice Projects**



\-   `Week-11/01\_model\_evaluation\_metrics.py` --- calculating accuracy,

    precision, recall, F1 score, and confusion matrix

\-   `Week-11/02\_cross\_validation.py` --- evaluating model performance

    using 5-fold cross-validation

\-   `Week-11/03\_model\_error\_analysis.py` --- identifying incorrect

    predictions and calculating accuracy and error rate

\-   `Week-11/04\_model\_evaluation\_report.py` --- complete model

    evaluation project combining evaluation metrics, confusion matrix,

    cross-validation, and error analysis



**### Libraries Used**



\-   Scikit-learn



**### Key Learning**



Learned how to evaluate machine learning models beyond accuracy, measure

performance across multiple folds, interpret confusion matrices, and

investigate incorrect predictions.



Built a complete student performance model evaluation report using

Logistic Regression.



Note: The final project uses a small sample dataset for learning

purposes. Its evaluation results are not representative of real-world

model performance.



**## Week 12: Student Performance Prediction Project --- Completed**



**### Project Overview**



Built a machine learning project to predict students' final grades using

the UCI Student Performance dataset.



The project covers the complete machine learning workflow, from dataset

inspection and exploratory data analysis to model training, evaluation,

hyperparameter tuning, and making predictions.



**### Concepts Covered**



\-   Dataset inspection and exploratory data analysis

\-   Data visualization and feature relationships

\-   Numerical and categorical feature preparation

\-   Data preprocessing using Scikit-learn

\-   Training and testing data splitting

\-   Linear Regression

\-   Random Forest Regressor

\-   Gradient Boosting Regressor

\-   Decision Tree Regressor

\-   Model comparison and evaluation

\-   Hyperparameter tuning using GridSearchCV

\-   Saving and loading trained models using Joblib



**### Project Repository**



\-   \[Student Performance

    Prediction](https://github.com/Nischal-Chauhan/Student-Performance-Prediction)



**### Models Compared**



\-   Linear Regression

\-   Random Forest Regressor

\-   Gradient Boosting Regressor

\-   Decision Tree Regressor



**### Best Model Results**



Tuned Random Forest Regressor:



\-   MAE: 2.99

\-   RMSE: 3.76

\-   R² Score: 0.312



**### Libraries Used**



\-   Python

\-   Pandas

\-   NumPy

\-   Matplotlib

\-   Seaborn

\-   Scikit-learn

\-   Joblib



**### Key Learning**



Learned how to build a complete machine learning regression project,

compare different algorithms, evaluate model performance, tune

hyperparameters, and save a trained model for future predictions.



Note: The model's predictive performance is limited and is intended for

learning purposes, not real-world student assessment.





\## Week 13: LLM Fundamentals \& Gemini Chatbot --- Completed



\### Concepts Covered



\- Large Language Models (LLMs) and how they generate responses

\- Prompts and inference

\- Tokens and context windows

\- Limitations of LLMs, including hallucinations, outdated information, bias, and context limits

\- Connecting Python applications to the Gemini API

\- Handling API errors and request timeouts



\### Practice Files



\- `Week-13/01\_llm\_fundamentals.py` --- introduction to Large Language Models, prompts, and inference

\- `Week-13/02\_tokens\_and\_context.py` --- tokens and context windows

\- `Week-13/03\_gemini\_chatbot.py` --- interactive chatbot built with the Google Gemini API



\### Libraries and Tools Used



\- Python

\- Google Gen AI SDK (`google-genai`)

\- `python-dotenv`

\- Google Gemini API



\### Key Learning



Learned the fundamentals of LLMs, how tokens and context windows work, and common limitations of language models. Built an interactive Python chatbot using the Gemini API and stored the API key in a local `.env` file rather than hard-coding it in the source code.



Note: The Gemini API requires an API key. The `.env` file containing the key is excluded from Git using `.gitignore`; never commit or share API keys.



\## Week 14: Prompt Engineering --- Completed



\### Concepts Covered



\- Role-based prompting

\- Few-shot prompting

\- Structured outputs using JSON

\- Prompt iteration and improvement

\- Dynamic prompt generation based on user input

\- Handling API errors and temporary server failures

\- Automatic retry mechanism



\### Practice Project



\- `Week-14/01\_prompt\_summarizer.py` --- AI-powered text summarizer using the Gemini API



\### Project Features



\- Short summaries (1–2 sentences)

\- Medium summaries (3–5 sentences)

\- Detailed summaries (6–8 sentences)

\- Exactly 3 key points in the generated output

\- Structured JSON responses

\- Automatic retry when the Gemini API returns a temporary 503 error

\- Input validation and error handling



\### Libraries and Tools Used



\- Python

\- Google Gen AI SDK (`google-genai`)

\- `python-dotenv`

\- JSON

\- Google Gemini API



\### Key Learning



Learned how to design and improve prompts, control the structure and length of AI-generated summaries, request structured JSON output, and handle temporary API failures using an automatic retry mechanism.



Note: The Gemini API requires an API key. The `.env` file containing the key is excluded from Git using `.gitignore`; never commit or share API keys.




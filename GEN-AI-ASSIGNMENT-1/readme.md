# 🧠 Text Feature Engineering Assignment

This project is part of my **Full Stack Gen AI course by Krish Naik sir**, guided by my mentor Sunny sir.

It focuses on converting real-world text data into numerical features for machine learning.

---

## 🚀 Project Overview

The goal of this assignment was to:

* Collect real-world text data (product reviews)
* Clean and preprocess the text
* Convert text into numerical features
* Analyze different feature engineering techniques
* Build a simple ML model for sentiment classification

---

## 📊 Dataset

* Source: Flipkart product reviews
* Data collected using Selenium (web scraping)
* Stored in CSV format (`reviews.csv`)

---

## 🛠️ Steps Performed

### 1️⃣ Data Collection

* Scraped product reviews from Flipkart
* Handled dynamic loading and scrolling

---

### 2️⃣ Text Preprocessing

* Converted text to lowercase
* Removed punctuation and numbers
* Tokenized text
* Removed stopwords
* Cleaned noisy data

---

### 3️⃣ Vocabulary Creation

* Extracted all unique words from dataset
* Removed noisy and irrelevant tokens
* Final vocabulary contains meaningful words

---

### 4️⃣ Feature Engineering

Implemented 3 techniques:

#### ✔ One Hot Encoding (OHE)

* Binary representation (0 or 1)

#### ✔ Bag of Words (BoW)

* Counts word frequency

#### ✔ TF-IDF

* Assigns importance to words
* Reduces weight of common words

---

### 5️⃣ Sparse Matrix Analysis

* Observed that most values are zero
* Explained inefficiency in large-scale systems

---

### 6️⃣ Sentiment Classification

* Used Logistic Regression
* Classified reviews into:

  * Positive (1)
  * Negative (0)

---

## 📈 Results

* TF-IDF performed better than BoW
* Important words had higher impact on predictions
* Model achieved good accuracy for basic sentiment classification

---

## ⚡ Challenges Faced

* Web scraping dynamic content (Flipkart)
* Cleaning noisy real-world data
* Handling duplicate and irrelevant tokens

---

## 🧠 Key Learnings

* Importance of preprocessing in NLP
* Difference between BoW and TF-IDF
* How text is converted into numerical form
* Real-world challenges in scraping and data cleaning

---

## 🔮 Future Improvements

* Use advanced models (Word2Vec, BERT)
* Improve preprocessing with lemmatization
* Use larger datasets
* Apply deep learning models

---

## 🛠️ Tech Stack

* Python
* Pandas
* NLTK
* Scikit-learn
* Selenium

---

## 📌 Conclusion

This project helped me understand how raw text data can be transformed into meaningful features and used in machine learning models.

It also provided hands-on experience with real-world data and challenges.

---

⭐ Learning in public — more projects coming soon!

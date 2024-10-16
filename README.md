# Email Spam Detection with Streamlit

This project is a machine learning-based email spam detection system built using Python and Streamlit. The system classifies emails as spam or not spam (ham) using a trained classification model.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [How to Run the App](#how-to-run-the-app)
5. [Project Structure](#project-structure)
6. [Model Overview](#model-overview)
7. [Dataset](#dataset)
8. [License](#license)

## Introduction
This project demonstrates how to build a machine learning model to classify emails as **spam** or **ham** (not spam) and visualize the results using a **Streamlit** web app. The model uses a variety of natural language processing (NLP) techniques and classification algorithms.

## Features
- **Streamlit App**: Interactive web interface for email classification.
- **Model**: Pretrained machine learning model for spam detection.
- **Visualization**: Display of classification results.
- **Real-time predictions**: Users can input custom email text for real-time classification.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/29ananyaseth/Email_spam_detection.git
   
2.Navigate to the Project Directory:
    cd Email_spam_detection
3.Install the Required Dependencies: Use the provided requirements.txt file to install the necessary Python packages:
    pip install -r requirements.txt
4.Run the Streamlit App:
     streamlit run app.py


------------------------------------------------------------------------------------------------------------------------------------------------------------------
Project Structure
-----------------

.
├── spam.csv                # Dataset file for training the model
├── spam.pkl                # Trained machine learning model
├── vectorizer.pkl          # Vectorizer for transforming text data
├── app.py                  # Main Streamlit app
├── requirements.txt        # Dependencies for the project
├── README.md               # Documentation file
├── train_and_save_model.py  # Script to train the model
└── spamdetector.py         # Script containing the email classification logic

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Model Overview
---------------

The model is based on Natural Language Processing (NLP) and machine learning techniques, specifically:

Text vectorization using TF-IDF Vectorizer.
Classification using a Naive Bayes classifier (or another classification algorithm).

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Training the Model
------------------

The training script (train_and_save_model.py) uses a labeled dataset of emails (spam vs. ham) to train the model.
The trained model is then saved as spam.pkl, and the text vectorizer is saved as vectorizer.pkl.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Dataset
-------

The dataset used for training the model is stored in spam.csv. It consists of a collection of emails that are labeled as either "spam" or "ham" (not spam).

Sample of the dataset:
Label	Email Text
ham	"Hi, how are you doing today?"
spam	"Congratulations! You've won a free iPhone!"

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

License
-------

This project is licensed under the MIT License.



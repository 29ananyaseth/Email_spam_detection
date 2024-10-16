import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load the dataset
data = pd.read_csv("spam.csv", encoding="latin1")

# Clean the data
data.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
data['v1'] = data['v1'].map({'ham': 0, 'spam': 1})

# Separate features and labels
x = data['v2']  # Message text
y = data['v1']  # Labels (ham=0, spam=1)

# Vectorize the text data
cv = CountVectorizer()
x = cv.fit_transform(x)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Train the Naive Bayes model
model = MultinomialNB()
model.fit(x_train, y_train)

# Evaluate the model
accuracy = model.score(x_test, y_test) * 100
print(f"Model accuracy: {accuracy:.2f}%")

# Save the trained model and vectorizer
pickle.dump(model, open("spam.pkl", "wb"))
pickle.dump(cv, open("vectorizer.pkl", "wb"))

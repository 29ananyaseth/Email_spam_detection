import pickle
import streamlit as st

# Load the trained model and vectorizer
model = pickle.load(open("spam.pkl", 'rb'))
cv = pickle.load(open("vectorizer.pkl", 'rb'))

# Define the main function for the Streamlit app
def main():
    st.title("Spam Message Detector")
    st.write("Enter a message to check if it's spam or not.")

    # Input from the user
    msg = st.text_input("Enter a message")

    if st.button("Predict"):
        # Transform the input message using the loaded vectorizer
        data = [msg]
        vect = cv.transform(data).toarray()

        # Make a prediction using the loaded model
        prediction = model.predict(vect)[0]

        # Display the result
        if prediction == 1:
            st.error("This is a SPAM message!")
        else:
            st.success("This is a HAM message!")

# Run the Streamlit app
if __name__ == '__main__':
    main()

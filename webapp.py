# Importing necessary libraries
import streamlit as st
import numpy as np
import pickle

    # loading the saved model
loaded_model = pickle.load(open('D:/projects/PracticePRo/Heart Disease/trained_model.sav', 'rb'))

# Function to make predictions
def predict_heart_disease(model, input_data):
    # Convert input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the numpy array as we are predicting for only one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Make prediction
    #prediction = model.predict(input_data_reshaped)
    #return prediction[0]

# Streamlit App
def main():
    st.title("Heart Disease Prediction App")


    # Sidebar with user input
    st.sidebar.header("Enter Patient Details:")
    age = st.sidebar.slider("Age", 1, 100, 25)
    sex = st.sidebar.radio("Sex", ["Male", "Female"])
    cp = st.sidebar.selectbox("Chest Pain Type", [0, 1, 2, 3])
    trestbps = st.sidebar.slider("Resting Blood Pressure", 80, 200, 120)
    chol = st.sidebar.slider("Cholesterol", 50, 600, 200)
    fbs = st.sidebar.radio("Fasting Blood Sugar", ["<=120 mg/dl", ">120 mg/dl"])
    restecg = st.sidebar.selectbox("Resting Electrocardiographic Results", [0, 1, 2])
    thalach = st.sidebar.slider("Maximum Heart Rate Achieved", 60, 220, 150)
    exang = st.sidebar.radio("Exercise Induced Angina", ["No", "Yes"])
    oldpeak = st.sidebar.slider("ST Depression Induced by Exercise", 0.0, 6.0, 1.0)
    slope = st.sidebar.selectbox("Slope of the Peak Exercise ST Segment", [0, 1, 2])
    ca = st.sidebar.slider("Number of Major Vessels Colored by Fluoroscopy", 0, 3, 1)
    thal = st.sidebar.selectbox("Thalassemia", [0, 1, 2, 3])

    # Create a button to make predictions
    if st.sidebar.button("Predict"):
        # Gather input data
        input_data = (age, 1 if sex == "Male" else 0, cp, trestbps, chol, 1 if fbs == ">120 mg/dl" else 0,
                      restecg, thalach, 1 if exang == "Yes" else 0, oldpeak, slope, ca, thal)

        # Make prediction
        prediction = predict_heart_disease("trained_model.sav", input_data)

        # Display result
        if prediction == 0:
            st.success("The person does not have heart disease.")
        else:
            st.error("The person has heart disease.")

# Run the app
if __name__ == "__main__":
    main()

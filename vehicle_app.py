# app.py

import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model
with open('final_model1.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit app
def main():
    st.set_page_config(page_title="Vehicle Insurance Prediction", page_icon="🚗")

    st.title("Vehicle Insurance Prediction")
    st.markdown("---")

    st.sidebar.header("User Input")

    # Collect user input
    gender = st.sidebar.radio("Select Gender", ["Male", "Female"])
    age = st.sidebar.slider("Select Age", min_value=18, max_value=80, value=30)
    previously_insured = st.sidebar.radio("Previously Insured", ["Yes", "No"])
    vehicle_damage = st.sidebar.radio("Vehicle Damage in the Past", ["Yes", "No"])
    vehicle_age = st.sidebar.radio("Vehicle Age", ["< 1 Year", "1-2 Year", " >2 Years"])

    # Map user input to numerical values
    gender_mapping = {"Male": 0, "Female": 1}
    previously_insured_mapping = {"Yes": 1, "No": 0}
    vehicle_damage_mapping = {"Yes": 0, "No": 1}
    vehicle_age_mapping = {"< 1 Year": 0, "1-2 Year": 1, " >2 Years": 2}

    gender = gender_mapping[gender]
    previously_insured = previously_insured_mapping[previously_insured]
    vehicle_damage = vehicle_damage_mapping[vehicle_damage]
    vehicle_age = vehicle_age_mapping[vehicle_age]

    # Make a prediction
    user_data = [[gender, age, previously_insured, vehicle_damage, vehicle_age]]
    prediction = model.predict(user_data)

    # Display the result
    st.markdown("---")
    st.subheader("Prediction Result:")
    result = "Interested in vehicle insurance." if prediction[0] == 1 else "Not interested in vehicle insurance."
    st.success(result)

    # Footer
    st.markdown("---")
    st.write(
        "Developed by: SHAURYA KUSHWAH\n"
                           "04119011921\n"
                           
    )

if __name__ == "__main__":
    main()

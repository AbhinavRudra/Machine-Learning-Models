import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler,LabelEncoder




# Load pre-trained SVM model
with open('insurance_prediction.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


st.title("Insurance Price Prediction App")
#st.image('images used/img_emotion.png')


scaler = StandardScaler()
encoder = LabelEncoder()

char = ['patient_occupation', 'patient_cholesterol_level', 'patient_gender', 'patient_smoking_status', 'patient_location', 'patient_covered_by_other_insurance_company', 'patient_alcohol_consumption', 'patient_exercise_regimen']
num = [ 'patient_years_with_insurance_with_us', 'patient_last_year_regular_checkup', 'patient_participates_in_adventure_sports', 'patient_occupation', 'patient_visited_doctor_last_1_year', 'patient_cholesterol_level', 'patient_average_daily_steps', 'patient_age', 'patient_has_heart_disease_history', 'patient_has_other_major_disease_history', 'patient_gender', 'patient_average_glucose_level', 'patient_body_mass_index', 'patient_smoking_status', 'patient_year_last_admitted', 'patient_location', 'patient_weight', 'patient_covered_by_other_insurance_company', 'patient_alcohol_consumption', 'patient_exercise_regimen', 'patient_weight_change_last_year', 'patient_body_fat_percentage', 'patient_insurance_cost']
print(len(num))


with st.sidebar:
    st.subheader('Patient Details')
    name = st.text_input('Name')
    address = st.text_area('Address')
    age = st.number_input('Age', min_value=18, max_value=100)
    bmi = st.number_input('BMI', min_value=10.0, max_value=50.0)


# Main content area
st.write('## Predict Insurance Price')

# Example button to trigger prediction (you'll replace this with your actual prediction logic)
if st.button('Predict'):
    # Preprocess inputs for the model (example preprocessing; adjust as necessary)
    gender_numeric = 1 if gender == 'Male' else 0
    smoking_status_numeric = 1 if smoking_status == 'Smoker' else 0

    # Create an input array for the model
    input_data = np.array([[age, bmi, gender_numeric, smoking_status_numeric]])

    # Make the prediction
    predicted_price = model.predict(input_data)[0]
    
    # Display the prediction
    st.write(f'Predicted Insurance Price for {name}: ${predicted_price:.2f}')

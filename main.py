import pickle
import numpy as np
import streamlit as st

# Load the model
predict_calories_model = pickle.load(open('calories_burn_model.pkl', 'rb'))

# function to predict calories
def predict_calories(input_data):
    # turn input data into numpy array
    input_data_as_input_numarray = np.asarray(input_data)
    # reshape the data into model shape (model input shape is (1,7)
    input_data_reshaped = input_data_as_input_numarray.reshape(1,-1)
    # predict the data
    test_data_prediction = predict_calories_model.predict(input_data_reshaped)
    # return the prediction result
    return test_data_prediction[0]


def main():
    # Title of the web app
    st.title("Memprediksi Kalori yang Terbakar")
    # Description of the web app
    st.write("Isi form berikut untuk memprediksi kalori yang terbakar")

    # Form input section
    # Radio button
    gender = st.radio(
        "Pilih jenis kelamin",
        ("Pria", "Wanita"),
        index=None,
        horizontal=True
    )

    # Number input
    age = st.number_input("Umur", value=None, step=None, format='%f')
    weight = st.number_input("Berat badan dalam kg", value=None, step=None, format='%f')
    height = st.number_input("Tinggi badan dalam cm", value=None, step=None, format='%f')
    duration = st.number_input("Waktu latihan dalam menit", value=None, step=None, format='%f')
    hearth = st.number_input("Detak jantung", value=None, step=None, format='%f')
    temp = st.number_input("Suhu badan", value=None, step=None, format='%f')

    # input validation
    if gender is None or age is None or weight is None or height is None or duration is None or hearth is None or temp is None:
        st.error("Pastikan semua input tidak kosong.")
        return

    index_gender = ("Pria", "Wanita").index(gender);
    result = ''

    # Predict button
    if st.button("Prediksi"):
        result = predict_calories([index_gender, age, height, weight, duration, hearth, temp])
        st.success(f"Prediksi kalori yang terbakar: {result}")


if __name__ == "__main__":
    main()
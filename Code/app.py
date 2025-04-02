
# Create a new file named 'app.py' to save the code for the Streamlit app. It is important you use this
# magic function at the begining of the cell. Otherwise you will get error message.

# Import the Streamlit library to create the web app interface.
import pickle
import streamlit as st

# Load the trained model (classifier) from the 'classifier.pkl' file using pickle.
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

# Define the main function that sets up the layout and functionality of the Streamlit app.
def main():
    # Streamlit UI
    st.title("📊 Customer Default Prediction App")
    st.write("Predict whether a customer will default on their credit payments.")
    # User input form
    st.sidebar.header("Enter Customer Details")

    # Create input fields where users can enter data for prediction:
    SEX = st.sidebar.selectbox('Gender',("Male","Female"))
    MARRIAGE = st.sidebar.selectbox('Marital Status',("Married", "Single", "Others"))
    EDUCATION = st.sidebar.selectbox('Education Level',("Graduate School", "University", "High School", "Others"))
    LIMIT_BAL = st.sidebar.number_input("Credit Limit", min_value=1000, max_value=1000000, step=1000)
    AGE = st.sidebar.number_input("Age", min_value=18, max_value=100, step=1)
    PAY_1 = st.sidebar.slider("Most Recent Payment Status (-1: Paid in full, 1+: Late)", -2, 8, 0)
    BILL_AMT1 = st.sidebar.number_input("Most Recent Bill Amount", min_value=0, max_value=1000000, step=100)
    PAY_AMT1 = st.sidebar.number_input("Most Recent Payment Amount", min_value=0, max_value=1000000, step=100)
    late_payments = st.sidebar.number_input("Number of Late Payments in last 6 months", min_value=0, max_value=6, step=1)
    credit_utilization = BILL_AMT1/LIMIT_BAL
    result = ""


    # When the 'Predict Default Risk' button is clicked, call the prediction function and display the result.
    if st.button("Predict Default Risk"):
        result = prediction(LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE, PAY_1, BILL_AMT1, PAY_AMT1, late_payments, credit_utilization)
        print(result)

# Define the function to make the prediction based on the input data from the user.
def prediction(LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE, PAY_1, BILL_AMT1, PAY_AMT1, late_payments, credit_utilization):

    # Pre-process the input data to convert categorical values into numerical values:
    if SEX == "Male":
        SEX = 1
    else:
        SEX = 2

    if MARRIAGE == "Married":
        MARRIAGE = 1
    elif MARRIAGE == "Single":
        MARRIAGE = 2
    else:
        MARRIAGE = 0

    if EDUCATION == "Graduate School":
        EDUCATION = 1
    elif EDUCATION == "University":
        EDUCATION = 2
    elif EDUCATION == "High School":
        EDUCATION = 3
    else:
        EDUCATION = 4

    # Make the prediction using the trained classifier.
    mypred = classifier.predict(
        [[LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE, PAY_1, BILL_AMT1, PAY_AMT1, late_payments, credit_utilization]])

    # Convert the prediction result into a human-readable format.
    if mypred == 1:
        pred = st.error(f"🚨 High Risk: The customer is likely to default! (Risk Score: {mypred})")
    else:
        pred = st.success(f"✅ Low Risk: The customer is unlikely to default. (Risk Score: {mypred})")
    return pred


# Check if the script is being run directly and call the main function to run the app.
if __name__=='__main__':
    main()

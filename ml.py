import streamlit as st

# Title
st.title("Welcome to Shreyas Nimkhedkar's Machine Learning Projects")

# Description
st.write("""
Explore some of my exciting projects:
- **Loan Prediction Project**: Predict loan approvals based on customer data.
- **Customer Churn Prediction Project**: Analyze customer behavior to predict churn.
""")

# HTML for the cards
st.markdown("""
<div style="display: flex; justify-content: space-around; margin-top: 20px;">

    <!-- Loan Prediction Project -->
    <div style="background-color: #4CAF50; color: white; padding: 20px; border-radius: 10px; width: 45%; text-align: center; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
        <h3>Loan Prediction Project</h3>
        <p>Predict loan approvals based on customer data.</p>
        <a href="https://loanprediction.streamlit.app/" target="_blank" style="text-decoration: none; color: #fff; background-color: #2e7d32; padding: 10px 15px; border-radius: 5px;">Visit App</a>
    </div>

    <!-- Customer Churn Prediction Project -->
    <div style="background-color: #FF5722; color: white; padding: 20px; border-radius: 10px; width: 45%; text-align: center; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
        <h3>Customer Churn Prediction Project</h3>
        <p>Analyze customer behavior to predict churn.</p>
        <a href="https://customerchurnpredition.streamlit.app/" target="_blank" style="text-decoration: none; color: #fff; background-color: #bf360c; padding: 10px 15px; border-radius: 5px;">Visit App</a>
    </div>

</div>
""", unsafe_allow_html=True)

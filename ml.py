import streamlit as st

# Title
st.title("Welcome to Shreyas Nimkhedkar's Machine Learning Projects")

# Introduction
st.write("""
Explore my projects below:
- **Loan Prediction Project**
- **Customer Churn Prediction Project**
""")

# Create Link Cards using HTML
st.markdown("""
<div style="display: flex; justify-content: space-around; margin-top: 20px;">

    <!-- Loan Prediction Project Card -->
    <div style="background-color: #1e90ff; color: white; padding: 20px; border-radius: 10px; width: 40%; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);">
        <h3>Loan Prediction Project</h3>
        <p>Predict loan approvals based on customer data.</p>
        <a href="https://loanprediction.streamlit.app/" target="_blank" style="text-decoration: none; color: #fff; background-color: #0a5bff; padding: 10px 20px; border-radius: 5px;">Visit App</a>
    </div>

    <!-- Customer Churn Prediction Project Card -->
    <div style="background-color: #ff4500; color: white; padding: 20px; border-radius: 10px; width: 40%; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);">
        <h3>Customer Churn Prediction Project</h3>
        <p>Analyze customer behavior to predict churn.</p>
        <a href="https://customerchurnpredition.streamlit.app/" target="_blank" style="text-decoration: none; color: #fff; background-color: #ff2500; padding: 10px 20px; border-radius: 5px;">Visit App</a>
    </div>

</div>
""", unsafe_allow_html=True)

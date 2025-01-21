import streamlit as st

st.title("WELCOME TO SHREYAS NIMKHEDKAR PROJECTS")

st.title("Introduction:")
st.write('''
Hello, I am Shreyas Nimkhedkar, and I am thrilled to share my journey in the world of Machine Learning and Data Analysis. 
This application showcases a collection of my machine learning projects, including:
- **Loan Prediction**: A project to predict loan approval based on customer details.
- **Customer Churn Prediction**: A project that analyzes customer behavior to predict the likelihood of churn.

These projects demonstrate my ability to work with complex datasets and develop predictive models to solve real-world problems effectively.
''')

st.title("Areas of Expertise:")
st.write('''
1. **Machine Learning**: Crafting predictive models with algorithms like Random Forest, XGBoost, and Logistic Regression.
2. **Data Analysis**: Performing thorough exploratory data analysis (EDA) to derive actionable insights.
3. **Python Programming**: Expertise in libraries such as Pandas, NumPy, scikit-learn, Matplotlib, and Seaborn.
4. **Project Focus**:
   - Loan Approval Prediction using customer financial data.
   - Customer Churn Analysis for better business retention strategies.
''')

# Custom Card-Like Design
st.markdown("""
<div style="border: 2px solid #ccc; border-radius: 10px; padding: 15px; margin: 20px 0; background-color: #f9f9f9;">
    <h3 style="color: #333;">Shreyas Project</h3>
    <p style="color: #555;">Click this card for loan predition Projects</p>
    <a href="https://loanpredition.streamlit.app/" target="_blank" style="text-decoration: none; color: white;">
        <button style="background-color: #007bff; border: none; color: white; padding: 10px 20px; border-radius: 5px; cursor: pointer;">
            
            Visit Project
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

# st.markdown("""
# <div style="border: 2px solid #ccc; border-radius: 10px; padding: 15px; margin: 20px 0; background-color: #f9f9f9;">
#     <h3 style="color: #333;">Shreyas Project</h3>
#     <p style="color: #555;">Click this card for customer churn predition Projects</p>
#     <a href="https://customerchurnpredition.streamlit.app/" target="_blank" style="text-decoration: none; color: white;">
#         <button style="background-color: #007bff; border: none; color: white; padding: 10px 20px; border-radius: 5px; cursor: pointer;">

#                Visit Project
#           </button>
#     </a>
# </div>
# """, unsafe_allow_html=True)

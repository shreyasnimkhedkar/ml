import streamlit as st
from streamlit_card import card



st.title("WELCOME TO SHREYAS NIMKHEDKAR PROJECTS")

st.title("Introduction:")
st.write('''
Hello, I am Shreyas Nimkhedkar, a passionate and skilled professional specializing in Machine Learning, Python, MySQL, and Power BI. 
My portfolio showcases projects that combine data analysis, machine learning, and visualization techniques to deliver actionable 
insights and innovative solutions.
''')

st.title("Areas of Expertise:")
st.write('''
1. Machine Learning: Building predictive models and data-driven solutions using supervised, unsupervised, and ensemble techniques.
2. Python: Expertise in data preprocessing, automation, and statistical analysis using libraries like Pandas, NumPy, scikit-learn, and Matplotlib.
3. MySQL: Proficient in designing and querying databases, performing ETL operations, and managing relational datasets.
4. Power BI: Developing intuitive dashboards to visualize key business metrics and insights effectively.
''')


card(
    title="Shreyas Project",
    text="click this card for Python Projects",
    url = "https://customerchurnpredition.streamlit.app/",
)

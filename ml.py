import streamlit as st

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

# Custom Card-Like Design
st.markdown("""
<div style="border: 2px solid #ccc; border-radius: 10px; padding: 15px; margin: 20px 0; background-color: #f9f9f9;">
    <h3 style="color: #333;">Shreyas Project</h3>
    <p style="color: #555;">Click this card for Python Projects</p>
    <a href="https://customerchurnpredition.streamlit.app/" target="_blank" style="text-decoration: none; color: white;">
        <button style="background-color: #007bff; border: none; color: white; padding: 10px 20px; border-radius: 5px; cursor: pointer;">
            Visit Project
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

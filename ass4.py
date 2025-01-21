import streamlit as st

st.set_page_config(page_title="Personal Portfolio", layout="wide")

# Initialize the session state for menu selection
if "menu_choice" not in st.session_state:
    st.session_state.menu_choice = "Home"

# Create a horizontal menu using buttons
st.markdown(
    """
    <style>
        .menu {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-bottom: 20px;
            background-color:rgb(69, 147, 71);
            padding: 10px 0;
            border-radius: 10px;
        }
        .menu button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            font-weight: bold;
            border: none;
            padding: 10px 15px;
            cursor: pointer;
            border-radius: 5px;
        }
        .menu button:hover {
            background-color: #45a049;
        }
        .menu button.active {
            background-color: #2e7d32;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display the menu
st.markdown('<div class="menu">', unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
with col1:
    if st.button("Home"):
        st.session_state.menu_choice = "Home"
with col2:
    if st.button("About Me"):
        st.session_state.menu_choice = "About Me"
with col3:
    if st.button("Projects"):
        st.session_state.menu_choice = "Projects"
with col4:
    if st.button("Skills"):
        st.session_state.menu_choice = "Skills"
with col5:
    if st.button("Contact"):
        st.session_state.menu_choice = "Contact"
st.markdown('</div>', unsafe_allow_html=True)

# Get the current menu choice
choice = st.session_state.menu_choice

# Render the selected page
if choice == "Home":
    st.title("Welcome to My Portfolio")
    st.markdown(
        """
        <div style="text-align: center; font-size: 18px; line-height: 1.6;">
            Hi! I'm <strong>Asad Ali</strong>, a passionate <strong>Data Scientist</strong> dedicated to transforming data into actionable insights.<br>
            I specialize in <strong>machine learning</strong>, <strong>data visualization</strong>, and <strong>statistical analysis</strong> to solve real-world problems.
        </div>
        """,
        unsafe_allow_html=True
    )

    
    # Add the uploaded image
    

elif choice == "About Me":
    st.title("About Me")
    st.write("""
    - **Education:** [Data Science] from [University Of Central Punjab]
    - **Skills:** [Data Analysis, Python, Streamlit, Machine Learning, R, Power BI, and more]
    """)
elif choice == "Projects":
    st.title("Projects")
    
    # SQL-based Project
    st.write("### Project 1: Inventory Management System (SQL)")
    st.write("- Description: Designed an inventory management system using SQL to handle products, orders, and inventory levels efficiently.")
    st.write("- Technologies: SQL, MySQL Workbench")
    st.write("[Source Code](https://github.com/your-repo/sql-inventory-management)")

    # Python-based Project
    st.write("### Project 2: Web Scraper for Faculty Data (Python)")
    st.write("- Description: Built a web scraper using Python's Beautiful Soup library to extract faculty data from university websites.")
    st.write("- Technologies: Python, Beautiful Soup, Pandas")
    st.write("[Source Code](https://github.com/your-repo/python-web-scraper)")

    # Data Visualization Project
    st.write("### Project 3: Sales Dashboard (Data Visualization)")
    st.write("- Description: Created an interactive sales dashboard using Power BI and Python for visualizing monthly and yearly sales trends.")
    st.write("- Technologies: Python, Matplotlib, Power BI")
    st.write("[Source Code](https://github.com/your-repo/sales-dashboard)")

elif choice == "Skills":
    st.title("Technical Skills")
    st.write("- **Python:** 🟩🟩🟩🟩⬜ (4/5)")
    st.write("- **Data Analysis:** 🟩🟩🟩🟩⬜ (4/5)")
    st.write("- **Power BI:** 🟩🟩🟩🟩⬜ (4/5)")
elif choice == "Contact":
    st.title("Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        if st.form_submit_button("Submit"):
            st.success("Thank you for reaching out!")
    st.write("Find me on:")
    st.write("[LinkedIn](https://linkedin.com/in/your-profile)")
    st.write("[GitHub](https://github.com/your-profile)")

# Styling
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
            font-family: 'Arial', sans-serif;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #333;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)

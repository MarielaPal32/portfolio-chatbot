import streamlit as st

st.set_page_config(page_title="Mariela Palmieri Portfolio", layout="wide")

# ---------------- HEADER ----------------
st.title("💼 Mariela Palmieri")
st.markdown("### Data Analyst | Python | Power BI | Machine Learning")

st.markdown("""
Welcome to my data portfolio. Here you can explore my projects, tools, and experience
in data analysis, dashboards, and machine learning.
""")

# ---------------- KPIs ----------------
col1, col2 = st.columns(2)

# KPI principal
col1.metric("📊 Projects", "5")

# Tools en formato chico (PRO)
with col2:
    st.markdown("**🛠 Main Tools**")
    st.markdown(
        """
        <span style='font-size:12px; background-color:#eee; padding:4px 8px; border-radius:10px;'>Python</span>
        <span style='font-size:12px; background-color:#eee; padding:4px 8px;'>Power BI</span>
        <span style='font-size:12px; background-color:#eee; padding:4px 8px;'>Streamlit</span>
        """,
        unsafe_allow_html=True
    )

st.divider()

# ---------------- SIDEBAR ----------------
st.sidebar.title("🔎 Filters")

project_type = st.sidebar.selectbox(
    "Project Type",
    ["All", "Machine Learning", "Dashboard", "EDA"]
)

tech_filter = st.sidebar.selectbox(
    "Tool",
    ["All", "Python", "Power BI", "Streamlit", "Scikit-learn", "Pandas"]
)

# ---------------- PROJECTS ----------------
projects = [
    {
        "name": "🛢️ Texas Utility Captstone",
        "type": "EDA",
        "tech": ["Python", "Pandas", "Power BI"],
        "desc": "EDA + interactive Power BI dashboard with KPIs and trends.",
        "details": """
        ✔ Exploratory Data Analysis with Python  
        ✔ Data cleaning and pattern detection  
        ✔ Power BI dashboard with KPIs and regional insights  
        """,
        "link": "https://github.com/MarielaPal32/texas-utility-capstone"
    },
    {
        "name": "📈 Gold Dashboard",
        "type": "Dashboard",
        "tech": ["Power BI"],
        "desc": "Financial dashboard analyzing gold market trends.",
        "details": """
        ✔ Time series analysis  
        ✔ KPI tracking  
        ✔ Built in Power BI  
        """,
        "link": "https://github.com/MarielaPal32/gold-market-dashboard"
    },
    {
        "name": "🤖 Titanic ML",
        "type": "Machine Learning",
        "tech": ["Python", "Scikit-learn"],
        "desc": "ML model predicting survival.",
        "details": """
        ✔ Feature engineering  
        ✔ Model training  
        ✔ Performance evaluation  
        """,
        "link": "https://github.com/MarielaPal32/Titanic"
    },
    {
        "name": "🎬 Netflix App",
        "type": "EDA",
        "tech": ["Python", "Pandas", "Streamlit"],
        "desc": "Interactive Streamlit dashboard for Netflix data.",
        "details": """
        ✔ Filters by genre, year, country  
        ✔ Dynamic visualizations  
        ✔ Interactive app with Streamlit  
        """,
        "link": "https://github.com/MarielaPal32/Netflix"
    },
    {
        "name": "🎮 Video Games Analysis",
        "type": "EDA",
        "tech": ["Python", "Pandas"],
        "desc": "Analysis of gaming industry trends.",
        "details": """
        ✔ Sales analysis by region  
        ✔ Trends by platform and genre  
        """,
        "link": "https://github.com/MarielaPal32/Videojuegos"
    },
]

# ---------------- FILTER LOGIC ----------------
filtered_projects = []

for p in projects:
    if project_type != "All" and p["type"] != project_type:
        continue
    if tech_filter != "All" and tech_filter not in p["tech"]:
        continue
    filtered_projects.append(p)

# ---------------- DISPLAY CARDS ----------------
st.subheader("🚀 Projects")

cols = st.columns(2)

for i, project in enumerate(filtered_projects):
    with cols[i % 2]:
        st.container(border=True)

        st.markdown(f"### {project['name']}")
        st.markdown(project["desc"])

        st.markdown(
    " ".join([f"<span style='font-size:12px; background-color:#eee; padding:4px 8px; border-radius:10px; margin-right:5px;'>{t}</span>" for t in project["tech"]]),
    unsafe_allow_html=True
    )

        with st.expander("See more"):
            st.markdown(project["details"])

        st.link_button("🔗 View Project", project["link"])

# ---------------- CHATBOT DEMO ----------------
st.divider()
st.subheader("💬 Ask me (Demo Assistant)")

user_input = st.text_input("Ask something about me:")

if user_input:
    if "power bi" in user_input.lower():
        st.success("I build executive dashboards using Power BI with business KPIs.")

    elif "python" in user_input.lower():
        st.success("I use Python for data analysis, automation, and ML models.")

    elif "streamlit" in user_input.lower():
        st.success("I develop interactive data apps using Streamlit.")

    elif "experience" in user_input.lower():
        st.success("Experience in EDA, dashboards, and machine learning projects.")

    else:
        st.info("Great question! Connect with me on LinkedIn for more details: https://www.linkedin.com/in/mariela-palmieri/")
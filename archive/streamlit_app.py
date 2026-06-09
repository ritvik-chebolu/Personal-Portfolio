import streamlit as st
import os
import base64
import re

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="Ritvik Chebolu - Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Load Custom Stylesheet
if os.path.exists("style.css"):
    with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Inject FontAwesome Icons
st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">',
    unsafe_allow_html=True
)

def clean_html(html_str):
    """Strips all leading whitespace on every line to prevent Streamlit from rendering markdown code blocks."""
    return re.sub(r'^[ \t]+', '', html_str, flags=re.MULTILINE)

# Helper function to get base64 encoded image
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    return ""

# Helper to render section headers
def render_section_header(title, icon_class, element_id):
    st.markdown(clean_html(f"""
    <div id="{element_id}" class="section-header animate-fade-in delay-1">
        <i class="{icon_class}"></i> {title}
    </div>
    """), unsafe_allow_html=True)

# Helper to render cards
def render_card(title, subtitle, date_str, bullets, delay_class="delay-2"):
    bullet_html = "".join([f"<li>{b}</li>" for b in bullets])
    content_html = f"<ul>{bullet_html}</ul>" if bullets else ""
    st.markdown(clean_html(f"""
    <div class="custom-card animate-fade-in {delay_class}">
        <div class="card-header">
            <div class="card-title-group">
                <h3 class="card-title">{title}</h3>
                <div class="card-subtitle">{subtitle}</div>
            </div>
            <span class="card-date">{date_str}</span>
        </div>
        <div class="card-content">
            {content_html}
        </div>
    </div>
    """), unsafe_allow_html=True)

# Helper to render projects
def render_project_card(title, date_str, description, tags, link_url="", link_text="", delay_class="delay-2"):
    tag_html = "".join([f'<span class="project-tag">{t}</span>' for t in tags])
    footer_html = ""
    if link_url and link_text:
        footer_html = f"""
        <div class="project-footer">
            <div class="project-tags">{tag_html}</div>
            <a href="{link_url}" target="_blank" class="btn-card-link">
                {link_text} <i class="fas fa-external-link-alt"></i>
            </a>
        </div>
        """
    else:
        footer_html = f"""
        <div class="project-footer" style="border-top: none; padding-top: 0;">
            <div class="project-tags">{tag_html}</div>
        </div>
        """
        
    st.markdown(clean_html(f"""
    <div class="custom-card animate-fade-in {delay_class}">
        <div class="card-header">
            <h3 class="card-title">{title}</h3>
            <span class="card-date">{date_str}</span>
        </div>
        <div class="card-content">
            <p style="margin: 0 0 12px 0;">{description}</p>
            {footer_html}
        </div>
    </div>
    """), unsafe_allow_html=True)

# Helper to render skills
def render_skills_section(skills_dict):
    groups_html = ""
    for category, items in skills_dict.items():
        icon_class = "fas fa-code"
        if category == "Technologies":
            icon_class = "fas fa-laptop-code"
        elif category == "Libraries":
            icon_class = "fas fa-cubes"
            
        badges = "".join([f'<span class="skill-badge">{s}</span>' for s in items])
        groups_html += f"""
        <div class="skills-group">
            <div class="skills-group-title"><i class="{icon_class}"></i> {category}</div>
            <div class="skills-badges-container">
                {badges}
            </div>
        </div>
        """
    st.markdown(clean_html(f"""
    <div class="skills-container animate-fade-in delay-2">
        {groups_html}
    </div>
    """), unsafe_allow_html=True)

# Helper to render certifications
def render_certs_section(certs_groups, all_certs_link=""):
    grid_items = ""
    for issuer, certs in certs_groups.items():
        list_items = "".join([f"<li>{c}</li>" for c in certs])
        grid_items += f"""
        <div class="cert-card">
            <div class="cert-issuer">{issuer}</div>
            <ul class="cert-list">
                {list_items}
            </ul>
        </div>
        """
    
    link_html = ""
    if all_certs_link:
        link_html = f"""
        <div style="text-align: center; margin-top: 25px;">
            <a href="{all_certs_link}" target="_blank" class="btn-credentials">
                <i class="fas fa-certificate"></i> View All Credentials & Certificates
            </a>
        </div>
        """
        
    st.markdown(clean_html(f"""
    <div class="certs-grid animate-fade-in delay-2">
        {grid_items}
    </div>
    {link_html}
    """), unsafe_allow_html=True)

# Helper to render summary/highlights
def render_summary_section(highlights):
    list_items = ""
    icons = [
        "fas fa-graduation-cap",
        "fas fa-briefcase",
        "fas fa-briefcase",
        "fas fa-chalkboard-teacher",
        "fas fa-university",
        "fas fa-chess"
    ]
    for i, item in enumerate(highlights):
        icon = icons[i] if i < len(icons) else "fas fa-check"
        list_items += f"""
        <li style="display: flex; align-items: flex-start; gap: 12px; margin-bottom: 12px;">
            <i class="{icon}" style="color: #6366f1; margin-top: 4px; font-size: 1.05rem; width: 20px; text-align: center;"></i>
            <span style="color: #a1a1aa; font-size: 0.95rem; line-height: 1.5;">{item}</span>
        </li>
        """
    st.markdown(clean_html(f"""
    <div class="custom-card animate-fade-in delay-3" style="margin-top: 25px;">
        <h3 class="card-title" style="margin-bottom: 18px; font-size: 1.25rem;">
            <i class="fas fa-star" style="color: #6366f1; margin-right: 8px;"></i> Professional Highlights
        </h3>
        <ul style="list-style: none; padding: 0; margin: 0;">
            {list_items}
        </ul>
    </div>
    """), unsafe_allow_html=True)

# Helper to render contact me
def render_contact_section(email_address, linkedin_url):
    st.markdown(clean_html(f"""
    <div class="custom-card contact-card animate-fade-in delay-2">
        <h3 class="contact-title">Let's Build Something Great!</h3>
        <p class="contact-text">
            I am always open to discussing new opportunities, project collaborations, or just talking about Data Science and Analytics. Feel free to connect!
        </p>
        <div class="contact-buttons">
            <a href="mailto:{email_address}" class="social-button">
                <i class="fas fa-envelope"></i> Email Me
            </a>
            <a href="{linkedin_url}" target="_blank" class="social-button">
                <i class="fab fa-linkedin"></i> LinkedIn
            </a>
        </div>
    </div>
    """), unsafe_allow_html=True)

# ----------------- LAYOUT GENERATION -----------------

# Desktop Top Navigation
st.markdown(clean_html("""
<!-- Top Navigation Bar -->
<div class="top-nav">
    <a href="#" class="nav-brand">Ritvik Chebolu</a>
    <div class="nav-links">
        <a href="#education" class="nav-link">Education</a>
        <a href="#skills" class="nav-link">Skills</a>
        <a href="#experience" class="nav-link">Experience</a>
        <a href="#projects" class="nav-link">Projects</a>
        <a href="#certifications" class="nav-link">Certifications</a>
        <a href="#responsibility" class="nav-link">Responsibilities</a>
        <a href="#achievements" class="nav-link">Achievements</a>
        <a href="#contact" class="nav-link">Contact</a>
    </div>
</div>
"""), unsafe_allow_html=True)

# Hero Section
img_b64 = get_base64_image("circle_cropped.png")
avatar_html = f'<img src="data:image/png;base64,{img_b64}" class="hero-avatar" alt="Ritvik Chebolu">' if img_b64 else ''

st.markdown(clean_html(f"""
<div class="hero-container animate-fade-in delay-1">
    <div class="hero-content">
        <h1 class="hero-name">Ritvik Chebolu</h1>
        <div class="hero-subtitle">Analytics Engineer at Wayfair | M.Sc. in Data Science</div>
        <div class="hero-bio">
            M.Sc. in Data Science graduate from Rochester Institute of Technology (RIT) and B.Tech. Mechanical Engineering from IIT Dharwad. Passionate chess player, athlete, and builder of data-driven forecasting algorithms and analytics workflows.
        </div>
        <div class="social-links">
            <a href="https://www.linkedin.com/in/ritvik-chebolu" target="_blank" class="social-button">
                <i class="fab fa-linkedin"></i> LinkedIn
            </a>
            <a href="https://github.com/ritvik-chebolu" target="_blank" class="social-button">
                <i class="fab fa-github"></i> GitHub
            </a>
            <a href="https://bit.ly/gdrive-resume" target="_blank" class="social-button">
                <i class="fas fa-file-pdf"></i> Resume
            </a>
            <a href="https://ritvikchebolu.substack.com" target="_blank" class="social-button">
                <i class="fas fa-pen-nib"></i> Substack
            </a>
            <a href="https://twitter.com/ritvikteja" target="_blank" class="social-button">
                <i class="fab fa-twitter"></i> Twitter
            </a>
        </div>
    </div>
    <div class="hero-avatar-container">
        {avatar_html}
    </div>
</div>
"""), unsafe_allow_html=True)

# Professional Highlights Summary
highlights_data = [
    "Analytics Engineer at Wayfair",
    "Ex-Data Scientist at Carrier Corporation",
    "Data Science graduate student at Rochester Institute of Technology, New York, USA",
    "Dean's List 2024 at RIT",
    "Bachelor's degree from Indian Institute of Technology Dharwad (IIT Dharwad)",
    "A chess geek who also loves playing Football(Soccer), Badminton, Basketball, Cricket and Ping Pong"
]
render_summary_section(highlights_data)

# Education
render_section_header("Education", "fas fa-graduation-cap", "education")
render_card(
    "Master of Science in Data Science",
    "Rochester Institute of Technology, New York",
    "Aug 2021 - May 2024",
    [
        "<strong>GPA: 3.70</strong>",
        "Coursework: Applied Data Science, Information Retrieval and Text Mining, Software Engineering for Data Science, Non-Relational Data Management, Database Design Implementation, Data Management and Analytics, Foundations of Data Science and Analytics, Applied Statistics, Software Construction, Visual Analytics"
    ],
    delay_class="delay-2"
)
render_card(
    "Bachelor of Technology in Mechanical Engineering",
    "Indian Institute of Technology Dharwad, Karnataka, India",
    "Aug 2017 - May 2021",
    [
        "<strong>GPA: 3.88</strong>",
        "Relevant Coursework: Calculus, Linear Algebra, Ordinary Differential Equations, Data Analysis, Numerical Analysis",
        "Research work in the field of computational advanced manufacturing"
    ],
    delay_class="delay-3"
)

# Skills
render_section_header("Skills & Expertise", "fas fa-laptop-code", "skills")
skills_data = {
    "Programming": ["Python", "SQL", "Java", "R", "C++", "MongoDB", "Neo4j", "JavaScript", "PySpark"],
    "Technologies": ["GCP", "AWS", "GBQ", "Snowflake", "Airflow", "dbt", "Looker", "Tableau", "Excel", "MySQL", "PowerBI", "Microsoft Office", "Android Studio"],
    "Libraries": ["TensorFlow", "Keras", "Scikit Learn", "OpenCV", "Streamlit", "Seaborn", "plotly", "Pandas", "NumPy", "ggplot2", "Beautiful Soup"]
}
render_skills_section(skills_data)

# Experience
render_section_header("Professional Experience", "fas fa-briefcase", "experience")
render_card(
    "Analytics Engineer",
    "Wayfair",
    "July 2023 - Present",
    [
        "Developed and optimized algorithms for the Outlet store Pricing tool and Inventory Management (Operations) forecasting, increasing the quantity on hand by <strong>10%</strong> and revenue generated by <strong>15%</strong> on a weekly basis.",
        "Utilized inventory forecasting analytics to yield a <strong>24% improvement</strong> in supply chain efficiency, resulting in a monthly cost savings of <strong>$100k</strong> in inventory management.",
        "Set up an analytics workflow to extract Point of Sales data with APIs, setting up KPI dashboards and sales reports that were used to make data-driven decisions that improved outlet store operations."
    ]
)
render_card(
    "Auxiliary Services Analyst",
    "RIT",
    "May 2023 - June 2023",
    [
        "Cleaning duplicated data records from the RIT Dining Services database for demand forecasting.",
        "Extending Technical Support to the dining cafes by modifying their software to create, update and delete items from the menus.",
        "Developing an end-to-end framework to set up kiosks in dining areas, and assist with hardware and software installation."
    ]
)
render_card(
    "Graduate Teaching Assistant",
    "RIT",
    "Jan 2023 - May 2023",
    [
        "Teaching Assistant for the courses <code>Database Design Implementation</code> (ISTE 608) and <code>Data Modeling</code> (ISTE 230) at RIT.",
        "Grading assignments, holding office hours, and assisting <strong>50 students</strong> with their coursework."
    ]
)
render_card(
    "Junior Machine Learning Engineer",
    "Omdena - (Open Source Contribution)",
    "Dec 2022 - Jan 2023",
    [
        "Contributed to the development of a Recommendation Engine to create a self learning user experience with relevant chess puzzles for beginners to mid-level players on the ChessX platform.",
        "Developed a Machine Learning model using player stats and game history in a vectorized format to match with the most relevant puzzles and game analysis."
    ]
)
render_card(
    "Data Scientist",
    "Carrier Corporation, Pittsford, New York",
    "May 2022 - Nov 2022",
    [
        "Developing and formulating a problem statement by investigation to identify user pain points and decrease customer's investment in security personnel by about <strong>$175k annually</strong>.",
        "Leveraging data science methodologies to deploy machine learning models which reduce false alarm notifications in security systems by around <strong>38%</strong>.",
        "Worked with the product and business teams, and collaborated with customer's for direct feedback on pain-points to develop an analytical/predictive model using LSTM (Recurrent Neural Network) and a time-series k-means clustering algorithm to detect potential security threats in buildings.",
        "Analyzing a <strong>330 GB database</strong> consisting of a customer's live security monitoring system data collected and utilizing cloud architecture (AWS) to store, clean, process, analyze, transform, predict and finally deploy a machine learning model into production.",
        "Predictive analytics for device health and strategize maintenance shutdowns for security devices and systems."
    ]
)
render_card(
    "Thermal Engineering Intern",
    "Visakhapatnam Steel Plant, India",
    "July 2019",
    [
        "Dashboard analytics from turbine blades lead to a <strong>12% increase</strong> in operational efficiency in terms of response time.",
        "Analysis of variation of blade temperature over time for steam and gas turbines.",
        "Inferred and drew plots of theoretical velocity profiles and turbine blade temperatures at different lengths of turbines to validate the data with simulation results from measurement systems.",
        "This internship was closely linked to my previous internship at BHEL Hyderabad because BHEL Hyderabad deals with the manufacturing and assembly phase of Steam turbines whereas this internship throws light on the inner workings (control and operation) of Steam and Gas Turbines and the associated power generation aspects."
    ]
)
render_card(
    "Steam Turbine Engineering Intern",
    "Bharat Heavy Electronics Ltd, Hyderabad, India",
    "May 2019",
    [
        "Inferential analysis of blade profile to suggest a <strong>3% reduction</strong> in fluid drag for <strong>1.4% decrement</strong> in overall thermal loss.",
        "Analysis of the variation in blade profiles of a turbine over length for various turbine capacities to examine the flow rates, temperature distribution and stress-strain curves from theoretical data.",
        "Understanding the inner workings and control of steam turbines of different capacities and cross-validate their operational parameters with real-time data collected from testing sensors."
    ]
)
render_card(
    "Manufacturing Engineering Intern",
    "Visakhapatnam Steel Plant, India",
    "Dec 2018",
    [
        "Repair analysis for a green sand casting material to replace with a material to speed up molding by <strong>13 seconds/m³</strong>.",
        "Repair analysis for a torpedo ladle car used to carry molten steel from a blast furnace.",
        "Mechanics involved with part manufacture and assembly fixture for materials with varying compositions and to determine the best material in terms of stress and fatigue levels."
    ]
)

# Projects
render_section_header("Featured Projects", "fas fa-project-diagram", "projects")
render_project_card(
    "National Hockey League Database Application Design",
    "May 2023",
    "Developed an end-to-end database application with views, reports, forms and dashboards to store and display information about NHL season games.",
    ["Database Application", "SQL", "Dashboard", "Reports"]
)
render_project_card(
    "Sequence Classification using NLP",
    "Mar 2022",
    "Classifying user's input statements based on their polarity and subjectivity scores to get a sense of the user's expression. Built with TextBlob library built on NLTK which has a predefined set of words classified as positive, negative and neutral along with a score assigned to each tokenized word.",
    ["NLP", "NLTK", "TextBlob", "Sentiment Analysis", "Streamlit"],
    "https://sequence-classification-nlp.streamlitapp.com/",
    "Sentiment Analysis Web App"
)
render_project_card(
    "Visual Analytics 2019 (VAST) Challenge",
    "Mar 2022",
    "A visual analytics approach to solve a crisis management problem, carry rescue operations and address issues reported in a city. Providing timely updates to rescue teams using interactive radar time-series plots and tableau dashboards for real-time city surveillance and understanding the user (citizens) pain-points from a remote location.",
    ["Visual Analytics", "Crisis Management", "Tableau", "Time-series"],
    "https://ritvik-chebolu.github.io/VAST-2019-MC1/",
    "Disaster Management Webpage"
)
render_project_card(
    "Acute Ischemic Stroke Prediction",
    "Dec 2021",
    "Predicted patient's stroke severity based on their prior medical history and biological details. A Voting Classifier Ensemble model was used to decrease bias and variance, and also fine-tuned the model using GridSearchCV to achieve an accuracy of <strong>97.5%</strong>. Gathered primary patient data from an Indian Government hospital to train several models and understand their performance metrics on the dataset.",
    ["Machine Learning", "Ensemble Methods", "Voting Classifier", "GridSearchCV", "Healthcare"],
    "https://github.com/ritvik-chebolu/Acute-Ischemic-Stroke-Prediction",
    "GitHub Repo"
)
render_project_card(
    "User Feedback Sentiment Analysis",
    "Dec 2021",
    "Built a user feedback evaluation system using python. Statistical Natural Language Processing using Natural Language Toolkit library (NLTK) to analyze user feedback and determine if they make a positive, negative or neutral sense based on sentiment and polarity scores.",
    ["NLP", "NLTK", "Sentiment Analysis", "Python"],
    "https://github.com/ritvik-chebolu/Feedback-Sentiment-Analysis",
    "GitHub Repo"
)
render_project_card(
    "Customer Behavior Pattern Analysis for Revenue Generation",
    "Nov 2021",
    "Assembled a Tableau dashboard to analyze revenue generation using data on customer behavior and purchase patterns to identify growth opportunities and supply chain trends.",
    ["Tableau Dashboard", "Business Intelligence", "Revenue Analysis", "Customer Behavior"],
    "https://public.tableau.com/app/profile/ritvik7660/viz/CustomerRevenueAnalysis_16727974077450/RevenueAnalysis",
    "Tableau Dashboard"
)
render_project_card(
    "LinkedIn Social Media Analytics",
    "May 2021",
    "Marketing analytics for the LinkedIn social media page of FestMan. Built a dashboard to draw inferences from the LinkedIn page data in the year 2020 to derive insights about their followers/visitors counts and click through rate.",
    ["Marketing Analytics", "Tableau", "Social Media", "CTR Analysis"],
    "https://public.tableau.com/app/profile/ritvik4126/viz/FestMan05-20-2021/Inferences",
    "Tableau Dashboard"
)
render_project_card(
    "Behavioral Analysis of Shape Memory Alloys for 4D Printing",
    "May 2021",
    "Advanced manufacturing using shape shifting alloys to study the thermal and mechanical cycles of a Nitinol wire. Performed experiments to collect primary data for a 3 point mechanical bending system, cleaned and analyzed datasets using Microsoft Excel to draw inferences based on stress-strain curves for different temperature distributions to distinguish between two material compositions. Formulated a mathematical model to determine the stress-strain relation for the three-point bending mechanical system.",
    ["Research Project", "4D Printing", "Excel", "Nitinol", "Mathematical Modeling"],
    "https://drive.google.com/drive/folders/1-YI1nSfaayxFkQvQMFZIia3nRsu2A11J?usp=sharing",
    "Google Drive Folder"
)

# Courses and Certifications
render_section_header("Courses & Certifications", "fas fa-certificate", "certifications")

st.markdown(clean_html("""
<div class="custom-card animate-fade-in delay-2" style="margin-bottom: 20px;">
    <h4 class="card-title" style="font-size: 1.05rem; margin-bottom: 10px;">
        <i class="fas fa-book" style="color: #6366f1; margin-right: 8px;"></i> Relevant Coursework & Expertise
    </h4>
    <p style="margin: 0; font-size: 0.9rem; line-height: 1.6; color: #a1a1aa;">
        Prompt Engineering for Developers, Visual Analytics, Database Design Implementation, Software Construction, 
        Foundations of Data Science and Analytics, Applied Statistics, Computer Programming using C++, Calculus, 
        Linear Algebra, Ordinary Differential Equations, Data Analysis, Numerical Analysis, Probability and Statistics.
    </p>
</div>
"""), unsafe_allow_html=True)

certs_data = {
    "AWS & Scrum": [
        "AWS Technical Essentials Training",
        "Professional Scrum Master Certification (Carrier)"
    ],
    "LinkedIn: AI & NLP": [
        "Advanced AI: Transformers for NLP using Large Language Models",
        "Transformers: Text Classification for NLP using BERT"
    ],
    "LinkedIn: Data & SQL": [
        "Advanced SQL for Data Scientists",
        "Master SQL for Data Science",
        "SQL: Tips, Tricks and Techniques",
        "SQL: Data Reporting and Analysis",
        "SQL Essential Training",
        "Presto Essentials: Data Science",
        "Learning SQL Programming"
    ],
    "LinkedIn: Stats & Math": [
        "Statistics Foundations",
        "Probability",
        "Essential Math for Machine Learning",
        "Building Analytical Skills with Statistical Analysis",
        "Introduction to Data Science"
    ],
    "LinkedIn: Python & Viz": [
        "Python for Data Science: Tips, Tricks and Techniques",
        "Python for Data Visualization",
        "Data Analytics: Dashboards vs. Data Stories",
        "Data Analytics: Graph Analytics",
        "Data Visualization: Storytelling",
        "Data Ethics - Managing private customer data"
    ],
    "IBM & GUVI Madras": [
        "Data Science Methodologies (IBM)",
        "Machine Learning with Python (IBM)",
        "Python for Data Science (IBM)",
        "Descriptive Statistics (GUVI - IIT Madras)",
        "Engineering Data Science Systems (GUVI - IIT Madras)",
        "Statistics (GUVI - IIT Madras)"
    ]
}

render_certs_section(certs_data, "https://drive.google.com/drive/folders/1zeoSvGmipYM5Hw2IStvybJilhFgNT0FR?usp=sharing")

# Positions of Responsibility
render_section_header("Positions of Responsibility", "fas fa-users-cog", "responsibility")
render_card(
    "Speaker Support Lead",
    "Open Data Science Conference (ODSC) West 2023",
    "Nov 2022",
    [
        "Helped set up speaker sessions for ODSC West 2023 along with other fun networking events for the attendees and speakers at the conference.",
        "Hosted the ODSC West '23 conference collaborating with the event staff to ensure speaker's readiness before talks."
    ]
)
render_card(
    "Public Relations and Outreach Coordinator",
    "Entrepreneurship Cell",
    "2018 - 2021",
    [
        "Sole point of contact to manage public relations with industry experts, guest speakers and university directors.",
        "Coordinate with Event Management team to host events, talks, competitions and entrepreneurial activities.",
        "Led and developed the <a href='https://www.iitdh.ac.in/iic/' target='_blank' style='color: #6366f1; text-decoration: none;'>Institute Innovation Council at IIT Dharwad</a> since its formation in 2018."
    ]
)
render_card(
    "Class Representative",
    "Undergraduate Program",
    "2017 - 2021",
    [
        "Managed the class schedules and a Mechanical Engineering undergraduate degree program.",
        "Co-ordinated with the Dean, professors and students to organize academic and non-academic events."
    ]
)
render_card(
    "Formula Student (FSAE)",
    "Formula Bharat",
    "2018 - 2020",
    [
        "Electrical team lead directly managing a team to work on the inner harness and wiring for all electrical elements in the car.",
        "Co-ordinated with mechanical and powertrain teams to integrate telemetry and data acquisition systems."
    ]
)
render_card(
    "Career Development Cell Volunteer",
    "IIT Dharwad",
    "Aug 2020",
    [
        "Hosted Career events for undergraduate students to help build connections and establish a network with industry professionals."
    ]
)

# Activities and Achievements
render_section_header("Activities & Achievements", "fas fa-trophy", "achievements")
st.markdown(clean_html("""
<div class="custom-card animate-fade-in delay-2">
    <ul class="cert-list" style="margin: 0; font-size: 0.95rem; line-height: 1.6;">
        <li style="margin-bottom: 10px;">Runner's Up for the Men's Doubles category in Intramurals Badminton Tournament (an RIT league) in November 2022 and chosen to be a Varsity Athlete until the 2023 season.</li>
        <li style="margin-bottom: 10px;">Bagged 3rd for the Men's Doubles category in Intramurals Badminton Tournament (an RIT league) in April 2022.</li>
        <li style="margin-bottom: 10px;">Achieved 4th place in DevHack 2.0 (an annual tech-fest hackathon at IIT Dharwad) for designing a "Smart Closet" that sanitizes and dries laundry in a closet space.</li>
        <li style="margin-bottom: 10px;">Ranked 8th in Chess at the Inter IIT Sports Meet (national inter-college event) at Indian Institute of Technology, Madras, India in December 2017.</li>
        <li style="margin-bottom: 10px;">Placed 2nd twice in Inter-Departmental Football League at IIT Dharwad in 2018 and 2020.</li>
        <li style="margin-bottom: 10px;">College topper for one of the courses (Mechanical Measurements), which involves data collection and descriptive analysis of the data collected from various experiments and equipment.</li>
    </ul>
</div>
"""), unsafe_allow_html=True)

# Contact Me
render_section_header("Contact Me", "fas fa-paper-plane", "contact")
render_contact_section("ritvik.teja@gmail.com", "https://www.linkedin.com/in/ritvik-chebolu")

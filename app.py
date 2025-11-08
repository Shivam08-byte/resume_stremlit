import streamlit as st
from datetime import datetime
import base64
import csv
import os
from pathlib import Path
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import requests

# Page configuration
st.set_page_config(
    page_title="Shivam Malviya - Resume",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Email configuration function
def send_email_notification(name, email, subject, message):
    """Send email notification when form is submitted"""
    try:
        # Email configuration - use Streamlit secrets in production
        # For local testing, you can set these directly (not recommended for production)
        
        # Try to get from Streamlit secrets first (for deployment)
        try:
            smtp_server = st.secrets.get("SMTP_SERVER", "smtp.gmail.com")
            smtp_port = st.secrets.get("SMTP_PORT", 587)
            sender_email = st.secrets.get("SENDER_EMAIL", "")
            sender_password = st.secrets.get("SENDER_PASSWORD", "")
            receiver_email = st.secrets.get("RECEIVER_EMAIL", "shivammalviyawork@gmail.com")
        except:
            # Fallback for local development
            smtp_server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
            smtp_port = int(os.environ.get("SMTP_PORT", 587))
            sender_email = os.environ.get("SENDER_EMAIL", "")
            sender_password = os.environ.get("SENDER_PASSWORD", "")
            receiver_email = os.environ.get("RECEIVER_EMAIL", "shivammalviyawork@gmail.com")
        
        # Skip if email credentials not configured
        if not sender_email or not sender_password:
            return False, "Email credentials not configured"
        
        # Create message
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"New Contact Form Submission: {subject}"
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Reply-To"] = email
        
        # Create HTML email body
        html_body = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px; background-color: #f9f9f9; border-radius: 10px;">
                    <h2 style="color: #667eea; border-bottom: 3px solid #667eea; padding-bottom: 10px;">
                        📬 New Contact Form Submission
                    </h2>
                    
                    <div style="background: white; padding: 20px; border-radius: 8px; margin-top: 20px;">
                        <p><strong style="color: #667eea;">📅 Date & Time:</strong><br>
                        {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
                        
                        <p><strong style="color: #667eea;">👤 Name:</strong><br>
                        {name}</p>
                        
                        <p><strong style="color: #667eea;">📧 Email:</strong><br>
                        <a href="mailto:{email}" style="color: #667eea;">{email}</a></p>
                        
                        <p><strong style="color: #667eea;">📋 Subject:</strong><br>
                        {subject}</p>
                        
                        <p><strong style="color: #667eea;">💬 Message:</strong></p>
                        <div style="background: #f5f5f5; padding: 15px; border-radius: 5px; border-left: 4px solid #667eea;">
                            {message.replace(chr(10), '<br>')}
                        </div>
                    </div>
                    
                    <div style="margin-top: 20px; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 8px; text-align: center;">
                        <p style="color: white; margin: 0;">
                            <strong>Reply directly to this email to respond to {name}</strong>
                        </p>
                    </div>
                    
                    <p style="text-align: center; color: #999; font-size: 12px; margin-top: 20px;">
                        This email was sent from your portfolio contact form<br>
                        <a href="https://resumeshivammalviyawork.streamlit.app/" style="color: #667eea;">resumeshivammalviyawork.streamlit.app</a>
                    </p>
                </div>
            </body>
        </html>
        """
        
        # Attach HTML body
        msg.attach(MIMEText(html_body, "html"))
        
        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        
        return True, "Email sent successfully"
    
    except Exception as e:
        return False, f"Email error: {str(e)}"

# Google Sheets integration function
def save_to_google_sheets(name, email, subject, message):
    """Save form submission to Google Sheets"""
    try:
        # Try to get Google Sheets webhook URL from secrets
        try:
            sheets_url = st.secrets.get("GOOGLE_SHEETS_URL", "")
        except:
            sheets_url = os.environ.get("GOOGLE_SHEETS_URL", "")
        
        if not sheets_url:
            return False, "Google Sheets not configured"
        
        # Prepare data
        data = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "name": name,
            "email": email,
            "subject": subject,
            "message": message
        }
        
        # Send to Google Sheets via webhook/Apps Script
        response = requests.post(sheets_url, json=data, timeout=10)
        
        if response.status_code == 200:
            return True, "Saved to Google Sheets"
        else:
            return False, f"Sheets error: {response.status_code}"
    
    except Exception as e:
        return False, f"Sheets error: {str(e)}"

# Formspree integration function
def send_to_formspree(name, email, subject, message):
    """Send form submission to Formspree"""
    try:
        # Try to get Formspree endpoint from secrets
        try:
            formspree_url = st.secrets.get("FORMSPREE_ENDPOINT", "")
        except:
            formspree_url = os.environ.get("FORMSPREE_ENDPOINT", "")
        
        if not formspree_url:
            return False, "Formspree not configured"
        
        # Prepare data for Formspree
        data = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message,
            "_replyto": email,
            "_subject": f"Contact Form: {subject}"
        }
        
        # Send to Formspree
        response = requests.post(formspree_url, data=data, headers={"Accept": "application/json"}, timeout=10)
        
        if response.status_code == 200:
            return True, "Sent via Formspree"
        else:
            return False, f"Formspree error: {response.status_code}"
    
    except Exception as e:
        return False, f"Formspree error: {str(e)}"

# Custom CSS with animations and modern design
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main-header {
        font-size: 4rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0;
        animation: fadeInDown 1s ease-in;
    }
    
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-top: 0;
        animation: fadeInUp 1s ease-in;
    }
    
    .section-header {
        font-size: 2.2rem;
        font-weight: 600;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        border-bottom: 3px solid;
        border-image: linear-gradient(135deg, #667eea 0%, #764ba2 100%) 1;
        padding-bottom: 10px;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    
    .contact-info {
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 30px;
        padding: 20px;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border-radius: 15px;
        animation: fadeIn 1.5s ease-in;
    }
    
    .contact-info a {
        color: #667eea;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .contact-info a:hover {
        color: #764ba2;
        transform: scale(1.1);
    }
    
    .skill-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 10px 20px;
        margin: 5px;
        border-radius: 25px;
        font-weight: 500;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        animation: fadeInUp 0.5s ease-in;
    }
    
    .skill-badge:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    .experience-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 20px;
        border-left: 5px solid #667eea;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        animation: slideInLeft 0.5s ease-in;
    }
    
    .experience-card:hover {
        transform: translateX(10px);
        box-shadow: 0 8px 15px rgba(102, 126, 234, 0.3);
    }
    
    .project-card {
        background: linear-gradient(135deg, rgba(67, 160, 71, 0.05) 0%, rgba(56, 142, 60, 0.05) 100%);
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 20px;
        border-left: 5px solid #43A047;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        animation: slideInRight 0.5s ease-in;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(67, 160, 71, 0.3);
    }
    
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 15px rgba(102, 126, 234, 0.3);
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Streamlit specific overrides */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    div[data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .stProgress > div > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">✨ Shivam Malviya ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">🚀 Senior Software Engineer | 🤖 AI/ML Expert | ☁️ Cloud & Automation Specialist</p>', unsafe_allow_html=True)

# Contact Information
st.markdown("""
    <div class="contact-info">
        📧 shivammalviyawork@gmail.com | 📱 +91 7247380914 | 
        💼 <a href="https://www.linkedin.com/in/shivam-malviya-6981b8192/" target="_blank">LinkedIn</a> | 
        💻 <a href="https://github.com/Shivam08-byte" target="_blank">GitHub</a>
    </div>
    """, unsafe_allow_html=True)

# Tabs for different sections
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🎯 About", "💼 Experience", "🚀 Projects", "🛠️ Skills", "🎓 Education", "📬 Contact"])

with tab1:
    st.markdown('<p class="section-header">About Me</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
        ### 👋 Hello! I'm Shivam
        
        **Senior Software Engineer** and automation expert with strong expertise in **Python, Django, Azure**, 
        and database systems. Specialized in developing **AI/ML-driven solutions** and automating processes 
        using cloud technologies to optimize performance and scalability.
        
        💡 **What I Do:**
        - Build low-code/no-code ML pipeline tools
        - Design and deploy scalable cloud solutions on Azure Kubernetes
        - Develop Gen AI-based applications and data integration systems
        - Optimize database architectures for high-performance applications
        
        🎯 **My Approach:**
        - Focus on automation and efficiency
        - Follow Agile methodologies
        - Deliver solutions that scale and perform
        """)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <div style="width: 150px; height: 150px; margin: 0 auto; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 4rem; box-shadow: 0 8px 16px rgba(102, 126, 234, 0.4);">
                👨‍💻
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Years of Experience", "3+", "Growing 🌱")
    with col2:
        st.metric("Projects Completed", "10+", "Enterprise Scale 🎯")
    with col3:
        st.metric("Technologies", "25+", "Always learning 📚")
    with col4:
        st.metric("Performance Boost", "50%", "Data Pipelines ⚡")

with tab2:
    st.markdown('<p class="section-header">Work Experience</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="experience-card">
        <h3>💼 Senior Software Engineer 1</h3>
        <p><strong>🏢 HCL Soft, Noida, India</strong> | 📅 Aug 2022 - Present</p>
        <h4 style="color: #667eea; margin-top: 15px;">🚀 AION Project</h4>
        <ul>
            <li>�️ Developed a <strong>low-code/no-code ML pipeline tool</strong> backend using Python, Django, and SQLite, streamlining ML lifecycle management</li>
            <li>⚡ Engineered a data ingestion pipeline with a <strong>50% performance boost</strong> and implemented Univariate Forecasting and Data Augmentation for time series analytics</li>
            <li>☁️ Deployed the platform on <strong>Azure Kubernetes (K8s)</strong> with a load balancer, <strong>doubling operational efficiency</strong> during testing</li>
            <li>🎯 Designed and executed the <strong>Bring Your Own Model (BYOM)</strong> feature, integrating custom ML models seamlessly into the pipeline</li>
            <li>🤖 Developed a <strong>Gen AI-based document summarization</strong> feature for the GEM Portal, enabling efficient extraction of critical content</li>
            <li>🌍 Consulted on SX integration with BigFix SX, impacting operations in <strong>8 countries</strong> while ensuring compliance with international standards</li>
            <li>� Optimized database design for efficient handling of dataset and model metadata</li>
        </ul>
        <h4 style="color: #667eea; margin-top: 15px;">� Connector Framework</h4>
        <ul>
            <li>� Developed a secure data migration product for <strong>Jira, Confluence, Zendesk, and ServiceNow</strong> using NiFi, Java, and Docker</li>
            <li>🛡️ Implemented a role-based login system, <strong>increasing product security by 40%</strong></li>
            <li>⚡ Improved integration and deployment efficiency by <strong>30%</strong></li>
            <li>� Optimized NiFi flow scalability, reducing deployment times by <strong>25%</strong> and ensuring high availability for data pipelines</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="experience-card">
        <h3>💼 Programmer Analyst Trainee (Internship)</h3>
        <p><strong>🏢 Cognizant Technologies Solution, Pune, India</strong> | 📅 Jan 2022 - July 2022</p>
        <ul>
            <li>🌐 Proficient in front-end technologies including <strong>HTML, CSS, JavaScript, and ReactJS</strong></li>
            <li>☕ Skilled in server-side programming with <strong>Java</strong> and experienced in database management and caching solutions</li>
            <li>� Contributed to API integration, testing, and debugging in collaborative projects</li>
            <li>� Resolved bugs and provided technical support for critical systems in a support project</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown('<p class="section-header">Featured Projects</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="project-card">
            <h3>🤖 AION ML Pipeline Platform</h3>
            <p>Low-code/no-code ML pipeline tool for streamlined ML lifecycle management</p>
            <ul>
                <li>Built backend with Python, Django, SQLite</li>
                <li>Deployed on Azure Kubernetes with load balancer</li>
                <li>50% performance boost in data ingestion</li>
                <li>BYOM feature for custom ML model integration</li>
            </ul>
            <p><strong>Impact:</strong> Doubled operational efficiency during testing</p>
            <p><strong>Tech Stack:</strong> Python, Django, SQLite, Azure K8s, Docker</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="project-card">
            <h3>� Connector Framework</h3>
            <p>Secure data migration product for enterprise ITSM tools</p>
            <ul>
                <li>Supports Jira, Confluence, Zendesk, ServiceNow</li>
                <li>Role-based authentication system</li>
                <li>40% increase in product security</li>
                <li>25% reduction in deployment times</li>
            </ul>
            <p><strong>Impact:</strong> 30% improvement in integration efficiency</p>
            <p><strong>Tech Stack:</strong> NiFi, Java, Docker, PostgreSQL</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="project-card">
            <h3>� Gen AI Document Summarization</h3>
            <p>AI-powered document summarization feature for GEM Portal</p>
            <ul>
                <li>Extracts critical content efficiently</li>
                <li>Integrated with existing portal infrastructure</li>
                <li>Leverages generative AI models</li>
                <li>Real-time processing capabilities</li>
            </ul>
            <p><strong>Impact:</strong> Streamlined document review process</p>
            <p><strong>Tech Stack:</strong> Python, Generative AI, Django, FastAPI</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="project-card">
            <h3>� Univariate Forecasting & Data Augmentation</h3>
            <p>Time series analytics solution for predictive modeling</p>
            <ul>
                <li>Advanced forecasting algorithms</li>
                <li>Data augmentation techniques</li>
                <li>Real-time performance monitoring</li>
                <li>Scalable architecture</li>
            </ul>
            <p><strong>Impact:</strong> Enhanced prediction accuracy</p>
            <p><strong>Tech Stack:</strong> Python, Machine Learning, Azure, Django</p>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown('<p class="section-header">Technical Skills</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Programming Languages")
        languages = ["Python", "Java", "Shell Scripting", "JavaScript", "SQL"]
        st.markdown(" ".join([f'<span class="skill-badge">{skill}</span>' for skill in languages]), unsafe_allow_html=True)
        
        st.markdown("### Frameworks & Libraries")
        frameworks = ["Django", "FastAPI", "ReactJS", "NiFi", "TensorFlow"]
        st.markdown(" ".join([f'<span class="skill-badge">{fw}</span>' for fw in frameworks]), unsafe_allow_html=True)
        
        st.markdown("### Databases & Caching")
        databases = ["SQLite", "PostgreSQL", "Redis", "MySQL"]
        st.markdown(" ".join([f'<span class="skill-badge">{db}</span>' for db in databases]), unsafe_allow_html=True)
        
        st.markdown("### ITSM Tools")
        itsm = ["ServiceNow", "Jira", "Zendesk", "Confluence"]
        st.markdown(" ".join([f'<span class="skill-badge">{tool}</span>' for tool in itsm]), unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Cloud & DevOps")
        cloud = ["Azure", "Azure Kubernetes (AKS)", "Docker", "Kubernetes", "JMeter", "GitLab"]
        st.markdown(" ".join([f'<span class="skill-badge">{c}</span>' for c in cloud]), unsafe_allow_html=True)
        
        st.markdown("### Operating Systems")
        os_list = ["Windows", "Ubuntu", "Debian", "Linux"]
        st.markdown(" ".join([f'<span class="skill-badge">{os}</span>' for os in os_list]), unsafe_allow_html=True)
        
        st.markdown("### Specialized Skills")
        specialized = ["Machine Learning Pipelines", "Generative AI", "Data Augmentation", "Univariate Forecasting", "Docker Swarm"]
        st.markdown(" ".join([f'<span class="skill-badge">{s}</span>' for s in specialized]), unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📈 Skill Proficiency")
    
    skill_data = {
        "Python": 95,
        "Django": 90,
        "Azure & Kubernetes": 85,
        "Machine Learning": 85,
        "Docker": 85,
        "Database Design": 90,
        "Java": 75,
        "Generative AI": 80
    }
    
    for skill, level in skill_data.items():
        st.write(f"**{skill}**")
        st.progress(level / 100)

with tab5:
    st.markdown('<p class="section-header">Education & Certifications</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎓 Education")
        st.markdown("""
        **Bachelor of Engineering in Computer Science**  
        Sagar Institute of Research and Technology Excellence, Bhopal  
        📅 2018 - 2022
        
        **Key Focus Areas:**
        - Software Engineering
        - Data Structures & Algorithms
        - Database Management Systems
        - Machine Learning
        - Cloud Computing
        - Web Technologies
        """)
    
    with col2:
        st.markdown("### 📜 Certifications")
        st.markdown("""
        **🏆 Professional Certifications:**
        
        - **IBM Data Science Professional Certificate**  
          _IBM - Data Science & ML Fundamentals_
        
        - **The Complete SQL Bootcamp 2022**  
          _Advanced SQL & Database Management_
        
        - **Python for Data Science & Machine Learning Bootcamp**  
          _Data Analysis, ML, & Statistical Modeling_
        
        - **Python Solid Principles**  
          _Object-Oriented Design & Best Practices_
        """)
    
    st.markdown("---")
    
    st.markdown("### 🌟 Key Achievements")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="padding: 20px; background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%); border-radius: 15px; text-align: center;">
            <h2 style="color: #667eea; margin: 0;">50%</h2>
            <p style="margin: 5px 0;"><strong>Performance Boost</strong></p>
            <p style="font-size: 0.9rem; color: #666;">Data Ingestion Pipeline</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="padding: 20px; background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%); border-radius: 15px; text-align: center;">
            <h2 style="color: #667eea; margin: 0;">40%</h2>
            <p style="margin: 5px 0;"><strong>Security Increase</strong></p>
            <p style="font-size: 0.9rem; color: #666;">Connector Framework</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="padding: 20px; background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%); border-radius: 15px; text-align: center;">
            <h2 style="color: #667eea; margin: 0;">8+</h2>
            <p style="margin: 5px 0;"><strong>Countries</strong></p>
            <p style="font-size: 0.9rem; color: #666;">International Impact</p>
        </div>
        """, unsafe_allow_html=True)

with tab6:
    st.markdown('<p class="section-header">Get In Touch</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📬 Contact Form")
        st.write("Have a project in mind or want to connect? Drop me a message!")
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your Name *", placeholder="John Doe")
            email = st.text_input("Your Email *", placeholder="john@example.com")
            subject = st.selectbox(
                "Subject *",
                ["Job Opportunity", "Freelance Project", "Collaboration", "General Inquiry", "Other"]
            )
            message = st.text_area("Message *", placeholder="Tell me about your project or inquiry...", height=150)
            
            col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2])
            with col_btn1:
                submitted = st.form_submit_button("📤 Send Message", use_container_width=True)
            
            if submitted:
                if name and email and message:
                    # Track which methods succeeded
                    success_methods = []
                    failed_methods = []
                    
                    # 1. ALWAYS save to CSV (primary/fallback method)
                    csv_file = 'contact_submissions.csv'
                    file_exists = os.path.isfile(csv_file)
                    csv_saved = False
                    
                    try:
                        with open(csv_file, 'a', newline='', encoding='utf-8') as f:
                            writer = csv.writer(f)
                            if not file_exists:
                                writer.writerow(['Timestamp', 'Name', 'Email', 'Subject', 'Message'])
                            writer.writerow([
                                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                name,
                                email,
                                subject,
                                message
                            ])
                        csv_saved = True
                        success_methods.append("💾 CSV Database")
                    except Exception as e:
                        failed_methods.append(f"CSV: {str(e)}")
                    
                    # 2. Try to send email notification
                    email_sent, email_msg = send_email_notification(name, email, subject, message)
                    if email_sent:
                        success_methods.append("📧 Email Notification")
                    elif "not configured" not in email_msg.lower():
                        failed_methods.append(f"Email: {email_msg}")
                    
                    # 3. Try to save to Google Sheets
                    sheets_saved, sheets_msg = save_to_google_sheets(name, email, subject, message)
                    if sheets_saved:
                        success_methods.append("📊 Google Sheets")
                    elif "not configured" not in sheets_msg.lower():
                        failed_methods.append(f"Sheets: {sheets_msg}")
                    
                    # 4. Try to send via Formspree
                    formspree_sent, formspree_msg = send_to_formspree(name, email, subject, message)
                    if formspree_sent:
                        success_methods.append("📮 Formspree")
                    elif "not configured" not in formspree_msg.lower():
                        failed_methods.append(f"Formspree: {formspree_msg}")
                    
                    # Show success message
                    if csv_saved:
                        st.success(f"✅ Thank you, {name}! Your message has been received. I'll get back to you soon!")
                        st.balloons()
                        
                        # Show which methods worked
                        if success_methods:
                            success_text = " • ".join(success_methods)
                            st.info(f"""
                            **Message saved successfully!** 🎉
                            
                            **Saved via:** {success_text}
                            
                            Your contact details have been recorded and I'll respond within 24-48 hours.
                            """)
                        
                        # Show failures as warning (not error since CSV worked)
                        if failed_methods:
                            with st.expander("⚠️ Some backup methods failed (click to see details)"):
                                for method in failed_methods:
                                    st.warning(method)
                    else:
                        st.error("⚠️ Error saving message. Please try again or email me directly at shivammalviyawork@gmail.com")
                        if failed_methods:
                            for method in failed_methods:
                                st.error(method)
                else:
                    st.error("⚠️ Please fill in all required fields!")
    
    with col2:
        st.markdown("### 📞 Direct Contact")
        st.markdown("""<div style="padding: 20px; background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%); border-radius: 15px; margin-top: 10px;"><h4 style="color: #667eea;">📧 Email</h4><p><a href="mailto:shivammalviyawork@gmail.com" style="color: #667eea; text-decoration: none; font-weight: 500;">shivammalviyawork@gmail.com</a></p><h4 style="color: #667eea; margin-top: 20px;">📱 Phone</h4><p style="font-weight: 500;">+91 7247380914</p><h4 style="color: #667eea; margin-top: 20px;">💼 LinkedIn</h4><p><a href="https://www.linkedin.com/in/shivam-malviya-6981b8192/" target="_blank" style="color: #667eea; text-decoration: none; font-weight: 500;">Connect on LinkedIn</a></p><h4 style="color: #667eea; margin-top: 20px;">💻 GitHub</h4><p><a href="https://github.com/Shivam08-byte" target="_blank" style="color: #667eea; text-decoration: none; font-weight: 500;">Check out my projects</a></p></div>""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div style="padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white; text-align: center;">
            <h4 style="color: white; margin-top: 0;">⚡ Response Time</h4>
            <p style="font-size: 1.5rem; font-weight: bold; margin: 10px 0;">24-48 hrs</p>
            <p style="margin-bottom: 0;">I typically respond within 1-2 business days</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; padding: 20px;">
        <p>📱 This interactive resume was built with Streamlit</p>
        <p>© 2025 Shivam Malviya | Last Updated: November 2025</p>
    </div>
    """, unsafe_allow_html=True)

# Sidebar - Download Resume Option
with st.sidebar:
    st.markdown("### 📄 Resume Options")
    
    # Animated info box
    st.markdown("""
        <div style="padding: 15px; background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%); border-radius: 10px; border-left: 4px solid #667eea;">
            💡 <strong>Interactive Resume</strong><br>
            Explore different sections using the tabs above!
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### 📞 Quick Contact")
    st.markdown("""
    <div style="line-height: 2;">
        📧 <a href="mailto:shivammalviyawork@gmail.com" style="text-decoration: none; color: #667eea;">shivammalviyawork@gmail.com</a><br>
        📱 <strong>+91 7247380914</strong><br>
        💼 <a href="https://www.linkedin.com/in/shivam-malviya-6981b8192/" target="_blank" style="text-decoration: none; color: #667eea;">LinkedIn Profile</a><br>
        💻 <a href="https://github.com/Shivam08-byte" target="_blank" style="text-decoration: none; color: #667eea;">GitHub Portfolio</a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### 🌟 Highlights")
    st.markdown("""
        <div style="padding: 10px; margin: 5px 0; background: linear-gradient(135deg, rgba(102, 200, 71, 0.1) 0%, rgba(67, 160, 71, 0.1) 100%); border-radius: 8px; border-left: 3px solid #43A047;">
            ✅ 3+ years of experience
        </div>
        <div style="padding: 10px; margin: 5px 0; background: linear-gradient(135deg, rgba(102, 200, 71, 0.1) 0%, rgba(67, 160, 71, 0.1) 100%); border-radius: 8px; border-left: 3px solid #43A047;">
            ✅ Full-stack development
        </div>
        <div style="padding: 10px; margin: 5px 0; background: linear-gradient(135deg, rgba(102, 200, 71, 0.1) 0%, rgba(67, 160, 71, 0.1) 100%); border-radius: 8px; border-left: 3px solid #43A047;">
            ✅ AI/ML expertise
        </div>
        <div style="padding: 10px; margin: 5px 0; background: linear-gradient(135deg, rgba(102, 200, 71, 0.1) 0%, rgba(67, 160, 71, 0.1) 100%); border-radius: 8px; border-left: 3px solid #43A047;">
            ✅ Cloud architecture
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("📥 Download PDF Resume", use_container_width=True):
        st.balloons()
        st.info("🎉 PDF download feature - connect to your actual resume file!")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Contact form submissions viewer
    st.markdown("### 📨 Form Submissions")
    csv_file = 'contact_submissions.csv'
    if os.path.isfile(csv_file):
        try:
            import pandas as pd
            df = pd.read_csv(csv_file)
            st.metric("Total Messages", len(df))
            
            if st.button("👀 View Submissions", use_container_width=True):
                st.dataframe(df, use_container_width=True)
            
            # Download button for CSV
            with open(csv_file, 'rb') as f:
                st.download_button(
                    label="📥 Download Submissions CSV",
                    data=f,
                    file_name="contact_submissions.csv",
                    mime="text/csv",
                    use_container_width=True
                )
        except Exception as e:
            st.warning("No submissions yet")
    else:
        st.info("No messages received yet")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Fun stats
    st.markdown("### 📊 Fun Stats")
    st.markdown("""
        <div style="text-align: center; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
            <div style="font-size: 2rem; font-weight: bold;">🔥</div>
            <div style="font-size: 1.2rem; font-weight: bold;">100+</div>
            <div>Days of Coding Streak</div>
        </div>
    """, unsafe_allow_html=True)

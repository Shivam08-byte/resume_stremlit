import streamlit as st
from datetime import datetime
import base64

# Page configuration
st.set_page_config(
    page_title="Shivam Malviya - Resume",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
st.markdown('<p class="sub-header">🚀 Software Developer | 🤖 AI/ML Enthusiast | ☁️ Cloud Architect</p>', unsafe_allow_html=True)

# Contact Information
st.markdown("""
    <div class="contact-info">
        📧 shivammalviyawork@gmail.com | 📱 +91-XXXXXXXXXX | 
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
        
        Passionate software developer with expertise in building **scalable web applications** and **AI/ML solutions**. 
        Strong background in full-stack development, data analysis, and problem-solving. Committed to writing 
        clean, maintainable code and continuously learning new technologies.
        
        💡 **What I Love:**
        - Building impactful products that solve real problems
        - Exploring cutting-edge AI/ML technologies
        - Collaborating with talented teams
        - Open source contributions
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
        st.metric("Projects Completed", "15+", "And counting 🎯")
    with col3:
        st.metric("Technologies", "20+", "Always learning 📚")
    with col4:
        st.metric("Coffee Consumed", "∞", "Fuel for code ☕")

with tab2:
    st.markdown('<p class="section-header">Work Experience</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="experience-card">
        <h3>💼 Senior Software Developer</h3>
        <p><strong>🏢 Tech Solutions Inc.</strong> | 📅 Jan 2023 - Present</p>
        <ul>
            <li>🚀 Led development of a microservices-based e-commerce platform serving 100K+ users</li>
            <li>⚡ Implemented CI/CD pipelines reducing deployment time by 60%</li>
            <li>👥 Mentored junior developers and conducted code reviews</li>
            <li>🛠️ Technologies: Python, Django, React, PostgreSQL, AWS, Docker</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="experience-card">
        <h3>💼 Software Developer</h3>
        <p><strong>🏢 Digital Innovations Ltd.</strong> | 📅 Jun 2021 - Dec 2022</p>
        <ul>
            <li>🔧 Developed RESTful APIs and responsive web applications</li>
            <li>⚡ Optimized database queries improving application performance by 40%</li>
            <li>🤝 Collaborated with cross-functional teams using Agile methodologies</li>
            <li>🛠️ Technologies: Node.js, Express, MongoDB, React, Azure</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="experience-card">
        <h3>💼 Junior Developer</h3>
        <p><strong>🏢 StartUp Ventures</strong> | 📅 Jan 2020 - May 2021</p>
        <ul>
            <li>🌐 Built and maintained web applications using modern frameworks</li>
            <li>💳 Integrated third-party APIs and payment gateways</li>
            <li>📊 Participated in sprint planning and daily standups</li>
            <li>🛠️ Technologies: Python, Flask, JavaScript, MySQL</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown('<p class="section-header">Featured Projects</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="project-card">
            <h3>🤖 AI Chatbot Platform</h3>
            <p>Developed an intelligent chatbot using NLP and machine learning</p>
            <ul>
                <li>Built with Python, TensorFlow, and FastAPI</li>
                <li>Deployed on AWS with auto-scaling</li>
                <li>Handles 10K+ conversations daily</li>
            </ul>
            <p><strong>Tech Stack:</strong> Python, TensorFlow, FastAPI, Redis, PostgreSQL</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="project-card">
            <h3>📊 Data Analytics Dashboard</h3>
            <p>Real-time analytics dashboard for business intelligence</p>
            <ul>
                <li>Interactive visualizations with D3.js</li>
                <li>Real-time data processing pipeline</li>
                <li>Used by 500+ business users</li>
            </ul>
            <p><strong>Tech Stack:</strong> React, D3.js, Python, Apache Kafka, Elasticsearch</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="project-card">
            <h3>🛒 E-commerce Marketplace</h3>
            <p>Full-stack e-commerce platform with payment integration</p>
            <ul>
                <li>Secure payment processing with Stripe</li>
                <li>Admin dashboard for inventory management</li>
                <li>Mobile-responsive design</li>
            </ul>
            <p><strong>Tech Stack:</strong> Django, React, PostgreSQL, Redis, Stripe API</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="project-card">
            <h3>🔐 Authentication Service</h3>
            <p>Microservice for user authentication and authorization</p>
            <ul>
                <li>JWT-based authentication</li>
                <li>OAuth2 integration (Google, GitHub)</li>
                <li>Rate limiting and security features</li>
            </ul>
            <p><strong>Tech Stack:</strong> Node.js, Express, MongoDB, Redis, Docker</p>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown('<p class="section-header">Technical Skills</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Programming Languages")
        skills = ["Python", "JavaScript", "TypeScript", "Java", "SQL", "HTML/CSS"]
        st.markdown(" ".join([f'<span class="skill-badge">{skill}</span>' for skill in skills]), unsafe_allow_html=True)
        
        st.markdown("### Frameworks & Libraries")
        frameworks = ["Django", "Flask", "FastAPI", "React", "Node.js", "Express", "TensorFlow", "PyTorch"]
        st.markdown(" ".join([f'<span class="skill-badge">{fw}</span>' for fw in frameworks]), unsafe_allow_html=True)
        
        st.markdown("### Databases")
        databases = ["PostgreSQL", "MongoDB", "MySQL", "Redis", "Elasticsearch"]
        st.markdown(" ".join([f'<span class="skill-badge">{db}</span>' for db in databases]), unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Cloud & DevOps")
        cloud = ["AWS", "Azure", "Docker", "Kubernetes", "CI/CD", "GitHub Actions"]
        st.markdown(" ".join([f'<span class="skill-badge">{c}</span>' for c in cloud]), unsafe_allow_html=True)
        
        st.markdown("### Tools & Technologies")
        tools = ["Git", "Linux", "REST APIs", "GraphQL", "Microservices", "Agile/Scrum"]
        st.markdown(" ".join([f'<span class="skill-badge">{tool}</span>' for tool in tools]), unsafe_allow_html=True)
        
        st.markdown("### Soft Skills")
        soft = ["Problem Solving", "Team Collaboration", "Code Review", "Mentoring", "Communication"]
        st.markdown(" ".join([f'<span class="skill-badge">{s}</span>' for s in soft]), unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📈 Skill Proficiency")
    
    skill_data = {
        "Python": 90,
        "JavaScript": 85,
        "React": 80,
        "Django/Flask": 85,
        "SQL": 80,
        "AWS": 75,
        "Docker": 70,
        "Machine Learning": 65
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
        **Bachelor of Technology in Computer Science**  
        XYZ University | 2016 - 2020  
        CGPA: 8.5/10
        
        **Relevant Coursework:**
        - Data Structures & Algorithms
        - Database Management Systems
        - Web Technologies
        - Machine Learning
        - Software Engineering
        """)
    
    with col2:
        st.markdown("### 📜 Certifications")
        st.markdown("""
        - **AWS Certified Solutions Architect** - Amazon (2023)
        - **Professional Scrum Master I** - Scrum.org (2022)
        - **Machine Learning Specialization** - Coursera (2022)
        - **Full Stack Web Development** - Udemy (2021)
        - **Python for Data Science** - edX (2020)
        """)

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
                    st.success(f"✅ Thank you, {name}! Your message has been received. I'll get back to you soon!")
                    st.balloons()
                    
                    # Here you can add email functionality or save to a database
                    # For now, we'll just show a success message
                    
                    st.info(f"""
                    **Message Details:**
                    - **Name:** {name}
                    - **Email:** {email}
                    - **Subject:** {subject}
                    - **Message:** {message}
                    
                    _Note: In production, this would be sent via email or saved to a database._
                    """)
                else:
                    st.error("⚠️ Please fill in all required fields!")
    
    with col2:
        st.markdown("### 📞 Direct Contact")
        st.markdown("""
        <div style="padding: 20px; background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%); border-radius: 15px; margin-top: 10px;">
            <h4 style="color: #667eea;">📧 Email</h4>
            <p><a href="mailto:shivammalviyawork@gmail.com" style="color: #667eea; text-decoration: none; font-weight: 500;">shivammalviyawork@gmail.com</a></p>
            
            <h4 style="color: #667eea; margin-top: 20px;">📱 Phone</h4>
            <p style="font-weight: 500;">+91-XXXXXXXXXX</p>
            
            <h4 style="color: #667eea; margin-top: 20px;">💼 LinkedIn</h4>
            <p><a href="https://www.linkedin.com/in/shivam-malviya-6981b8192/" target="_blank" style="color: #667eea; text-decoration: none; font-weight: 500;">Connect on LinkedIn</a></p>
            
            <h4 style="color: #667eea; margin-top: 20px;">💻 GitHub</h4>
            <p><a href="https://github.com/Shivam08-byte" target="_blank" style="color: #667eea; text-decoration: none; font-weight: 500;">Check out my projects</a></p>
        </div>
        """, unsafe_allow_html=True)
        
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
        📱 <strong>+91-XXXXXXXXXX</strong><br>
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
    
    # Fun stats
    st.markdown("### 📊 Fun Stats")
    st.markdown("""
        <div style="text-align: center; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
            <div style="font-size: 2rem; font-weight: bold;">🔥</div>
            <div style="font-size: 1.2rem; font-weight: bold;">100+</div>
            <div>Days of Coding Streak</div>
        </div>
    """, unsafe_allow_html=True)

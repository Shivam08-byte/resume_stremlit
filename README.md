# 📄 Interactive Resume App - Streamlit

A beautiful, interactive resume application built with Streamlit and deployed on Streamlit Community Cloud.

## 🌟 Features

- **Interactive UI**: Modern, responsive design with tabs and animations
- **Multiple Sections**: About, Experience, Projects, Skills, and Education
- **Skill Visualization**: Progress bars showing proficiency levels
- **Mobile Responsive**: Works perfectly on all devices
- **Easy to Customize**: Simply edit `app.py` to update your information

## 🚀 Quick Start - Run Locally

1. **Clone the repository** (after you push it to GitHub)
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

4. **View in browser**
   - The app will automatically open in your default browser
   - Default URL: `http://localhost:8501`

## 🌐 Deploy to Streamlit Community Cloud (One-Click Deployment)

### Step 1: Push to GitHub

1. **Create a new repository on GitHub**
   - Go to https://github.com/new
   - Name it (e.g., `streamlit-resume`)
   - Don't initialize with README (we already have files)
   - Click "Create repository"

2. **Push your code**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy on Streamlit Community Cloud

1. **Go to Streamlit Community Cloud**
   - Visit: https://share.streamlit.io/

2. **Sign in with GitHub**
   - Click "Sign in with GitHub"
   - Authorize Streamlit to access your repositories

3. **Deploy your app** (This is the "one-click" part!)
   - Click "New app" button
   - Select your repository from the dropdown
   - Select branch: `main`
   - Main file path: `app.py`
   - Click "Deploy!"

4. **Wait for deployment** (usually takes 1-2 minutes)
   - Streamlit will install dependencies and start your app
   - You'll get a public URL like: `https://your-app-name.streamlit.app`

### Step 3: Share Your Resume!

Your resume is now live! Share the URL with:
- Potential employers
- Recruiters
- Your network
- On your LinkedIn profile

## 🔄 Updating Your Resume

Any time you want to update your resume:

1. **Edit `app.py`** locally
2. **Commit and push changes**
   ```bash
   git add app.py
   git commit -m "Update resume information"
   git push
   ```
3. **Automatic redeployment**: Streamlit will automatically detect the changes and redeploy (takes ~1 minute)

## ✏️ Customization Guide

### Update Personal Information

Edit the following sections in `app.py`:

```python
# Header section (lines 30-40)
st.markdown('<p class="main-header">Your Name</p>', unsafe_allow_html=True)

# Contact info (lines 42-48)
📧 your.email@example.com | 📱 +1-XXX-XXX-XXXX

# About section (lines 55-60)
# Update your bio and metrics
```

### Add/Remove Experience

Look for the Experience section (lines 70-120) and add/remove experience cards:

```python
st.markdown("""
<div class="experience-card">
    <h3>Your Job Title</h3>
    <p><strong>Company Name</strong> | Start Date - End Date</p>
    <ul>
        <li>Achievement 1</li>
        <li>Achievement 2</li>
    </ul>
</div>
""", unsafe_allow_html=True)
```

### Modify Skills

Update the skills section (lines 180-220):

```python
skills = ["Python", "JavaScript", "Your Skill", ...]
```

### Change Colors

Edit the CSS section (lines 10-60) to change colors:

```python
# Main color scheme
color: #1E88E5;  # Blue - change to your preferred color
```

## 📁 Project Structure

```
.
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore file
└── README.md          # This file
```

## 🛠️ Tech Stack

- **Framework**: Streamlit
- **Language**: Python 3.x
- **Deployment**: Streamlit Community Cloud
- **Version Control**: Git/GitHub

## 📝 Requirements

- Python 3.7+
- Streamlit 1.29.0+
- Git
- GitHub account (for deployment)

## 💡 Tips

- **Keep it updated**: Regularly update your resume as you gain experience
- **Use metrics**: Quantify achievements with numbers (e.g., "Improved performance by 40%")
- **Add links**: Include links to your projects, GitHub, LinkedIn
- **Mobile testing**: Always test on mobile devices
- **Analytics**: You can add Google Analytics to track visitors

## 🐛 Troubleshooting

### App won't start locally
```bash
# Make sure you're in the right directory
cd /path/to/your/project

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Run again
streamlit run app.py
```

### Deployment fails on Streamlit Cloud
- Check that `requirements.txt` is in the root directory
- Ensure `app.py` filename is correct (case-sensitive)
- Verify Python version compatibility
- Check Streamlit Cloud logs for specific errors

### Changes not reflecting after push
- Wait 1-2 minutes for automatic redeployment
- Or manually reboot app from Streamlit Cloud dashboard
- Clear browser cache

## 📞 Support

If you encounter issues:
1. Check Streamlit documentation: https://docs.streamlit.io/
2. Visit Streamlit forums: https://discuss.streamlit.io/
3. Check GitHub issues in this repository

## 📜 License

Feel free to use this template for your own resume!

## 🙏 Acknowledgments

Built with ❤️ using Streamlit

---

**Ready to impress?** Deploy your resume now and share it with the world! 🚀

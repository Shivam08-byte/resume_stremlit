# 📧 Email Notification Setup Guide

This guide will help you set up email notifications for your contact form.

## 🚀 Quick Setup (Using Gmail)

### Step 1: Generate Gmail App Password

1. **Go to your Google Account:** https://myaccount.google.com/
2. **Enable 2-Factor Authentication** (if not already enabled):
   - Go to Security → 2-Step Verification
   - Follow the setup process

3. **Create an App Password:**
   - Go to Security → 2-Step Verification → App passwords
   - Or directly: https://myaccount.google.com/apppasswords
   - Select app: "Mail"
   - Select device: "Other" → Type "Streamlit Resume App"
   - Click "Generate"
   - **Copy the 16-character password** (you'll use this as SENDER_PASSWORD)

### Step 2: Configure Secrets Locally

1. **Create the secrets file:**
   ```bash
   mkdir -p .streamlit
   cp .streamlit/secrets.toml.example .streamlit/secrets.toml
   ```

2. **Edit `.streamlit/secrets.toml`:**
   ```toml
   SMTP_SERVER = "smtp.gmail.com"
   SMTP_PORT = 587
   SENDER_EMAIL = "your-gmail@gmail.com"
   SENDER_PASSWORD = "your-16-char-app-password"
   RECEIVER_EMAIL = "shivammalviyawork@gmail.com"
   ```

3. **Replace the values:**
   - `SENDER_EMAIL`: Your Gmail address
   - `SENDER_PASSWORD`: The 16-character app password from Step 1
   - `RECEIVER_EMAIL`: Where you want to receive notifications (can be the same)

### Step 3: Configure on Streamlit Cloud

1. **Go to your Streamlit Cloud dashboard:**
   https://share.streamlit.io/

2. **Select your app:** `resume_stremlit`

3. **Click the ⚙️ Settings button**

4. **Go to "Secrets" section**

5. **Paste your secrets:**
   ```toml
   SMTP_SERVER = "smtp.gmail.com"
   SMTP_PORT = 587
   SENDER_EMAIL = "your-gmail@gmail.com"
   SENDER_PASSWORD = "your-16-char-app-password"
   RECEIVER_EMAIL = "shivammalviyawork@gmail.com"
   ```

6. **Click "Save"**

7. **Reboot your app** (if needed)

## 🧪 Testing

1. **Test locally first:**
   - Fill out the contact form
   - Check if you receive an email

2. **Test on production:**
   - Deploy to Streamlit Cloud
   - Fill out the form on your live site
   - Check your email

## ⚠️ Important Notes

- **Never commit secrets to Git!** The `.streamlit/secrets.toml` file is gitignored
- **Use App Passwords, not your regular password** for security
- **Gmail has sending limits:** 
  - Free Gmail: 500 emails/day
  - Google Workspace: 2000 emails/day

## 🔄 Alternative Email Services

### Using Outlook/Hotmail:
```toml
SMTP_SERVER = "smtp-mail.outlook.com"
SMTP_PORT = 587
```

### Using Yahoo:
```toml
SMTP_SERVER = "smtp.mail.yahoo.com"
SMTP_PORT = 587
```

### Using SendGrid (Recommended for production):
```toml
SMTP_SERVER = "smtp.sendgrid.net"
SMTP_PORT = 587
SENDER_EMAIL = "apikey"
SENDER_PASSWORD = "your-sendgrid-api-key"
```

## 🐛 Troubleshooting

### "Authentication failed" error:
- Make sure 2FA is enabled
- Use App Password, not regular password
- Check if "Less secure app access" is disabled (shouldn't need it with app passwords)

### "Connection refused" error:
- Check SMTP_SERVER and SMTP_PORT
- Ensure your network allows outbound connections on port 587

### Not receiving emails:
- Check spam/junk folder
- Verify RECEIVER_EMAIL is correct
- Check Gmail sent items to confirm email was sent

## 📞 Support

If you run into issues, check:
- Gmail App Password docs: https://support.google.com/accounts/answer/185833
- Streamlit Secrets docs: https://docs.streamlit.io/library/advanced-features/secrets-management

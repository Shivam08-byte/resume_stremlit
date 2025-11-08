# 📮 Formspree Integration Setup

The easiest way to handle contact form submissions in production!

## 🌟 Why Formspree?

- ✅ **No backend needed** - just add endpoint
- ✅ **5 seconds setup** - literally the fastest option
- ✅ **Email notifications** - get notified instantly
- ✅ **Spam protection** - built-in reCAPTCHA
- ✅ **100% reliable** - trusted by 100,000+ websites
- ✅ **Free tier** - 50 submissions/month

## 🚀 Quick Setup (2 minutes)

### Step 1: Create Formspree Account

1. Go to: https://formspree.io/
2. Click **"Sign Up"**
3. Sign up with:
   - Email, or
   - GitHub, or
   - Google

### Step 2: Create a Form

1. After signing in, click **"+ New Form"**

2. Fill in form details:
   - **Form name:** "Resume Contact Form"
   - **Your email:** shivammalviyawork@gmail.com (where you'll get notifications)

3. Click **"Create Form"**

4. **Copy the form endpoint URL**
   - It looks like: `https://formspree.io/f/xyzabc123`
   - Or just the form ID: `xyzabc123`

### Step 3: Add to Your App

#### Local (.streamlit/secrets.toml):
```toml
FORMSPREE_ENDPOINT = "https://formspree.io/f/xyzabc123"
```

#### Streamlit Cloud:
1. Go to your app settings → Secrets
2. Add:
```toml
FORMSPREE_ENDPOINT = "https://formspree.io/f/xyzabc123"
```

### Step 4: Test!

That's it! Fill out your contact form and you'll receive:
- ✅ Email notification with submission details
- ✅ All submissions visible in Formspree dashboard

## 📊 Formspree Dashboard Features

Log in to https://formspree.io/ to:

- **View all submissions** in one place
- **Export to CSV** for backup
- **Set up integrations** (Slack, webhooks, etc.)
- **Configure spam filters**
- **Customize email notifications**
- **Add team members**

## 💰 Pricing Tiers

### Free Plan (Perfect for personal resume!)
- ✅ 50 submissions/month
- ✅ Email notifications
- ✅ Spam filtering
- ✅ Unlimited forms
- ✅ CSV exports

### Paid Plans (If you need more)
- **Gold ($10/month):** 1,000 submissions
- **Platinum ($40/month):** 10,000 submissions
- **Custom uploads:** File attachments support

## ⚙️ Advanced Configuration

### Custom Email Template

In Formspree dashboard:
1. Go to your form settings
2. Click **"Notifications"**
3. Customize subject line and email template

### Spam Protection

1. Go to form settings → **"Spam Protection"**
2. Enable reCAPTCHA
3. Add to your Streamlit secrets:
```toml
FORMSPREE_RECAPTCHA_KEY = "your_site_key"
```

### Webhooks

Send submissions to other services:
1. Form settings → **"Webhooks"**
2. Add webhook URL
3. Submissions automatically forwarded

### Integrations

Connect to:
- Slack (get notifications in channel)
- Google Sheets (auto-save to sheets)
- Zapier (connect to 5,000+ apps)
- Airtable, Notion, etc.

## 🔍 Viewing Submissions

### In Formspree Dashboard:
1. Go to https://formspree.io/
2. Click on your form
3. See all submissions with:
   - Timestamp
   - All form fields
   - IP address
   - User agent
   - Spam score

### Export Options:
- **CSV:** Export all submissions
- **JSON:** API access for integrations
- **Email:** Get each submission via email

## 🎯 Best Practices

1. **Set up email forwarding** to your main inbox
2. **Add form to favorites** for quick access
3. **Enable spam protection** immediately
4. **Export submissions monthly** as backup
5. **Monitor usage** to stay within limits

## 🐛 Troubleshooting

### "Invalid form ID" error:
- Double-check the endpoint URL in secrets
- Make sure you copied the full URL: `https://formspree.io/f/YOUR_ID`

### Not receiving emails:
- Check Formspree spam folder
- Verify email address in form settings
- Check email notification settings

### Submissions not appearing:
- Check form is active (not paused)
- Verify endpoint URL is correct
- Check Formspree dashboard for errors

### Rate limit reached:
- Free plan: 50/month limit
- Upgrade to Gold plan for 1,000/month
- Or use CSV fallback (always works!)

## 🔄 Migration from Other Services

### From EmailJS:
1. Export submissions
2. Import to Formspree via CSV
3. Update endpoint in secrets

### From FormSubmit:
1. Create Formspree form
2. Update endpoint
3. No migration needed!

## 💡 Pro Tips

- **Multiple forms:** Create separate forms for different purposes
- **Archive submissions:** Download monthly CSVs
- **Team collaboration:** Add team members in settings
- **API access:** Use Formspree API for custom integrations
- **Analytics:** Track submission rates in dashboard

## 🎨 Form Customization

Formspree supports:
- ✅ Custom confirmation messages
- ✅ Redirect after submission
- ✅ Custom email templates
- ✅ Field validation
- ✅ Honeypot spam protection

## 📞 Support

- Documentation: https://help.formspree.io/
- Status page: https://status.formspree.io/
- Email support: help@formspree.io
- Community: https://github.com/formspree/formspree

## 🆚 Comparison with Other Methods

| Feature | Formspree | Email SMTP | Google Sheets | CSV |
|---------|-----------|------------|---------------|-----|
| Setup Time | 2 min | 15 min | 20 min | 0 min |
| Cost | Free* | Free | Free | Free |
| Reliability | 99.9% | 95% | 99% | 100% |
| Spam Protection | Yes | No | No | No |
| Dashboard | Yes | No | Yes | No |
| Notifications | Yes | Yes | Manual | No |
| Best For | Production | Self-hosted | Analytics | Backup |

*50 submissions/month on free plan

## ✅ Recommended Setup

Use **all 4 methods** for maximum reliability:
1. ✅ **CSV** - Always works (local backup)
2. ✅ **Email** - Instant notifications
3. ✅ **Formspree** - Easy management & spam protection
4. ✅ **Google Sheets** - Analytics and reporting

Your app will try all methods and use whichever works!

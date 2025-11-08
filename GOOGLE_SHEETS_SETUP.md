# 📊 Google Sheets Integration Setup

Save contact form submissions to Google Sheets automatically!

## 🚀 Quick Setup

### Step 1: Create Google Sheet

1. Go to: https://sheets.google.com/
2. Create a new spreadsheet
3. Name it: "Resume Contact Form Submissions"
4. Set up columns in Row 1:
   - A1: `Timestamp`
   - B1: `Name`
   - C1: `Email`
   - D1: `Subject`
   - E1: `Message`

### Step 2: Create Google Apps Script

1. In your Google Sheet, click **Extensions** → **Apps Script**

2. Delete any existing code and paste this:

```javascript
function doPost(e) {
  try {
    // Get the active spreadsheet
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    
    // Parse the incoming data
    var data = JSON.parse(e.postData.contents);
    
    // Append row with data
    sheet.appendRow([
      data.timestamp,
      data.name,
      data.email,
      data.subject,
      data.message
    ]);
    
    // Return success
    return ContentService.createTextOutput(JSON.stringify({
      'status': 'success',
      'message': 'Data saved successfully'
    })).setMimeType(ContentService.MimeType.JSON);
    
  } catch (error) {
    // Return error
    return ContentService.createTextOutput(JSON.stringify({
      'status': 'error',
      'message': error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}
```

3. **Save** the script (Ctrl/Cmd + S)
4. Name it: "Resume Form Handler"

### Step 3: Deploy as Web App

1. Click **Deploy** → **New deployment**

2. Click the gear icon ⚙️ next to "Select type"

3. Select **Web app**

4. Configure deployment:
   - **Description:** "Resume Contact Form"
   - **Execute as:** "Me (your email)"
   - **Who has access:** "Anyone"

5. Click **Deploy**

6. **Authorize** the script:
   - Click "Authorize access"
   - Select your Google account
   - Click "Advanced" → "Go to Resume Form Handler (unsafe)"
   - Click "Allow"

7. **Copy the Web App URL** (looks like: `https://script.google.com/macros/s/ABC...XYZ/exec`)

### Step 4: Add to Secrets

#### Local (.streamlit/secrets.toml):
```toml
GOOGLE_SHEETS_URL = "https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec"
```

#### Streamlit Cloud:
1. Go to your app settings
2. Add to Secrets:
```toml
GOOGLE_SHEETS_URL = "https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec"
```

### Step 5: Test!

Fill out your contact form and check if data appears in Google Sheets!

## 🎨 Optional: Format Your Sheet

Make it pretty! 

1. **Freeze header row:**
   - Click row 1 → View → Freeze → 1 row

2. **Format header:**
   - Select row 1
   - Background: Blue/Purple gradient
   - Text: White, Bold

3. **Add conditional formatting:**
   - Select column A (timestamps)
   - Format → Conditional formatting
   - Highlight recent submissions in green

4. **Add filters:**
   - Click row 1 → Data → Create a filter

## 📊 View Your Data

Your Google Sheet now has:
- ✅ Real-time updates when forms are submitted
- ✅ Automatic timestamps
- ✅ All contact details organized
- ✅ Easy to sort, filter, and analyze
- ✅ Can create charts and reports

## 🔧 Troubleshooting

### "Script not authorized" error:
- Make sure you authorized the script in Step 3
- Try redeploying the web app

### Data not appearing:
- Check Apps Script execution logs: Extensions → Apps Script → Executions
- Verify the URL is correct in secrets
- Test the URL directly with curl:
```bash
curl -X POST "YOUR_WEB_APP_URL" \
  -H "Content-Type: application/json" \
  -d '{"timestamp":"2025-11-09","name":"Test","email":"test@example.com","subject":"Test","message":"Testing"}'
```

### Permission errors:
- Make sure "Execute as: Me" in deployment settings
- Make sure "Who has access: Anyone" in deployment settings

## 🔄 Updating the Script

If you need to modify the script:
1. Make changes in Apps Script editor
2. Click **Deploy** → **Manage deployments**
3. Click the edit icon ✏️
4. Click **Deploy** (creates new version)
5. The URL stays the same!

## 💡 Pro Tips

- **Notifications:** Use Google Sheets rules to get email notifications
- **Backups:** File → Make a copy regularly
- **Sharing:** Share with team members for collaborative management
- **Integration:** Connect to other tools via Zapier or Make.com

## 📞 Support

- Google Apps Script docs: https://developers.google.com/apps-script/
- Video tutorial: Search "Google Sheets Apps Script Web App" on YouTube

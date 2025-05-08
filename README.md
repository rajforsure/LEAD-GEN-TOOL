# Automated Lead Generation & Smart Outreach Tool

This project uses Python, Selenium, and Twilio to:
- Scrape leads from websites
- Score leads based on keyword matching
- Send automated outreach messages (via Twilio SMS or simulated sending)

## ⚠️ Important Note

✅ This project uses **dummy Twilio credentials** in `config.py` for demonstration purposes.  
✅ No real Twilio account or phone numbers are included in this repository.  

👉 If you want to send real SMS messages:
1. Create a free account at [Twilio](https://www.twilio.com/try-twilio).
2. Add your `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE` to your own `config.py` file.
3. Do **NOT** upload real credentials to GitHub.

---

## Setup Instructions

1. Clone this repository
2. Create a virtual environment
3. Install dependencies:

```bash
pip install -r requirements.txt

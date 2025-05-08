# Automated Lead Generation & Smart Outreach Tool

This project uses Python, Selenium, and Twilio to:
- Extract leads from web pages
- Score leads based on defined criteria
- Automate follow-up messages via SMS/email

## Setup
1. Clone the repository.
2. Create and activate a virtual environment.
3. Run `pip install -r requirements.txt`.
4. Update `config.py` with your credentials.
5. Run the desired module:
   - `python scraper.py`
   - `python twilio_followup.py`
   - `python lead_score.py`

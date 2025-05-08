from scraper import extract_leads
from lead_score import score_lead
from twilio_followup import send_sms

sample_phone = "+911234567890"

leads = extract_leads()

print("Extracted Leads:", leads)  # <== Add this

for lead in leads:
    score = score_lead(lead)
    print(f"Lead: {lead} | Score: {score}")

    if score >= 30:
        send_sms(sample_phone, f"Hi! Based on your role ({lead}), we’d love to connect!")


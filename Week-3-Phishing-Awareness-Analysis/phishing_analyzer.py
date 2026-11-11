
import re
from urllib.parse import urlparse

print("====================================")
print("       PHISHING MESSAGE ANALYZER")
print("====================================")

message = input("\nPaste the email or message: ")

# Suspicious keywords
keywords = [
    "urgent",
    "verify your account",
    "account suspended",
    "click here",
    "password",
    "otp",
    "bank details",
    "limited time",
    "claim your prize",
    "immediately"
]

# Suspicious URL patterns
shortened_domains = [
    "bit.ly", "tinyurl.com", "t.co",
    "is.gd", "cutt.ly"
]

red_flags = []

# Check suspicious keywords
for word in keywords:
    if word in message.lower():
        red_flags.append("Suspicious keyword found: " + word)

# Extract links
urls = re.findall(r'https?://[^\s]+|www\.[^\s]+', message)

for url in urls:
    if url.startswith("www."):
        url = "http://" + url

    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    if parsed.scheme == "http":
        red_flags.append("Link uses HTTP instead of HTTPS: " + url)

    if domain in shortened_domains:
        red_flags.append("Shortened URL detected: " + url)

if not urls:
    print("\nNo links detected.")

# Display results
print("\n========== ANALYSIS RESULTS ==========")

if red_flags:
    print("Warning: Suspicious signs detected!")
    for flag in red_flags:
        print("-", flag)

    print("\nReason: These signs may indicate a phishing attempt.")
    print("Avoid clicking suspicious links or sharing personal details.")

else:
    print("No obvious phishing indicators detected.")
    print("Still verify the sender before trusting the message.")

print("\n======================================")

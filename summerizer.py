from groq import Groq
from main import page_text
import re

GROQ_API_KEY = "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"
prompt = "There are terms and conditions of a website, are there any terms and conditions which violate users privacy ? If there are then summerize it don't give intro to the output directly come to the point and give each point a numbering at last give your rating that it's harmful or not and if many pepole will agree with the terms and conditions"

def clean_text(text):
    text = text.strip()
    text = re.sub(r'\n\s*\n', '\n', text)
    text = '\n'.join(line.strip() for line in text.splitlines())
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('. ', '.\n')
    text = re.sub(r'\*', '', text)
    return text

tuned_text = prompt + page_text
client = Groq(api_key=GROQ_API_KEY)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": tuned_text,
        }
    ],
    model="llama3-70b-8192",
)
output = chat_completion.choices[0].message.content

cleaned_text = clean_text(output)
print(cleaned_text)
GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": query_to_gen,
        }
    ],
    model="llama3-70b-8192",
)
print(chat_completion.choices[0].message.content)
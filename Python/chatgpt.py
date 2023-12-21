from openai import OpenAI
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "user", "content": "Write a short poem about a rainbow that would appeal to physicists."}
    ]
)

print(completion.choices[0].message)

import openai

openai.api_key = 'your-openai-api-key'

def ask_gpt3(question):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=f"{question}\n\nAnswer:",
      temperature=0.5,
      max_tokens=100
    )
    return response.choices[0].text.strip()

# Test the function
print(ask_gpt3("What is the capital of France?"))


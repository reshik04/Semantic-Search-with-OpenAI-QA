

```
# OpenAI GPT-3 Query Function

This repository contains a Python script that uses the OpenAI API to interact with the GPT-3 model. The script defines a function `ask_gpt3(question)` that takes a question as input and returns the model's response.

## Setup

1. **Install OpenAI Python client**: This script requires the OpenAI Python client. You can install it using pip:

```bash
pip install openai
```

2. **API Key**: You need to replace `'your-openai-api-key'` with your actual OpenAI API key. This key can be obtained from the OpenAI website after you sign up.

## Code Explanation

The `ask_gpt3(question)` function works as follows:

- `openai.Completion.create`: This is the method used to interact with the GPT-3 model. It sends a prompt to the model and gets a completion.

- `engine="text-davinci-003"`: This specifies the version of the GPT-3 model to use.

- `prompt=f"{question}\n\nAnswer:"`: This is the prompt that is sent to the GPT-3 model. It consists of the question followed by "Answer:", indicating to the model that it should generate an answer.

- `temperature=0.5`: This parameter controls the randomness of the model's output. A lower value makes the output more deterministic, while a higher value makes it more random.

- `max_tokens=100`: This parameter limits the length of the output to 100 tokens.

The function then returns the generated text, stripped of leading and trailing whitespace.

## Testing the Function

The script includes a test call to the `ask_gpt3(question)` function with the question "What is the capital of France?". You can replace this with any question of your choice.

## Usage

You can import this function in your own Python scripts to easily get answers from the GPT-3 model, or you can run this script directly to see the test question in action.
```

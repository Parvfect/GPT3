

import os
import openai

openai.api_key = "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"

def codex_request_loop():
    
    prompt = ""
    max_tokens = 64

    while True:
        new_prompt = input("Do you want to add anything to add to the prompt?") + "\n"
        prompt = prompt + new_prompt
        
        response = push_to_codex(prompt, max_tokens)
        prompt = prompt + response.choices[0].text + "\n"
        
        print(prompt)

        max_tokens = len(prompt) + 64

def push_to_codex(prompt, max_tokens):
    return openai.Completion.create(
    engine="davinci-codex",
    prompt=prompt,
    temperature=0,
    max_tokens=max_tokens,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop = ["#", "'''"],
    )

if __name__ == "__main__":
    codex_request_loop()
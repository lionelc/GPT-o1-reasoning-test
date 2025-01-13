import os, sys
import json
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')

def read_json_input(input_file):
    with open(input_file) as f:
        content = json.load(f)
    return content

def main():
    content = read_json_input(sys.argv[1])
    max_iter = 10

    if len(sys.argv) > 2:
        max_iter = int(sys.argv[2])

    for i in range(max_iter):
        print("\n\n-------------Iteration ", i+1, "----------------")
        messages = [
                    {"role": "user", "content": "You are a smart detective who is very good at reasoning."},
                    {
                        "role": "user",
                        "content": content["puzzle"]
                    }
                ]
    
        completion = openai.ChatCompletion.create(
            model = content["model"],
            messages = messages
        )

        response = completion.choices[0].message["content"]
        print(response)

        print("---------------------------------")
        print("Expected Answer: \n", "\n".join(content["answers"]))

if __name__ == "__main__":
    main()


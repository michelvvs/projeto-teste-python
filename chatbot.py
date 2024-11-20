# import openai


# def send_message(message):
#     res = openai.chat.completions.create(
#         model = "gpt-4o-mini",
#         messages = [
#                     {"role": "user", "content": message}
#                     ],
#     )

#     return res["choices"][0]

# print(send_message("quem descobriu o Brasil?"))


from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

openai_api_key = os.getenv("OPENAI_KEY")

client = OpenAI(api_key = openai_api_key)
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "quantos anos tinha einstein quando morreu?"}],
    seed=1,
    temperature=0.0,
    max_tokens=1000
)
response = response.choices[0].message.content

print(response)
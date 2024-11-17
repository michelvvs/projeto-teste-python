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

client = OpenAI()
stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
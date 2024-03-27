from openai import OpenAI

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "give me the Mermaid flowchart for solving quadratic equation"},
    {"role": "user", "content": "What is the best software to drow it?"}
  ]
)
# I dont know if the messages response is right 
print(response.choices[0].message.content)

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    temperature=0.1, #0으로 갈 수록 안정적으로 답변 창의적답을 원할때 1에 가까이
    messages=[
        {"role": "system", "content": "you are helpful assistant."},
        {"role": "user", "content":"2022년 월드컵 우승 팀은 어디야?"},
    ]
)

print(response)

print("----")
print(response.choices[0].message.content)

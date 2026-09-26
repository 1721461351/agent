import os

import dotenv
from openai import OpenAI
from pydantic import BaseModel, EmailStr, Field
from pydantic import Field

dotenv.load_dotenv()


class UserInfo(BaseModel):
    """"传递用户信息进行数据提取，覆盖name、age、email"""
    name: str = Field(..., description="用户名字")
    email: EmailStr = Field(..., description="邮箱")
    age: int = Field(..., gt=0, description="年龄需要正整数")


client = OpenAI()

print( UserInfo.model_json_schema())

res = client.chat.completions.create(
    model=os.getenv("CHAT_MODEL"),
    messages=[
        {
            "role": "user",
            "content": "我叫小黑，今年20岁，联系方式是xxx@163.com"
        }
    ],
    tools=[
        {
            "type": "function",
            "function": {
                "name": UserInfo.__name__,
                "description": UserInfo.__doc__,
                "parameters": UserInfo.model_json_schema()
            }
        }
    ],

    tool_choice={"type": "function", "function": {
        "name": UserInfo.__name__,
    }}
)

print(res)

user = UserInfo.model_validate_json(res.choices[0].message.tool_calls[0].function.arguments)

print(user)
print()
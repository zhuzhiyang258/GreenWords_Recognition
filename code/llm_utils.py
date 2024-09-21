import os
from dotenv import load_dotenv
from openai import OpenAI

class DouBaoClient:
    """
    OpenAI client for DouBao
    """
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("ARK_API_KEY")
        self.base_url = os.getenv("ARK_BASE_URL")
        self.endpoint = os.getenv("END_POINT_ID")
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

    def get_standard_response(self, system_content, user_content):
        print("----- standard request -----")
        completion = self.client.chat.completions.create(
            model=self.endpoint,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
        )
        print(completion.choices[0].message.content)
        return completion.choices[0].message.content

    def get_streaming_response(self, system_content, user_content):
        print("----- streaming request -----")
        stream = self.client.chat.completions.create(
            model=self.endpoint,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
            stream=True
        )

        response = ""
        for chunk in stream:
            if not chunk.choices:
                continue
            print(chunk.choices[0].delta.content, end="")
            response += chunk.choices[0].delta.content
        print()
        return response
    

class OpenAIClient:
    """
    OpenAI client
    """
    def __init__(self):
        self.api_key = "123456"
        self.base_url = "http://localhost:8000/v1"
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)
        self.models = self.client.models.list()
        self.model = self.models.data[0].id

    def get_standard_response(self, system_content, user_content):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
        )
        return completion.choices[0].message.content


# # Usage
# if __name__ == "__main__":
#     system_content = "你是豆包，是由字节跳动开发的 AI 人工智能助手"
#     user_content = "常见的十字花科植物有哪些？"

#     client = DouBaoClient()
#     standard_response = client.get_standard_response(system_content, user_content)
#     streaming_response = client.get_streaming_response(system_content, user_content)

if __name__ == "__main__":
    client = OpenAIClient()
    system_content = "你是 AI 人工智能助手"
    user_content = "介绍一下四川的美食"
    standard_response = client.get_standard_response(system_content, user_content)
    # streaming_response = client.get_streaming_response(system_content, user_content)
    print(standard_response)

# # Usage
# if __name__ == "__main__":
#     system_content = "你是豆包，是由字节跳动开发的 AI 人工智能助手"
#     user_content = "常见的十字花科植物有哪些？"

#     client = DouBaoClient()
#     standard_response = client.get_standard_response(system_content, user_content)
#     streaming_response = client.get_streaming_response(system_content, user_content)
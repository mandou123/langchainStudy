from langchain_openai import ChatOpenAI
# ChatOpenAI는 OpenAI사의 채팅 전용 LLM

# 객체 생성
llm = ChatOpenAI(
    temperature=0.1, #샘플링 온도(=창의성: 0~2)
    max_tokens= 2048, #최대 토큰수
    model_name="gpt-3.5-turbo",
)

question = "대한민국의 수도는 어디인가요?"

#답변
print(f"[Reply]: {llm.invoke(question)}")
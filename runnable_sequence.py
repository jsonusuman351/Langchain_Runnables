from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt=PromptTemplate(
    template="write a joke about {topic}",
    input_variables=["topic"],  )

model=ChatOpenAI()

parser=StrOutputParser()

prompt2=PromptTemplate(
    template="Make this more funny: {joke}",
    input_variables=["joke"],  )

joke_chain=RunnableSequence(prompt,model,parser,prompt2,model,parser)

response=joke_chain.invoke({"topic":"chickens"})
print(response)


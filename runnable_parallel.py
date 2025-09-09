from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel, RunnableSequence

load_dotenv()

prompt1=PromptTemplate(
    template="generate linkedin post about {topic}",      
    input_variables=["topic"],  )

prompt2=PromptTemplate(
    template="generate tweet about: {topic}",      
    input_variables=["topic"],  )

llm=ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.7)
parser=StrOutputParser()

prallel_chain=RunnableParallel({
    'linkedin': RunnableSequence(prompt1,llm,parser),
    'tweet': RunnableSequence(prompt2,llm,parser)}
)

response=prallel_chain.invoke({"topic":"AI"})
print(response)



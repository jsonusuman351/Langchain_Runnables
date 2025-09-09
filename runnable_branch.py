from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableBranch

load_dotenv()

prompt1=PromptTemplate(
    template="write a report about {topic}",  
    input_variables=["topic"],  )

prompt2=PromptTemplate(
    template="summarize the  {text}",
    input_variables=["text"],  )

model=ChatOpenAI()
parser=StrOutputParser()

gen_report_chain=RunnableSequence(prompt1,model,parser)

branch=RunnableBranch(
    (lambda x:len(x.split())>200, RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(gen_report_chain,branch)
response=final_chain.invoke({"topic":"AI"})
print(response)

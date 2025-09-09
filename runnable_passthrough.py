from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()

prompt1=PromptTemplate(
    template="write a joke about {topic}",  
    input_variables=["topic"],  )

promp2t2=PromptTemplate(
    template="Explain this joke: {joke}",   
    input_variables=["joke"],  )

model=ChatOpenAI()
parser=StrOutputParser()

chain=RunnableSequence(prompt1,model,parser)



prallel=RunnableParallel({
    'original':RunnablePassthrough(),
    'explanation':RunnableSequence(promp2t2,model,parser)
}
)
final_chain=RunnableSequence(chain,prallel)

response=final_chain.invoke({"topic":"chickens"})
print(response)



from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda

load_dotenv()

prompt1=PromptTemplate(
    template="write a joke about {topic}",  
    input_variables=["topic"],  )

def word_count(text):
    return len(text.split())



model=ChatOpenAI()
parser=StrOutputParser()

chain=RunnableSequence(prompt1,model,parser)



prallel=RunnableParallel({
    'original':RunnablePassthrough(),
    'word_count':RunnableLambda(lambda text: len(text.split()))
    #or, 'word_count':RunnableLambda(word_count)
}
)
final_chain=RunnableSequence(chain,prallel)

response=final_chain.invoke({"topic":"chickens"})
print(response)



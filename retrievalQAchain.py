from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAI
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
import os


#load the documents
loader=TextLoader("docs.txt")
documents=loader.load()

#split the documents into chunks
text_splitter=CharacterTextSplitter(chunk_size=500,chunk_overlap=50)
docs=text_splitter.split_documents(documents)


# Get OpenAI API key from environment variable
# Get OpenAI API key from environment variable
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
# Convert the text into embeddings and store them in a vector database
vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings(openai_api_key=openai_api_key))

#create a retriver (fetches relevant documents based on a query)
retriever=vectorstore.as_retriever()

#initialize the LLM model
llm = OpenAI()

#create a RetrievalQA chain
qa_chain=RetrievalQA.from_chain_type(llm=llm,retriever=retriever)


# Ask a question and get an answer using invoke (run is deprecated)
query = "what are the key takeaways from the document?"
response = qa_chain.invoke(query)

# Print the response
print(response)



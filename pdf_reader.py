from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader


#load the documents
loader=TextLoader("docs.txt")
documents=loader.load()

#split the documents into chunks
text_splitter=CharacterTextSplitter(chunk_size=500,chunk_overlap=50)
docs=text_splitter.split_documents(documents)

#convert the text into embeddings and store them in a vector database
vectorstore=FAISS.from_documents(docs,OpenAIEmbeddings())

#create a retriver (fetches relevant documents based on a query)
retriever=vectorstore.as_retriever()

#manually retrieve relevant doucuments
query="what are the key takeaways from the document?"
retrieved_docs=retriever.get_relevant_documents(query)

#combine the retrieved documents into a single prompt
retrieved_text="\n".join([doc.page_content for doc in retrieved_docs])

#initialize the LLM model
llm=OpenAI()

#manually pass retrieved text to the LLM
prompt=f"Based on the following text, answer the question: {query}\n\n{retrieved_text}"
response=llm.predict(prompt)

#print the response
print(response) 


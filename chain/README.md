Advanced RAG Q&A Chatbot With Chain And Retrievers Using Langchain

building advanced RAG Q&A chatbot with chain and retrievers using langchain
A retriever is an interface that returns documents given an unstructured query. 

It is more general than a vector store. A retriever does not need to be able to store documents, only to return (or retrieve) them. Vector stores can be used as the backbone of a retriever, but there are other types of retrievers as well.

Chains refer to sequences of calls - whether to an LLM, a tool, or a data preprocessing step. 
The primary supported way to do this is with LCEL.
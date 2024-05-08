#!/usr/bin/env python
# coding: utf-8

# In[5]:


import openai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Initialize OpenAI client
openai.api_key = 'your-openai-api-key'

# Define your corpus
corpus = [
    "The sky is blue and beautiful.",
    "Love this blue and beautiful sky!",
    "The quick brown fox jumps over the lazy dog.",
    "A king's breakfast has sausages, ham, bacon, eggs, toast and beans",
    "I love green eggs, ham, sausages and bacon!",
    "The brown fox is quick and the blue dog is lazy!",
    "The sky is very blue and the sky is very beautiful today",
    "The dog is lazy but the brown fox is quick!"
]

# Create embeddings for your corpus
corpus_embeddings = [openai.Embed.create(model="text-embedding-3-small", text=doc) for doc in corpus]

# Define a function for semantic search
def semantic_search(query):
    query_embedding = openai.Embed.create(model="text-embedding-3-small", text=query)
    similarities = [cosine_similarity([query_embedding], [doc_embedding]) for doc_embedding in corpus_embeddings]
    best_match = corpus[np.argmax(similarities)]
    return best_match

# Test the function
print(semantic_search("blue sky"))


# In[ ]:





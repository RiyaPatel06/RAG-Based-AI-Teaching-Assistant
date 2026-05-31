An AI-powered Teaching Assistant for Java/DSA courses that allows students to ask questions and automatically finds the most relevant video sections from course content using Retrieval-Augmented Generation (RAG)

# How to use this RAG AI Teaching Assistent on your own data

## Step 1 - Collect to mp3

Move all your video files to the videos folder

## Step 2 - Convert to mp3

Convert all your video files to mp3 by running video_to_mp3

## Convert mp3 to json

Convert all the mp3 files to json by running mp3_to_json

## Step 4 - Convert the json files to vectors

Use the file preprocess_json to convert the json files to a dataframe with embeddings and save it as a joblib pickle

## Step 5 - Prompt generation and feeding to LLM

Read the joblib file and load it in to the memory.Then create a relevent prompt as per the user query and feed it to the LLM

# Tech Stack

- Python
- Whisper
- Ollama
- Pandas
- Scikit-Learn
- Joblib
- JSON

# WorkFlow

1. Convert video lectures to audio.
2. Generate transcripts using Whisper.
3. Split transcripts into chunks.
4. Generate embeddings.
5. Store embeddings locally.
6. User asks a question.
7. Retrieve relevant chunks using semantic search.
8. LLM generates a contextual answer with video timestamps.

# Future Improvements

. Streamlit Web Interface
. Vector Database Integration
. Multi-course Support
. Real-time Chat Interface

# Architecture Diagram

Video Files
↓
Audio Extraction
↓
Whisper STT
↓
JSON Chunks
↓
Embeddings (BGE-M3)
↓
Vector Search
↓
Relevant Chunks
↓
LLM (Ollama)
↓
Answer + Timestamp

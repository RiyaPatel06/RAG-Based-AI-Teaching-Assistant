# How to use this RAG AI Teaching Assistent on your own data

## Step 1 - Collect to mp3

convert all your video files to the videos folder

## Step 2 - Convert to mp3

convert all the mp3 files to json by running mp3_to_json

## Step 4 - Convert the json files to vectors

Use the file preprocess_json to convert the json files to a dataframe with embeddings and save it as a joblib pickle

## Step 5 - Prompt generation and feeding to LLM

Read the joblib file and load it in to the memory.Then create a relevent prompt as per the user query and feed it to the LLM

'''from datasets import load_dataset
from huggingface_hub import login
import torch

from transformers import (
    AutoModelForSeq2SeqLM,
    pipeline)

hf_token = "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"
login(hf_token)

data_id= "samsum"
dataset = load_dataset(data_id, trust_remote_code=True)

#model_id = "google/flan-t5-base"
#model_id = "google/pegasus-xsum"
model_id = "gpt2-large"
#model_id = "facebook/bart-base"
#model_id = "google/flan-t5-small"
llm = pipeline("summarization", model=model_id,device=0)




# A basic prompt to the dialogue to run though the pipeline
input_diags = [[f'summarize: {i}'] for i in dataset['validation']['dialogue']]

# Also extract the ground truths into a list
ground_truths = [i for i in dataset['validation']['summary']]

# Run the input dialogues through the pipeline
outputs = llm(input_diags[0:20], max_length=60, clean_up_tokenization_spaces=True)
# Extract the predictions into a list.
outputs = [i[0]['summary_text'] for i in outputs]




import evaluate
rouge = evaluate.load('rouge')

foundation_model_results = rouge.compute(predictions= outputs,  #List of predictions
                                         references=ground_truths[0:20], #list of ground truths
                                         use_aggregator=True,
                                         use_stemmer=True,
                                         )

print("-----------------evaluation_results--------------------------------------")
print(foundation_model_results)





'''



from datasets import load_dataset
from huggingface_hub import login
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import evaluate 


import matplotlib.pyplot as plt
import numpy as np





import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 


def short_the_prompt(long_description):

    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('punkt_tab') 

    #long_sentence = "It's such a fine day today, The sun is out, and the sky is blue. Can you tell me what the weather will be like tomorrow?"

    word_tokens = word_tokenize(long_description)

    short_description = ' '.join([t for t in word_tokens if t not in stopwords.words('english')])

    print(short_description)
    return short_description


def Evaluate_model(model_id, examles_number = 20, batch_size = 4):

    # Select device (GPU if available)
    device = 0 if torch.cuda.is_available() else -1
    # ==========================
    # Load Dataset for Title Generation
    # ==========================
    data_id = "Skelebor/book_titles_and_descriptions_en"
    dataset = load_dataset(data_id, trust_remote_code=True)

    # Check available splits
    #print("Available splits:", dataset.keys())

    # Use the train split (take a small sample for evaluation)
    #print(sample_data)
    # ==========================
    # Load the Model Pipeline
    # ==========================
    torch_dtype = torch.float16 if torch.cuda.is_available() else None  # Use mixed precision only if GPU is available



    #model = AutoModelForSeq2SeqLM.from_pretrained(model_id, torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32)

    tokenizer = AutoTokenizer.from_pretrained(model_id)

    llm = pipeline("text2text-generation", model=model_id, tokenizer=tokenizer, device=device,    torch_dtype=torch_dtype  # Use None (default precision) for CPU
  # Enable mixed precision
)

    # ==========================
    # Prepare Inputs and Outputs
    # ==========================
    # Prompt to generate titles from book descriptions
    sample = 0
    predictions = []
    while sample < examles_number:
        sample_data = dataset["train"].select(range(sample,sample + 1))  # Take the first 20 examples
        #print(sample)
        input_prompts = [
            tokenizer.decode(
                tokenizer.encode(
                    (
                        "Below are examples of book descriptions and their corresponding titles:\n\n"
                        "Description: A guide to understanding how habits work and how to change them.\n"
                        "Title: The Power of Habit: Why We Do What We Do\n\n"
                        "Description: A practical approach to building small, consistent changes that lead to major achievements.\n"
                        "Title: Atomic Habits: Tiny Changes, Remarkable Results\n\n"
                        "Description: A guide to deep, focused work that leads to high productivity and success.\n"
                        "Title: Deep Work: Rules for Focused Success in a Distracted World\n\n"
                        "Now, generate a concise and descriptive title for the following book description:\n\n"
                        f"Title of Description: {(i['description'])}\n"
                        
                    ),
                    max_length=512,
                    truncation=True  # Truncate if the input exceeds the max length
                ),
                skip_special_tokens=True  # Remove special tokens if any
            )
            for i in sample_data
        ]

        outputs = llm(input_prompts, max_new_tokens=15, clean_up_tokenization_spaces=True)
        predictions.extend([
            output['generated_text'] if 'generated_text' in output else output['summary_text']
            for output in outputs
        ])
        sample += 1

    #print(len(predictions))
    # Extract ground truth titles
    sample_data = dataset["train"].select(range(examles_number))  # Take the first 20 examples

    ground_truths = [i['title'] for i in sample_data]
    #print(predictions)
    #print((len(ground_truths)))
    # ==========================
    # Generate Titles
    # ==========================
    # Run the inputs through the model pipeline

    # Extract generated titles
    '''predictions = []
    for i in range(0, len(input_prompts), batch_size):
        batch = input_prompts[i:i+batch_size]
        outputs = llm(batch, max_new_tokens=15, clean_up_tokenization_spaces=True)
        predictions.extend([output['generated_text'] if 'generated_text' in output else output['summary_text'] for output in outputs])'''
    #print(predictions)
    # ==========================
    # Evaluate with ROUGE
    # ==========================
    rouge = evaluate.load('rouge')
    #results = rouge.compute(predictions=predictions, references=ground_truths, use_aggregator=True, use_stemmer=True)

    results = rouge.compute(
        predictions=predictions,
        references=ground_truths,
        use_aggregator=True,
        use_stemmer=True
    )

    # ==========================
    # Print Evaluation Results
    # ==========================
    print("-----------------Evaluation Results--------------------------------------" + model_id + "-----------------------")
    print(results)
    return results

    # Display a few example outputs
    '''for i, (prompt, pred, ref) in enumerate(zip(input_prompts[:3], predictions[:3], ground_truths[:3])):
        print(f"\nExample {i+1}")
        print("Input Description:", prompt)
        print("Generated Title:", pred)
        print("Ground Truth Title:", ref)'''




##########################################          evaluation with chancks        ##############################



import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from datasets import load_dataset
import evaluate
import nltk
#from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from nltk.tokenize import sent_tokenize

# Download NLTK resources
nltk.download('punkt')

# Function to split text into chunks (using the chunking method provided earlier)
def chunk_by_token_count(text, tokenizer, max_token_limit=512):
    tokens = tokenizer.encode(text)
    chunks = []
    for i in range(0, len(tokens), max_token_limit):
        chunk = tokens[i:i + max_token_limit]
        chunk_text = tokenizer.decode(chunk, skip_special_tokens=True)
        chunks.append(chunk_text)
    return chunks

def chunk_by_sentences(text, tokenizer, max_token_limit=512):
    sentences = sent_tokenize(text)
    chunk = []
    chunks = []
    token_count = 0
    for sentence in sentences:
        sentence_tokens = tokenizer.encode(sentence)
        if token_count + len(sentence_tokens) <= max_token_limit:
            chunk.append(sentence)
            token_count += len(sentence_tokens)
        else:
            chunks.append(' '.join(chunk))
            chunk = [sentence]
            token_count = len(sentence_tokens)
    if chunk:
        chunks.append(' '.join(chunk))
    return chunks

def sliding_window_chunking(text, tokenizer, max_token_limit=512, window_overlap=50):
    sentences = sent_tokenize(text)
    chunk = []
    chunks = []
    token_count = 0
    for i, sentence in enumerate(sentences):
        sentence_tokens = tokenizer.encode(sentence)
        if token_count + len(sentence_tokens) <= max_token_limit:
            chunk.append(sentence)
            token_count += len(sentence_tokens)
        else:
            chunks.append(' '.join(chunk))
            chunk = sentences[i - window_overlap:i + 1]  # Create overlap by adding last few sentences
            token_count = sum(len(tokenizer.encode(sen)) for sen in chunk)
    if chunk:
        chunks.append(' '.join(chunk))
    return chunks

import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize

def chunk_by_semantics(text, model, tokenizer, max_token_limit=512):
    h=0
'''    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)  # Move the model to the correct device

    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    embeddings = []

    # Process each sentence
    for sentence in sentences:
        inputs = tokenizer(
            sentence,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=max_token_limit
        )
        # Move inputs to the same device as the model
        inputs = {key: value.to(device) for key, value in inputs.items()}

        # Generate sentence embedding
        with torch.no_grad():
            outputs = model(**inputs)
            sentence_embedding = outputs.last_hidden_state.mean(dim=1).cpu().numpy()
        embeddings.append(sentence_embedding)

    # Group sentences into chunks based on similarity
    chunks = []
    current_chunk = [sentences[0]]
    current_embedding = embeddings[0]

    for i in range(1, len(sentences)):
        similarity = cosine_similarity(current_embedding, embeddings[i])
        if similarity > 0.7:  # Threshold for grouping sentences into a chunk
            current_chunk.append(sentences[i])
            current_embedding = np.mean([current_embedding, embeddings[i]], axis=0)
        else:
            chunks.append(' '.join(current_chunk))
            current_chunk = [sentences[i]]
            current_embedding = embeddings[i]

    # Add the last chunk
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks'''



# Evaluate function
def Evaluate_model2(model_id, examples_number=20, batch_size=4, chunk_method="token", max_token_limit=512):

    # Select device (GPU if available)
    device = 0 if torch.cuda.is_available() else -1
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id, device_map="auto")
    llm = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

    # Load dataset for title generation
    data_id = "Skelebor/book_titles_and_descriptions_en"
    dataset = load_dataset(data_id, trust_remote_code=True)
    
    # Prepare inputs and outputs
    sample = 0
    predictions = []
    while sample < examples_number:
        sample_data = dataset["train"].select(range(sample, sample + 1))  # Take the first `examples_number` examples
        
        input_prompts = [
            tokenizer.decode(
                tokenizer.encode(
                    (
                        "Below are examples of book descriptions and their corresponding titles:\n\n"
                        "Description: A guide to understanding how habits work and how to change them.\n"
                        "Title: The Power of Habit: Why We Do What We Do\n\n"
                        "Description: A practical approach to building small, consistent changes that lead to major achievements.\n"
                        "Title: Atomic Habits: Tiny Changes, Remarkable Results\n\n"
                        "Description: A guide to deep, focused work that leads to high productivity and success.\n"
                        "Title: Deep Work: Rules for Focused Success in a Distracted World\n\n"
                        "Now, generate a concise and descriptive title for the following book description:\n\n"
                        f"Title of Description: {(i['description'])}\n"
                    ),
                    
                ),
                #max_length=512,
                #truncation=True  # Truncate if the input exceeds the max length
                #skip_special_tokens=True
            )
            for i in sample_data
        ]

        # Apply chunking based on the selected method
        #print(input_prompts)
        for prompt in input_prompts:
            chunks = chunk_by_token_count(prompt, tokenizer, max_token_limit) if chunk_method == "token" else \
                    chunk_by_sentences(prompt, tokenizer, max_token_limit) if chunk_method == "sentence" else \
                    sliding_window_chunking(prompt, tokenizer, max_token_limit) if chunk_method == "sliding_window" else \
                    chunk_by_semantics(prompt, model, tokenizer, max_token_limit)
            
            # Generate predictions for each chunk
            #print(len(chunks))
            #outputs = []
            s=""
            chunk_titles =[]
            for chunk in chunks:
                outputs = llm([chunk], max_new_tokens=15, clean_up_tokenization_spaces=True)
                s+= outputs[0]['generated_text'] 
                chunk_titles.append(s)
               # print(s)
            outputs[0]['generated_text']  = s
                #predictions.extend([output[0]['generated_text'] if 'generated_text' in output[0] else output[0]['summary_text']])
            #outputs.append(output)
            #print(output)
                #print(output)
        '''
        input_prompts = [
            tokenizer.decode(
                tokenizer.encode(
                    (
                       "Create a concise and descriptive title for the following topics:\n" + "\n".join(chunk_titles)

                    ),
                    
                ),
                #skip_special_tokens=True
            )
            for i in sample_data
        ]
        outputs = llm(input_prompts, max_new_tokens=15, clean_up_tokenization_spaces=True)
        '''
        #outputs = llm(input_prompts, max_new_tokens=15, clean_up_tokenization_spaces=True)
        predictions.extend([
            output['generated_text'] if 'generated_text' in output else output['summary_text']

            #output[0]['generated_text'] if 'generated_text' in output else ""
            for output in outputs
        ])
        sample += 1

    # Extract ground truth titles
    sample_data = dataset["train"].select(range(examples_number))

    ground_truths = [i['title'] for i in sample_data]
    #print(predictions)
    #print(ground_truths)
    # Evaluate using ROUGE
    rouge = evaluate.load('rouge')
    results = rouge.compute(predictions=predictions, references=ground_truths, use_aggregator=True, use_stemmer=True)

    # Print evaluation results
    print(f"-----------------Evaluation Results--------------------------------------{model_id}-----------------------")
    print(results)
    return results







############################ Evaluate prompts  #######################################################


def Evaluate_model_prompt(prompt, model_id = "google/flan-t5-large", examles_number = 20, batch_size = 4):

    # Select device (GPU if available)
    device = 0 if torch.cuda.is_available() else -1
    # ==========================
    # Load Dataset for Title Generation
    # ==========================
    data_id = "Skelebor/book_titles_and_descriptions_en"
    dataset = load_dataset(data_id, trust_remote_code=True)

    # Check available splits
    #print("Available splits:", dataset.keys())

    # Use the train split (take a small sample for evaluation)
    #print(sample_data)
    # ==========================
    # Load the Model Pipeline
    # ==========================
    torch_dtype = torch.float16 if torch.cuda.is_available() else None  # Use mixed precision only if GPU is available



    #model = AutoModelForSeq2SeqLM.from_pretrained(model_id, torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32)

    tokenizer = AutoTokenizer.from_pretrained(model_id)

    llm = pipeline("text2text-generation", model=model_id, tokenizer=tokenizer, device=device,    torch_dtype=torch_dtype  # Use None (default precision) for CPU
  # Enable mixed precision
    )

    
    sample = 0
    predictions = []
    while sample < examles_number:
        sample_data = dataset["train"].select(range(sample,sample + 1))  # Take the first 20 examples
        #print(sample)
        input_prompts = [
            tokenizer.decode(
                tokenizer.encode(
                    (
                        prompt.format(description=i['description'])  # Format the prompt with dynamic content
                        
                    ),
                    max_length=512,
                    truncation=True  # Truncate if the input exceeds the max length
                ),
                skip_special_tokens=True  # Remove special tokens if any
            )
            for i in sample_data
        ]

        outputs = llm(input_prompts, max_new_tokens=15, clean_up_tokenization_spaces=True)
        predictions.extend([
            output['generated_text'] if 'generated_text' in output else output['summary_text']
            for output in outputs
        ])
        sample += 1

    #print(len(predictions))
    # Extract ground truth titles
    sample_data = dataset["train"].select(range(examles_number))  # Take the first 20 examples

    ground_truths = [i['title'] for i in sample_data]
    #print(predictions)
    #print((len(ground_truths)))
    # ==========================
    # Generate Titles
    # ==========================
    # Run the inputs through the model pipeline

    # Extract generated titles
    # ==========================
    # Evaluate with ROUGE
    # ==========================
    rouge = evaluate.load('rouge')
    #results = rouge.compute(predictions=predictions, references=ground_truths, use_aggregator=True, use_stemmer=True)

    results = rouge.compute(
        predictions=predictions,
        references=ground_truths,
        use_aggregator=True,
        use_stemmer=True
    )

    # ==========================
    # Print Evaluation Results
    # ==========================
    print("-----------------Evaluation Results--------------------------------------" + model_id + "-----------------------")
    print(results)
    return results







############################# Creating the graph of the evaluation results       ####################






# ==========================
# Data Preparation
# ==========================
#Input: models_list: List of models we want to evaluate, examples_number (max value = 31 because of CUDA error: out of memory)
def get_data(models_list, examples_number = 20):
    results = {}
    for model in models_list:
        print(model)
        res = Evaluate_model(model,examples_number)
        results[model] = res
        torch.cuda.empty_cache()  # Clear GPU memory after each model
    return results

def get_data_for_prompt(prompts_list, examples_number = 20):
    results = {}
    model_id = "google/flan-t5-large"
    i = 1
    
    for prompt in prompts_list:
        #print(prompt)
        res = Evaluate_model_prompt(prompt,model_id,examples_number)
        pr = 'prompt' + str(i)
        results[pr] = res
        torch.cuda.empty_cache()
        i+=1
        # Clear GPU memory after each model
    return results


# ==========================
# Results Data Example
# ==========================
'''results = {
    "google/flan-t5-base": {
        "rouge1": 0.382, "rouge2": 0.249, "rougeL": 0.378, "rougeLsum": 0.375
    },
    "google/pegasus-xsum": {
        "rouge1": 0.261, "rouge2": 0.141, "rougeL": 0.253, "rougeLsum": 0.252
    },
    "facebook/bart-base": {
        "rouge1": 0.088, "rouge2": 0.0,   "rougeL": 0.073, "rougeLsum": 0.072
    },
    "google/flan-t5-small": {
        "rouge1": 0.185, "rouge2": 0.065, "rougeL": 0.163, "rougeLsum": 0.166
    }
}'''


def create_graph(results,examples_number):
    model_names = list(results.keys())
    metrics = ["rouge1", "rouge2", "rougeL", "rougeLsum"]

    data = {metric: [results[model][metric] for model in model_names] for metric in metrics}

    # ==========================
    # Plotting the Results
    # ==========================
    bar_width = 0.2
    index = np.arange(len(model_names))

    fig, ax = plt.subplots(figsize=(12, 6))

    for i, metric in enumerate(metrics):
        plt.bar(index + i * bar_width, data[metric], bar_width, label=metric)

    # ==========================
    # Formatting the Graph
    # ==========================
    ax.set_xlabel('Prompts')
    ax.set_ylabel('ROUGE Scores')
    ax.set_title('ROUGE Evaluation Results Across Prompt On ' + str(examples_number) + ' Samples (google/flan-t5-large)')
    ax.set_xticks(index + bar_width * 1.5)
    ax.set_xticklabels(model_names, rotation=15)
    ax.legend()

    plt.tight_layout()
    plt.show()





# ==========================
# Authentication and Setup
# ==========================
hf_token = "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"  
login(hf_token)



model_id1 = "google/flan-t5-base"
model_id5 = "google/flan-t5-small"
#model_id2 = "google/pegasus-xsum"
model_id3 = "google/flan-t5-large"
model_id4 = "facebook/bart-base"

models = []


models.append(model_id3)
models.append(model_id1)
#models.append(model_id2)
models.append(model_id4)
models.append(model_id5)


#results = get_data(models,100)
#create_graph(results,100)






prompt1  = '''
    "Below are examples of book descriptions and their corresponding titles:\n\n"
    "Description: A guide to understanding how habits work and how to change them.\n"
    "Title: The Power of Habit: Why We Do What We Do\n\n"
    "Description: A practical approach to building small, consistent changes that lead to major achievements.\n"
    "Title: Atomic Habits: Tiny Changes, Remarkable Results\n\n"
    "Description: A guide to deep, focused work that leads to high productivity and success.\n"
    "Title: Deep Work: Rules for Focused Success in a Distracted World\n\n"
    "Now, generate a concise and descriptive title for the following book description:\n\n"
    f"Title of Description: {description}\n
'''



prompt2  = ''' f"Generate a concise title:{description}\n'''



prompt3 = """
Below are some book descriptions with both their titles and subtitles. Please generate a title and subtitle based on the description.

Example 1:
Description: A comprehensive guide to understanding the science of habits and how to change them.
Title: The Power of Habit
Subtitle: Why We Do What We Do and How to Change

Example 2:
Description: A practical guide to making small changes in behavior to create lasting results.
Title: Atomic Habits
Subtitle: Tiny Changes, Remarkable Results

Example 3:
Description: A guide to focused work and eliminating distractions to achieve personal and professional success.
Title: Deep Work
Subtitle: Rules for Focused Success in a Distracted World

Now, generate a a concise title for the following description:

Book Description: {description}
"""



prompt4  = """
Below are book descriptions and the titles that best match them. The goal is to generate a title that is creative yet descriptive of the content.
Book 1:
Description: A guide to understanding how habits work and how to change them.
Title: The Power of Habit: Why We Do What We Do
Book 2:
Description: A practical guide on making small changes that lead to massive results.
Title: Atomic Habits: Tiny Changes, Remarkable Results
Book 3:
Description: A roadmap to deep, focused work and eliminating distractions.
Title: Deep Work: Rules for Focused Success in a Distracted World
Now, use your creativity to generate an appropriate and engaging title for the following book description:
Book Description: {description}
"""

prompt5  = """
Here are a few examples of books with their descriptions and titles:
Example 1:
Description: A guide to understanding how habits work and how to change them.
Title: The Power of Habit: Why We Do What We Do
Example 2:
Description: A guide to building small habits that have a large impact on achieving success.
Title: Atomic Habits: Tiny Changes, Remarkable Results
Example 3:
Description: A book about focused work and eliminating distractions to achieve success.
Title: Deep Work: Rules for Focused Success in a Distracted World
Now, based on the description below, generate a concise and focused title that captures the key essence of the book:
Book Description: {description}
"""


#Instructional Prompt
prompt6 = """ 
Below are book descriptions and titles:

Description: A guide to habits and change.
Title: The Power of Habit

Description: Small changes lead to big results.
Title: Atomic Habits

Description: Focused work for success.
Title: Deep Work

Generate a title for:

Book Description: {description}
"""


# Instructional Prompt relevant
prompt7 = """ 
Below are book descriptions and titles:

Description: A young girl uncovers the truth behind a world where the moon disappears, and people reappear transformed, with danger at every turn.
Title: Collide (Collide, #1)

Description: A festive twist on a classic tale where an agent battles supernatural Christmas spirits to save his life and loved ones.
Title: The Man From U.N.D.E.A.D.'s Christmas Carol

Generate a title for:

Book Description: {description}
"""

prompts = []

prompts.append(prompt1)
prompts.append(prompt2)
#prompts.append(prompt3)
prompts.append(prompt4)
#prompts.append(prompt5)
prompts.append(prompt6)

prompts.append(prompt7)



results = get_data_for_prompt(prompts,50)
create_graph(results,50)
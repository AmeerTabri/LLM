from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch
from parsing import *
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# The model and its size can be changed
model_name = "google/flan-t5-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Initialize the symantic similarity pre-trained model
SentenceModel = SentenceTransformer('all-mpnet-base-v2')  

# Use the GPU if possoble for better performance
device = "cuda" if torch.cuda.is_available() else "cpu" 
model = model.to(device) 

def score_title(title, content):
    # score based on symantic similarity
    def similarity(str1, str2): 
        embeddings = SentenceModel.encode([str1, str2])
        similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0] 
        return similarity
    
    # Score based on length (penalize titles that are too short or too long)
    def length(title): 
        return max(0, 1 - abs(len(title) - len(content)) / len(content))
    
    print(title, ": ", 0.5*similarity(title, content) + 0.5*length(title))
    return 0.5*similarity(title, content) + 0.5*length(title)
    

def select_best_title(titles, content):
    # Score all titles
    scored_titles = [(title, score_title(title, content)) for title in titles]
    
    # Select the title with the highest score
    best_title = max(scored_titles, key=lambda x: x[1])
    
    return best_title[0]


def generate_title(content, context = "", max_length=7, data_set = ""):  
    prompt = f"Generate a concise title for the following book description:\n\n{content}" 
    prompt = f"giving the context of the content: {context}, Generate a title for this paragraph: {content}"
 
    # Tokenize the input
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to(device)

    outputs = model.generate(
        inputs["input_ids"],
        max_new_tokens=20,  
        num_beams=50,       # Reduce beam search for efficiency
        temperature=1.1,   # Slightly increased for more variety
        do_sample=True,
        early_stopping=False,
        no_repeat_ngram_size=2,  # Prevent repetition of 2-grams
        num_return_sequences=3   # Generate only one sequence
    )

    titles = []  
    for output in outputs:
        titles.append(tokenizer.decode(output, skip_special_tokens=True).strip()) 
    title = select_best_title(titles, content)

    return title

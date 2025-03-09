from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch
from parsing import *
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load Flan-T5 model and tokenizer
model_name = "google/flan-t5-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Initialize the symantic similarity pre-trained model
SentenceModel = SentenceTransformer('all-mpnet-base-v2')  # You can use other models based on your requirements


# Move to the appropriate device
device = "cuda" if torch.cuda.is_available() else "cpu" 
model = model.to(device)
# model = model.half().to(device)

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
        max_new_tokens=12,  # Limit to 3 new tokens
        num_beams=50,       # Reduce beam search for efficiency
        temperature=0.9,   # Slightly increased for more variety
        do_sample=True,
        early_stopping=False,
        no_repeat_ngram_size=2,  # Prevent repetition of 2-grams
        num_return_sequences=3   # Generate only one sequence
    )

    titles = []  
    for output in outputs:
        titles.append(tokenizer.decode(output, skip_special_tokens=True).strip()) 
    title = select_best_title(titles, content)

    print(title)
    return title


def generate_multiple_titles(content, max_length=7, data_set=""):
    prompt = f"Generate a concise title for the following book description:\n\n{content}"

    
    # prompt = f"Generate a title that summarizes the content, focusing on its purpose and intent:\n\n{content}" 
    # prompt = (
    #     "Below are examples of descriptions and their corresponding titles:\n\n"
    #     "Description: This European Standard specifies the process and technical requirements for the development of software.\n"
    #     "Title: Software Development Standards\n\n"
    #     "Description: This document provides safety requirements for railway systems.\n"
    #     "Title: Railway Safety Requirements\n\n"
    #     "Now, generate a concise title for the following description:\n\n"
    #     f"Description: {content}\n"
    #     "Title:"
    # )
    # prompt = (
    #     "Below are examples of book descriptions and their corresponding titles:\n\n"
    #     f"Description: {data_set[1]['content']}\n"
    #     f"Title: {data_set[1]['title']}\n\n"
    #     f"Description: {data_set[2]['content']}\n"
    #     f"Title: {data_set[2]['title']}\n\n"
    #     "Now, "
    #     "Generate a concise title for the following book description:\n\n"
    #     f"Description: {content}\n"
    #     "Title:"
    # )
    
    # Tokenize the input
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to(device)

    # Generate 3 titles
    outputs = model.generate(
        inputs["input_ids"],
        max_new_tokens=20,  # Limit to 20 new tokens
        num_beams=50,       # Beam search for high-quality titles
        temperature=0.7,    # Add some randomness for variety
        do_sample=False,
        early_stopping=True,
        no_repeat_ngram_size=2,  # Prevent repetition of 2-grams
        num_return_sequences=3   # Generate 3 titles
    )

    # Decode the outputs into a list of titles
    titles = [tokenizer.decode(output, skip_special_tokens=True).strip() for output in outputs]

    # Display all generated titles for manual selection
    print("Generated Titles:")
    for i, title in enumerate(titles, 1):
        print(f"{i}. {title}")
    
    # Manual selection
    selected_index = int(input("Select a title (1, 2 or 3): ")) - 1

    # Return the selected title
    selected_title = titles[selected_index]
    print(f"Selected Title: {selected_title}")
    return selected_title


def generate_best_title(content, max_length=7, data_set=""):
    # Define three different prompts to generate titles
    parent_title = "scope"
    prompts = [
        f"Generate a concise title for the following subsection under the section titled '{parent_title}':\n\n{content}",
        f"Given the parent section is titled '{parent_title}', create a suitable title for the following subsection:\n\n{content}",
        f"Generate a descriptive subsection title based on the parent section's title '{parent_title}' for the following content:\n\n{content}",
    ]

    # Tokenize the input for all prompts
    inputs = [tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to(device) for prompt in prompts]

    # Define the parameter set for generating titles
    params = {
        "max_new_tokens": 20,  # Limit new tokens 
        "temperature": 1.0,    # Add randomness
        "num_beams": 30,       # Beam search for high-quality generation
        "top_p": 0.9,          # Top-p for nucleus sampling
        "do_sample": True,     # Enable sampling
        "early_stopping": True,
    }
    
    # Generate titles using the same parameters and different prompts
    titles = []
    for input_data in inputs:
        outputs = model.generate(
            input_data["input_ids"],
            max_new_tokens=params["max_new_tokens"],  
            temperature=params["temperature"],
            num_beams=params["num_beams"],
            top_p=params["top_p"],
            do_sample=params["do_sample"],
            early_stopping=params["early_stopping"], 
        )

        # Decode and store the title
        title = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
        titles.append(title)

    # Display all generated titles for manual selection
    print("Generated Titles:")
    for i, title in enumerate(titles, 1):
        print(f"{i}. {title}")
    
    # Manual selection
    selected_index = int(input("Select the best title (1, 2 or 3): ")) - 1

    # Return the selected title
    selected_title = titles[selected_index]
    print(f"Selected Title: {selected_title}")
    return selected_title
 

# file_num = 1

# file_path = f"inputs/input{file_num}.md"
# output_file_path = f"outputs/output{file_num}.md"

# tree = Tree()
# parse_file(file_path, output_file_path, tree)
# save_as_html(tree, f"outputs/output{file_num}.html")
# # tree.print_sections()

# tree.tree_to_json(empty_cond = False, leaf_cond = True)


def process_json_file(file_path, limit=10): 
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Use a list of dictionaries to store extracted data dynamically
    data_set = []
    for i, item in enumerate(data):
        if i == limit:  
            break
        
        content = item.get("content", "").replace("\n", "").strip()
        section = item.get("section", "")
        title = item.get("title", "")
        
        # Print or log extracted data
        print(f"Section: {section}")
        print(f"Title: {title}")
        print(f"Content: {content}\n")
        
        # Append to data_set
        data_set.append({
            "section": section,
            "title": title,
            "content": content
        }) 

    return data_set
        
# data = process_json_file("data_set.json", limit=3)   
# print("data = ", data)

# content = "This European Standard specifies the process and technical requirements for the development of software      \
#     for programmable electronic systems for use in railway control and protection applications. It is aimed at use      \
#     in any area where there are safety implications. These systems can be implemented using dedicated microprocessors,  \
#     programmable logic controllers, multiprocessor distributed systems, larger scale central processor systems or other \
#     architectures."
# # title = generate_multiple_titles(content)
# title = generate_title(content)

# score = score_title(title[3], content)
# print(f"Semantic similarity score: {score:.4f}")

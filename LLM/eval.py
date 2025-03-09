from datasets import load_dataset
from huggingface_hub import login
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import evaluate


import matplotlib.pyplot as plt
import numpy as np


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
    sample_data = dataset["train"].select(range(examles_number))  # Take the first 20 examples

    # ==========================
    # Load the Model Pipeline
    # ==========================



    tokenizer = AutoTokenizer.from_pretrained(model_id)
    llm = pipeline("text2text-generation", model=model_id, tokenizer=tokenizer, device=device,torch_dtype=torch.float16  # Enable mixed precision
)

    # ==========================
    # Prepare Inputs and Outputs
    # ==========================
    # Prompt to generate titles from book descriptions
    
    input_prompts = [
        #f"Generate a concise and descriptive title for the following book description:\n\n{i['description']}"
        (
            "Below are examples of book descriptions and their corresponding titles:\n\n"
            "Description: A guide to understanding how habits work and how to change them.\n"
            "Title: The Power of Habit: Why We Do What We Do\n\n"
            "Description: A practical approach to building small, consistent changes that lead to major achievements.\n"
            "Title: Atomic Habits: Tiny Changes, Remarkable Results\n\n"
            "Description: A guide to deep, focused work that leads to high productivity and success.\n"
            "Title: Deep Work: Rules for Focused Success in a Distracted World\n\n"
            "Now, generate a concise and descriptive title for the following book description:\n\n"
            f"Description: {i['description']}\n"
            "Title:"
        )
        for i in sample_data
    ]

    # Extract ground truth titles
    ground_truths = [i['title'] for i in sample_data]

    # ==========================
    # Generate Titles
    # ==========================
    # Run the inputs through the model pipeline
    outputs = llm(input_prompts, max_new_tokens=15, clean_up_tokenization_spaces=True)

    # Extract generated titles
    predictions = [output['generated_text'] if 'generated_text' in output else output['summary_text'] for output in outputs]
    '''predictions = []
    for i in range(0, len(input_prompts), batch_size):
        batch = input_prompts[i:i+batch_size]
        outputs = llm(batch, max_new_tokens=15, clean_up_tokenization_spaces=True)
        predictions.extend([output['generated_text'] if 'generated_text' in output else output['summary_text'] for output in outputs])'''

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




# ==========================
# Data Preparation
# ==========================
#Input: models_list: List of models we want to evaluate, examples_number (max value = 31 because of CUDA error: out of memory)
def get_data(models_list, examples_number = 20):
    results = {}
    for model in models_list:
        res = Evaluate_model(model,examples_number)
        results[model] = res
        torch.cuda.empty_cache()  # Clear GPU memory after each model

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


def create_graph(results):
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
    ax.set_xlabel('Models')
    ax.set_ylabel('ROUGE Scores')
    ax.set_title('ROUGE Evaluation Results Across Models')
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
model_id2 = "google/pegasus-xsum"
model_id3 = "google/flan-t5-large"
model_id4 = "facebook/bart-base"

models = []
models.append(model_id1)
models.append(model_id2)
models.append(model_id4)
models.append(model_id5)
models.append(model_id3)


results = get_data(models,20)
create_graph(results)

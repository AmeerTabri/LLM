from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

# Load Flan-T5-small model and tokenizer
model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Move to the appropriate device
device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

def generate_title(content, model, tokenizer, max_length=7):
    """
    Generate a concise title for a given section using a lightweight model.
    """
    # Create the instruction prompt
    prompt = f"Generate a concise and descriptive title:\n\n{content}"
    
    # Tokenize the input
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True).to(device)
    
    # Generate the title
    outputs = model.generate(
        inputs["input_ids"],
        max_length=max_length,
        num_beams= 5,  # Use beam search for better results
        temperature=0.7,  # Controls creativity
        do_sample = True,
        early_stopping=True
    )
    
    # Decode and return the title
    return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

# Example usage
section_content = "A process shall exist for reviewing the identified licenses to determine the obligations, restrictions and  rights granted by each license.  "
title = generate_title(section_content, model, tokenizer)
print("Generated Title:", title)

 
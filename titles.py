from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

# Load Flan-T5-base model and tokenizer
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Move to the appropriate device
device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

def generate_title(content, max_length=7):
    # Create the instruction prompt
    prompt = f"Generate a concise title:\n\n{content}"
    
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
    title = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    print(title)
    return title


content = "This European Standard specifies the process and technical requirements for the development of software for programmable electronic systems for use in railway control and protection applications. It is aimed at use in any area where there are safety implications. These systems can be implemented using dedicated microprocessors, programmable logic controllers, multiprocessor distributed systems, larger scale central processor systems or other architectures."
generate_title(content)


# # Example usage
# section_content = "A process shall exist for reviewing the identified licenses to determine the obligations, restrictions and  rights granted by each license.  "
# title = generate_title(section_content, model, tokenizer)
# print("Generated Title:", title)

# from transformers import GPT2LMHeadModel, GPT2Tokenizer
# import torch

# def generate_title(content):
#     # Load GPT-2 model and tokenizer
#     model_name = "gpt2-large"  # You can replace with "gpt2-medium", "gpt2-large", etc.
#     tokenizer = GPT2Tokenizer.from_pretrained(model_name)
#     model = GPT2LMHeadModel.from_pretrained(model_name)

#     # Check if GPU is available
#     device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#     # Move model to GPU if available
#     model = model.to(device)

#     # Create a prompt for title generation
#     prompt = f"Generate a short title for the following content \n\n{content}\n\nTitle:"

#     # Encode the prompt and move inputs to GPU
#     inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
#     attention_mask = torch.ones(inputs.shape, dtype=torch.long).to(device)  # Attention mask

#     # Generate the output
#     outputs = model.generate(
#         inputs,
#         attention_mask=attention_mask,
#         max_length=120,  # Limit the total length of the generated text
#         num_return_sequences=1,
#         no_repeat_ngram_size=2,
#         temperature=0.7,
#         top_k=50,
#         top_p=0.95,
#         do_sample=True,
#         pad_token_id=tokenizer.eos_token_id,
#     )

#     # Decode the generated text
#     generated_title = tokenizer.decode(outputs[0], skip_special_tokens=True)

#     # Extract only the title (remove the prompt and any extra content)
#     generated_title = generated_title.split("Title:")[1].strip()

#     # Remove any undesired extra content (e.g., author information)
#     if ", Author:" in generated_title:
#         generated_title = generated_title.split(", Author:")[0].strip()

#     return generated_title

# content = "This European Standard specifies the process and technical requirements for the development of software for programmable electronic systems for use in railway control and protection applications. It is aimed at use in any area where there are safety implications. These systems can be implemented using dedicated microprocessors, programmable logic controllers, multiprocessor distributed systems, larger scale central processor systems or other architectures."
# print(generate_title(content))

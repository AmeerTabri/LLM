from datasets import load_dataset
from huggingface_hub import login
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import evaluate

# ==========================
# Authentication and Setup
# ==========================
hf_token = "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"
login(hf_token)

# Device setup
device = "cuda" if torch.cuda.is_available() else "cpu"

# ==========================
# Load Dataset
# ==========================
data_id = "samsum"
dataset = load_dataset(data_id, trust_remote_code=True)

# ==========================
# Load GPT-2-large Model and Tokenizer
# ==========================
model_id = "gpt2-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id).to(device)

# Set the pad_token to eos_token to avoid errors
tokenizer.pad_token = tokenizer.eos_token

# ==========================
# Generate Summaries with GPT-2
# ==========================
def generate_summary(prompt, max_new_tokens=7):
    """
    Generate text using GPT-2 with a summarization prompt.
    """
    # Tokenize input, set attention_mask explicitly
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, padding=True).to(device)
    attention_mask = inputs['attention_mask']
    
    # Generate text
    outputs = model.generate(
        inputs["input_ids"],
        attention_mask=attention_mask,  # Explicitly set attention_mask
        max_new_tokens=max_new_tokens,  # New tokens to generate
        num_beams=5,  # Beam search
        pad_token_id=tokenizer.eos_token_id,  # Ensure padding works
        early_stopping=True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

# Prepare input prompts
input_diags = [f"Summarize the following dialogue:\n\n{i}" for i in dataset['validation']['dialogue'][:20]]
ground_truths = [i for i in dataset['validation']['summary'][:20]]

# Generate predictions (single input per loop to avoid batch issues)
predictions = [generate_summary(prompt) for prompt in input_diags]

# ==========================
# Evaluate with ROUGE
# ==========================
rouge = evaluate.load('rouge')

results = rouge.compute(
    predictions=predictions,
    references=ground_truths,
    use_aggregator=True,
    use_stemmer=True
)

# ==========================
# Print Results
# ==========================
print("-----------------evaluation_results--------------------------------------")
print(results)

# Display example outputs
for i, (input_text, pred, ref) in enumerate(zip(input_diags[:3], predictions[:3], ground_truths[:3])):
    print(f"\nExample {i+1}")
    print("Input Dialogue:", input_text)
    print("Generated Summary:", pred)
    print("Ground Truth Summary:", ref)

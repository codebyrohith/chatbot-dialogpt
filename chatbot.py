from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

def generate_response(user_input, chat_history=None):
    """Generates a chatbot response using DialoGPT."""
    if chat_history is None:
        chat_history = []  # Ensure chat history is initialized as an empty list

    # Encode user input
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

    # Convert chat_history list to a tensor properly
    if len(chat_history) > 0:
        bot_input_ids = torch.cat([chat_history[0], new_input_ids], dim=-1)
    else:
        bot_input_ids = new_input_ids

    # Generate response
    chat_history = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    response = tokenizer.decode(chat_history[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

    print(response)

    return response, [chat_history]  # Store chat history as a list to prevent errors

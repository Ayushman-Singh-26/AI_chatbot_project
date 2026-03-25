from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Function to generate a natural language response based on the user input
def generate_response(command):
    # Encode the user command into tokens
    inputs = tokenizer.encode(command, return_tensors="pt")
    
    # Generate a response from the GPT-2 model
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2, top_p=0.95, temperature=0.7)
    
    # Decode the output into a readable string
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response

# Main function to handle user input and respond dynamically
def virtual_assistant():
    print("Virtual Assistant Activated! Ask me anything.")
    
    while True:
        # Get user input (command)
        command = input("\nYou: ")
        
        # If user wants to exit
        if command.lower() in ["exit", "quit", "bye"]:
            print("Goodbye! Have a great day!")
            break
        
        # Generate response using GPT-2
        response = generate_response(command)
        
        # Output the response
        print(f"Assistant: {response}")

# Start the virtual assistant
if __name__ == "__main__":
    virtual_assistant()

# import torch
# from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2ForQuestionAnswering

# # Initialize the model and tokenizer
# model = GPT2ForQuestionAnswering.from_pretrained('gpt2')
# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# # Define a function to generate a response
# def generate_response(model, tokenizer, question, context):
#     # Encode the question and context
#     input_ids = tokenizer(question + context, return_tensors='pt')

#     # Generate a response
#     with torch.no_grad():
#         output = model(**input_ids)

#     # Get the start and end indices of the answer
#     start_index = output.start_logits.argmax().item()
#     end_index = output.end_logits.argmax().item()

#     # Decode the answer
#     answer = tokenizer.decode(input_ids.input_ids[start_index:end_index+1], skip_special_tokens=True)

#     return answer

# # Define a function to chat with the bot
# def chat_with_bot(model, tokenizer):
#     while True:
#         # Get the user's question
#         question = input("You: ")

#         # Generate a response
#         response = generate_response(model, tokenizer, question, "Answer as if you are a assistant for a coffee shop.")

#         # Print the response
#         print("Chatbot:", response)

#         # Check if the user wants to exit
#         if question.lower() == 'exit':
#             break

# # Start the chat
# chat_with_bot(model, tokenizer)


import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the pretrained model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Define the chatbot's input prompt
input_prompt = "Hello, how can I help you today?"

def generate_response(input_text):
    # Prepare the input text for the model
    input_ids = tokenizer(input_prompt + " " + input_text, return_tensors="pt")["input_ids"]

    # Generate the model's response
    with torch.no_grad():
        output_ids = model.generate(input_ids, max_length=64)

    # Decode the generated response
    decoded_response = tokenizer.decode(output_ids[0].tolist())

    return decoded_response

# Start the chatbot conversation
while True:
    # Get user input
    user_input = input("> ")

    # Generate and print the model's response
    response = generate_response(user_input)
    print(response)

from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Define a separate pad token if it's not already set
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Context with few-shot Q&A examples
context = """
I am an expert in beverages and food items. Ask me any question, and I will provide a detailed answer.

Q: What is Latte?
A: Latte is a type of coffee made with espresso and steamed milk. It is often topped with a small amount of foam and can be flavored with syrups.

Q: What is Cappuccino?
A: Cappuccino is a coffee drink prepared with equal parts of espresso, steamed milk, and foamed milk. It is traditionally served in smaller cups compared to lattes.

Q: What is Chipotle?
A: Chipotle is a fast-casual restaurant chain specializing in burritos, tacos, and bowls made with fresh, customizable ingredients.

Q: What is Subway?
A: Subway is a sandwich chain known for its customizable subs, offering a wide variety of bread, fillings, and toppings.

Q: What is {user_question}?
A:"""

def get_food_or_beverage_answer(question):
    # Fill in the user's question in the Q&A context
    prompt = context.format(user_question=question)

    # Tokenize the input with padding and attention mask
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    
    # Generate the output
    output = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],  # Explicitly pass attention_mask
        max_length=700,
        num_beams=5,  # Use beam search for better results
        no_repeat_ngram_size=2,
        pad_token_id=tokenizer.pad_token_id,
    )

    # Decode the generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    # Extract the answer from the generated text
    answer = generated_text.split(f"What is {question}?\nA:")[1].strip()
    return answer

# Interactive input from the user
while True:
    user_input = input("Ask a question about beverages or food items (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    try:
        answer = get_food_or_beverage_answer(user_input)
        print(f"Answer: {answer}")
    except Exception as e:
        print(f"Error: {e}")






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


# import torch
# from transformers import GPT2LMHeadModel, GPT2Tokenizer

# # Load the pretrained model and tokenizer
# tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# model = GPT2LMHeadModel.from_pretrained("gpt2")

# # Define the chatbot's input prompt
# input_prompt = "Hello, how can I help you today?"

# def generate_response(input_text):
#     # Prepare the input text for the model
#     input_ids = tokenizer(input_prompt + " " + input_text, return_tensors="pt")["input_ids"]

#     # Generate the model's response
#     with torch.no_grad():
#         output_ids = model.generate(input_ids, max_length=64)

#     # Decode the generated response
#     decoded_response = tokenizer.decode(output_ids[0].tolist())

#     return decoded_response

# # Start the chatbot conversation
# while True:
#     # Get user input
#     user_input = input("> ")

#     # Generate and print the model's response
#     response = generate_response(user_input)
#     print(response)

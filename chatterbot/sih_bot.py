# Importing necessary libraries
from chatterbot.trainers import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating a chatbot instance
chatbot = ChatBot('MEdicalBot')

# Creating a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Training the bot on general conversation data
trainer.train('chatterbot.corpus.english')

# Adding domain-specific data about medical regulations
medical_data = [
    {
    },
    {
    },
]

# Training the chatbot on the medical data
for item in medical_data:
    trainer.train([
        item['question'],
        item['answer']
    ])

# Defining a function to get responses from the chatbot
def get_bot_response(user_input):
    response = chatbot.get_response(user_input)
    return str(response)

# Main loop for user interaction
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = get_bot_response(user_input)
    print("MedicalBot:", response)

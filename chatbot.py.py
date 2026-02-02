import sys
import time

def human_flow(text):
    # This simulates a human typing rhythm
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04) 
    print()

def get_response(user_input):
    user_input = user_input.lower()

    # Traditional Greetings
    if "namaste" in user_input or "om" in user_input or "pranam" in user_input:
        return "Namaste. Om. I am here to assist you with a calm mind. How can I be of service today?"
    
    # Inquiry about identity
    elif "who are you" in user_input:
        return "I am a humble assistant created to provide support and guidance. My purpose is to help solve your queries."
    
    # Help/Assistance
    elif "help" in user_input or "sahayata" in user_input:
        return "It would be my duty to help you. Please describe your concern so I can provide the right direction."
    
    # Support/Contact
    elif "contact" in user_input or "email" in user_input:
        return "You may reach out to the team at services.algonivetech@gmail.com for further guidance."
    
    # Work/Task
    elif "work" in user_input or "task" in user_input:
        return "I am currently focused on processing your requests with accuracy. Learning and exploring is a constant process."
    
    # Departure
    elif "exit" in user_input or "bye" in user_input or "shubratri" in user_input:
        return "Namaste. Om Shanti. May your path ahead be peaceful."
    
    # Default response
    else:
        return "I am listening, but I need a bit more clarity to help you better. Could you please rephrase your request?"

def start_chat():
    print("-" * 40)
    human_flow("Namaste.")
    human_flow("Om. I am your support assistant.")
    human_flow("Please tell me how I can help you today.")
    print("-" * 40)
    
    while True:
        # Prompt for user input with a simple arrow
        user_input = input("> ")
        
        # Get response
        response = get_response(user_input)
        
        # Display the response with a natural delay
        time.sleep(0.5)
        sys.stdout.write("Assistant: ")
        human_flow(response)
        
        # End the conversation
        if "exit" in user_input.lower() or "bye" in user_input.lower():
            break

if __name__ == "__main__":
    start_chat()
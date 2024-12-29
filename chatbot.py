# chatbot.py

from paybill import get_paybill_info
from airtime import get_tubonge_details
from customer_support import get_customer_support
from payment import get_payment_instructions
from sms import get_sms_bundles, get_free_sms_info, get_tutext_sms_bundle
from reversal import get_reversal_instructions
from airtime_instructions import show_airtime_instructions

def process_user_message(user_message):
    response = ""

    # Welcome message
    if user_message.lower() in ["hi", "hello","hey","sasa","mambo","vipi","habari"]:
        response = "Hey and Welcome to Airtel Money Chatbot! How can I assist you today?"

    # Handle specific Paybill queries first
    elif "kplc" in user_message.lower() or "electricity" in user_message.lower():
        response = get_paybill_info(user_message)
    elif "kcb" in user_message.lower() or "kcb bank" in user_message.lower():
        response = get_paybill_info(user_message)
    elif "dtb" in user_message.lower() or "diamond trust bank" in user_message.lower():
        response = get_paybill_info(user_message)
    elif "Equity Bank" in user_message.lower() or "equity" in user_message.lower():
        response = get_paybill_info(user_message)    
    elif "MAISHA BANK" in user_message.lower() or "maisha bank" in user_message.lower():
        response = get_paybill_info(user_message)
    elif "Access Bank" in user_message.lower() or "access" in user_message.lower():
        response = get_paybill_info(user_message)  
    elif "Bank of Africa" in user_message.lower() or "boa" in user_message.lower():
        response = get_paybill_info(user_message)
    elif "IM Bank" in user_message.lower() or "im" in user_message.lower():
        response = get_paybill_info(user_message)
    elif "Sportpesa" in user_message.lower() or "sportpesa" in user_message.lower():
        response = get_paybill_info(user_message)

    # Handle generic Payment instructions
    elif "pay" in user_message.lower() or "payment" in user_message.lower():
        response = get_payment_instructions(user_message)
        if not response.startswith("To pay"):  # Check if no specific payment instruction was returned
            response = "Sorry, I don't have specific payment instructions for your query. Could you clarify?"

    # Handle Reversal instructions
    elif "reversal" in user_message.lower() or "reverse" in user_message.lower():
        response = get_reversal_instructions(user_message)

    # Handle Tubonge
    elif "tubonge" in user_message.lower():
        response = get_tubonge_details(user_message)

    # Handle Airtime instructions
    elif "airtime" in user_message.lower():
        response = show_airtime_instructions(user_message)

    # Handle Customer Support
    elif "customer care" in user_message.lower() or "support" in user_message.lower():
        response = get_customer_support()

    # Handle SMS Bundles
    elif "sms bundle" in user_message.lower() or "sms" in user_message.lower():
        response = get_sms_bundles()

    # Handle Free SMS info
    elif "free sms" in user_message.lower():
        response = get_free_sms_info()

    # Handle Tutext SMS Bundle
    elif "tutext" in user_message.lower():
        response = get_tutext_sms_bundle()

    # Default response if no intent is matched
    if not response:
        response = "I'm sorry, I didn't understand that. Could you please rephrase?"

    return response


if __name__ == "__main__":
    print("Airtel Money Chatbot: Type 'quit' to exit.")
    while True:
        user_message = input("You: ").strip()

        if user_message.lower() in ["thank you","thanks","asante","shukran"]:
            print("Airtel Money Chatbot: Welcome, anymore questions, feel free to ask.")
            continue

        if user_message.lower() in ["quit","bye"]:
            print("Airtel Money Chatbot: Goodbye!")    
            break
        elif not user_message:
            print("Airtel Money Chatbot: Please enter a valid query.")
            continue

        response = process_user_message(user_message)
        print(f"Airtel Money Chatbot: {response}")

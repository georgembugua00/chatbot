from data.payment_data import payment_instructions

def get_payment_instructions(user_message):
    user_message = user_message.lower()  # Normalize to lowercase once
    for key, instruction in payment_instructions.items():
        if key.lower() in user_message:  # Compare in lowercase
            return instruction
    return (
        "I can assist with payment instructions for Airtel Money to M-PESA Buy Goods, "
        "Airtel Money to M-PESA Paybill, and Airtel Money Till. "
        "Please specify the payment type you need help with, e.g., 'How do I pay to M-PESA Buy Goods?'"
    )

# Example of how you would call the function
#user_message = "How do I pay to M-PESA Buy Goods?"
#print(get_payment_instructions(user_message))
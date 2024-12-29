# reversal.py

def get_reversal_instructions(user_message):
    # Check for reversal keyword in the user message
    if "reversal" or "reverse" in user_message.lower():
        return (
            "Here is how you can reverse an Airtel Money transaction in Kenya:\n\n"
            "1. Using USSD Code *334#:\n"
            "   - Dial *334# on your phone\n"
            "   - Select Option 8: My account/PIN\n"
            "   - Choose Option 2: Reverse Transaction\n"
            "   - For transactions done immediately, select Option 1: Initiate Transaction Reversal\n"
            "   - Choose the last transaction sent, then enter your Airtel Money PIN to confirm.\n"
            "   - For older transactions, select Option 1: Other WSend Transactions, enter the Transaction ID, and confirm with your Airtel Money PIN.\n\n"
            "2. Reach Out to Airtel Customer Care:\n"
            "   - Dial 100 or 0733 100 100\n"
            "   - Choose Airtel Money services from the voice menu\n"
            "   - Select the Airtel Money Reversal option and speak with a customer care agent.\n"
            "   - This call is free of charge.\n\n"
            "3. Approve a Reversal Request as the Recipient:\n"
            "   - Dial *334# on your phone\n"
            "   - Select Option 8: My account/PIN\n"
            "   - Choose Option 2: Reverse Transaction\n"
            "   - Select Option 2: Approve/Reject Pending Reversal\n"
            "   - Choose the transaction to approve, enter your Airtel Money PIN to approve the reversal.\n\n"
            "Note: The reversal process can take up to 48 hours to complete. Please ensure the funds are still in the recipient’s account for successful reversal."
        )
    elif "reverse" in user_message.lower():
        return (
            "Here is how you can reverse an Airtel Money transaction in Kenya:\n\n"
            "1. Using USSD Code *334#:\n"
            "   - Dial *334# on your phone\n"
            "   - Select Option 8: My account/PIN\n"
            "   - Choose Option 2: Reverse Transaction\n"
            "   - For transactions done immediately, select Option 1: Initiate Transaction Reversal\n"
            "   - Choose the last transaction sent, then enter your Airtel Money PIN to confirm.\n"
            "   - For older transactions, select Option 1: Other WSend Transactions, enter the Transaction ID, and confirm with your Airtel Money PIN.\n\n"
            "2. Reach Out to Airtel Customer Care:\n"
            "   - Dial 100 or 0733 100 100\n"
            "   - Choose Airtel Money services from the voice menu\n"
            "   - Select the Airtel Money Reversal option and speak with a customer care agent.\n"
            "   - This call is free of charge.\n\n"
            "3. Approve a Reversal Request as the Recipient:\n"
            "   - Dial *334# on your phone\n"
            "   - Select Option 8: My account/PIN\n"
            "   - Choose Option 2: Reverse Transaction\n"
            "   - Select Option 2: Approve/Reject Pending Reversal\n"
            "   - Choose the transaction to approve, enter your Airtel Money PIN to approve the reversal.\n\n"
            "Note: The reversal process can take up to 48 hours to complete. Please ensure the funds are still in the recipient’s account for successful reversal."
        )
    
    return None  # If no reversal-related query, return None

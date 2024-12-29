# paybill.py

def get_paybill_info(user_message):
    # Check for KPLC-related keywords
    if "kplc" in user_message.lower() or "electricity" in user_message.lower():
        return (
            "To pay your KPLC bill via Airtel Money, follow these steps:\n\n"
            "1. Dial *334# on your Airtel line.\n"
            "2. Select 'Pay Bill' from the menu.\n"
            "3. Enter the KPLC paybill number:\n"
            "   - For prepaid: 888880\n"
            "   - For postpaid: 888888\n"
            "4. Enter your KPLC account number.\n"
            "5. Enter the amount you wish to pay.\n"
            "6. Confirm the details and enter your Airtel Money PIN to complete the transaction.\n\n"
            "You will receive a confirmation message from Airtel Money and KPLC."
        )
    # Check for KCB-related keywords
    elif "kcb" in user_message.lower() or "kcb bank" in user_message.lower():
        return (
            "To pay your KCB account via Airtel Money, follow these steps:\n\n"
            "1. Dial *334# on your Airtel line.\n"
            "2. Select 'Pay Bill' from the menu.\n"
            "3. Enter the KCB paybill number: 522522.\n"
            "4. Enter your KCB account number.\n"
            "5. Enter the amount you wish to pay.\n"
            "6. Confirm the details and enter your Airtel Money PIN to complete the transaction.\n\n"
            "You will receive a confirmation message from Airtel Money and KCB."
        )
    # Check for DTB-related keywords
    elif "dtb" in user_message.lower() or "diamond trust bank" in user_message.lower():
        return (
            "To pay to your DTB Account via Airtel Money, follow these steps:\n\n"
            "1. Dial *334# on your Airtel line.\n"
            "2. Select 'Pay Bill' from the menu.\n"
            "3. Enter the DTB paybill number: 516600.\n"
            "4. Enter your DTB account number.\n"
            "5. Enter the amount you wish to pay.\n"
            "6. Confirm the details and enter your Airtel Money PIN to complete the transaction.\n\n"
            "You will receive a confirmation message from Airtel Money and DTB."
        )
    
    elif "MAISHA BANK" in user_message.lower() or "maisha bank" in user_message.lower():
        return (
            "To pay to your MAISHA BANK Account via Airtel Money, follow these steps:\n\n"
            "1. Dial *334# on your Airtel line.\n"
            "2. Select 'Pay Bill' from the menu.\n"
            "3. Enter the MAISHA BANK paybill number: 516600.\n"
            "4. Enter your MAISHA BANK account number.\n"
            "5. Enter the amount you wish to pay.\n"
            "6. Confirm the details and enter your Airtel Money PIN to complete the transaction.\n\n"
            "You will receive a confirmation message from Airtel Money and MAISHA BANK."
        )
    
    elif "Equity Bank" in user_message.lower() or "equity" in user_message.lower():
        return (
            "To pay to your Equity Bank Account via Airtel Money, follow these steps:\n\n"
            "1. Dial *334# on your Airtel line.\n"
            "2. Select 'Pay Bill' from the menu.\n"
            "3. Enter the Equity Bank paybill number: 247 247.\n"
            "4. Enter your Equity Bank account number.\n"
            "5. Enter the amount you wish to pay.\n"
            "6. Confirm the details and enter your Airtel Money PIN to complete the transaction.\n\n"
            "You will receive a confirmation message from Airtel Money and Equity Bank."
        )
    
    elif "IM BANK" in user_message.lower() or "im bank" in user_message.lower():
        return (
            "To pay to your IM BANK Account via Airtel Money, follow these steps:\n\n"
            "1. Dial *334# on your Airtel line.\n"
            "2. Select 'Pay Bill' from the menu.\n"
            "3. Enter the IM BANK paybill number: 542 542.\n"
            "4. Enter your IM BANK account number.\n"
            "5. Enter the amount you wish to pay.\n"
            "6. Confirm the details and enter your Airtel Money PIN to complete the transaction.\n\n"
            "You will receive a confirmation message from Airtel Money and IM BANK."
        )
    
    elif "Access Bank PLC" in user_message.lower() or "access bank" in user_message.lower():
        return(
            "To pay to your Access Bank PLC Account via Airtel Money, follow these steps:\n\n"
            "1. Dial *334# on your Airtel line.\n"
            "2. Select 'Pay Bill' from the menu.\n"
            "3. Enter the Access Bank PLC paybill number: 862 863.\n"
            "4. Enter your Access Bank PLC account number.\n"
            "5. Enter the amount you wish to pay.\n"
            "6. Confirm the details and enter your Airtel Money PIN to complete the transaction.\n\n"
            "You will receive a confirmation message from Airtel Money and Access Bank PLC."
        )
    
    elif "Bank of Africa" in user_message.lower() or "BOA" in user_message.lower():
        return(
            "To pay to your Bank of Africa Account via Airtel Money, follow these steps:\n\n"
            "1. Dial *334# on your Airtel line.\n"
            "2. Select 'Pay Bill' from the menu.\n"
            "3. Enter the Bank of Africa paybill number: 972 900.\n"
            "4. Enter your Bank of Africa account number.\n"
            "5. Enter the amount you wish to pay.\n"
            "6. Confirm the details and enter your Airtel Money PIN to complete the transaction.\n\n"
            "You will receive a confirmation message from Airtel Money and Bank of Africa."
        )
    elif "SportPesa" in user_message.lower() or "sportpesa" in user_message.lower():
        return(
            "To pay to your SportPesa Account via Airtel Money, follow these steps:\n\n"
            "1. Dial *334# on your Airtel line.\n"
            "2. Select 'Pay Bill' from the menu.\n"
            "3. Enter the SportPesa paybill number: 955 100.\n"
            "4. Enter your SportPesa account number.\n"
            "5. Enter the amount you wish to pay.\n"
            "6. Confirm the details and enter your Airtel Money PIN to complete the transaction.\n\n"
            "You will receive a confirmation message from Airtel Money and SportPesa."
        )
    
    elif "Betika C2B" in user_message.lower() or "betika" in user_message.lower():
        return(
            "To pay to your Betika C2B Account via Airtel Money, follow these steps:\n\n"
            "1. Dial *334# on your Airtel line.\n"
            "2. Select 'Pay Bill' from the menu.\n"
            "3. Enter the Betika C2B paybill number: 516600.\n"
            "4. Enter your Betika C2B account number.\n"
            "5. Enter the amount you wish to pay.\n"
            "6. Confirm the details and enter your Airtel Money PIN to complete the transaction.\n\n"
            "You will receive a confirmation message from Airtel Money and Betika C2B."
        )
    
    # If no matching keywords are found
    return "Sorry, I don't have information on that paybill. Please provide more details."

# Airtel Money Chatbot

Welcome to the Airtel Money Chatbot repository! This chatbot is designed to assist Airtel Money customers with various inquiries and services, including paying bills, purchasing airtime, checking SMS bundles, and more. The chatbot integrates with Twilio to provide interactive communication via WhatsApp.

---

## Features
- **Bill Payments**: Get instructions for paying bills such as electricity (KPLC) and bank transfers (KCB, DTB).
- **Airtime Purchase**: Receive guidance on buying airtime and learning about Tubonge deals.
- **Reversals**: Access instructions for reversing transactions.
- **Customer Support**: Get contact details for customer support.
- **SMS Bundles**: Check available SMS bundles, free SMS info, and special offers like Tutext.

---

## Files in the Repository

1. `chatbot.py`: Main chatbot script to handle user messages and route them to the appropriate functions.
2. `paybill.py`: Provides payment instructions for different bills.
3. `airtime.py`: Contains details for airtime purchases and Tubonge offers.
4. `customer_support.py`: Handles customer support queries.
5. `payment.py`: Processes payment-related instructions.
6. `sms.py`: Handles SMS bundle queries and special offers.
7. `reversal.py`: Contains reversal instructions.
8. `airtime_instructions.py`: Additional logic for airtime purchases.
9. Other utility files as needed for smooth chatbot functionality.

---

## Prerequisites
- **Python 3.8+**: Ensure Python is installed on your machine.
- **Twilio Account**: For WhatsApp integration.
- **AWS EC2 Instance**: Deploy the chatbot on an EC2 instance with a public IP address.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/airtel-money-chatbot.git
   cd airtel-money-chatbot
   ```

2. **Install Dependencies**:
   Create a virtual environment and install required libraries:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Set Up Twilio**:
   - Sign up for a Twilio account.
   - Configure a Twilio phone number for WhatsApp.
   - Update your Twilio credentials in the `.env` file.

4. **Run the Chatbot Locally**:
   ```bash
   python chatbot.py
   ```

5. **Deploy to EC2**:
   - Upload all files to your EC2 instance.
   - Install dependencies on the EC2 instance.
   - Run the chatbot and ensure it has a public IP accessible for Twilio.

---

## Usage
- Start the chatbot by running `chatbot.py`.
- Interact with the chatbot using WhatsApp via the configured Twilio number.
- Example Queries:
  - "How do I pay my electricity bill?"
  - "What are the available Tubonge deals?"
  - "How do I reverse a transaction?"

---

## Future Enhancements
- Add support for more languages.
- Integrate with Airtel Money APIs for real-time transaction data.
- Expand use cases for gaming bundles and other Airtel services.

---

## Contributing
Contributions are welcome! Please create a pull request or open an issue for any bugs or feature suggestions.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact
For any questions or support, please reach out to **[Your Name]** at **your.email@example.com**.


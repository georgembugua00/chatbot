
def show_airtime_instructions(user_message):
    """
    Displays the instructions on how to buy airtime.
    """
    if "airtime" in user_message.lower():
        return (
            "To buy airtime, dial *544# and follow the prompts. Top up airtime to call other networks as the subscription only covers Airtel calls and discounted rates."
        )
# Call the function to display the instructions

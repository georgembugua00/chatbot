from data.tubonge_data import tubonge_data

def list_tubonge_deals():
    deals = "\n".join(
        [f"- {name}: {details['fee']} ({details['validity']})" for name, details in tubonge_data.items()]
    )
    return f"Available Tubonge Deals:\n{deals}\n\nTo subscribe, dial *544# and follow the prompts."

def get_tubonge_details(bundle_name):
    for name in tubonge_data.keys():
        if bundle_name.lower() in name.lower():
            bundle = tubonge_data[name]
            return (
                f"{name} Details:\n"
                f"- Fee: {bundle['fee']}\n"
                f"- Validity: {bundle['validity']}\n"
                f"- Benefits: {bundle['benefits']}\n"
                f"- Call Rate to Other Networks: {bundle['call_rate']}\n"
                "To subscribe, dial *544# and follow the prompts."
            )
    return "Sorry, I couldn't find details for that Tubonge bundle."

# sms.py

from data.sms_bundle import sms_bundles, sms_info

def get_sms_bundles():
    response = "Airtel SMS Bundles:\n"
    for bundle, details in sms_bundles.items():
        response += f"\n{bundle.replace('_', ' ').title()}:"
        response += f"\n- {details['no_of_sms']} SMS (Airtel to Airtel)\n"
        response += f"- {details['off_net']} SMS to other networks\n"
        response += f"- Price: Ksh {details['price']} for {details['validity']}\n"
    return response

def get_free_sms_info():
    return sms_info["free_sms"]

def get_tutext_sms_bundle():
    return sms_info["tutext_sms_bundle"]

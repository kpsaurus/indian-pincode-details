import json
from pathlib import Path

__version__ = "0.0.1"


CURRENT_DIR = Path(__file__).resolve().parent


def get_pincode_details(pincode):
    """
    Getting the available details from a given pincode.
    If no details is found against that pincode, empty list will be returned.

    Args:
        pincode (int): Pincode

    Returns:
        list: List of details if found.
    """
    details = []

    with open(CURRENT_DIR / 'pincodes.json') as file:
        pincodes = json.load(file)
        details = list(
            filter(lambda address: address["pincode"] == pincode, pincodes))

    return details

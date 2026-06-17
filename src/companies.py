import json

COMPANIES_FILE = "data/companies.json"

def load_companies():

    with open(COMPANIES_FILE, "r") as f:
        return json.load(f)

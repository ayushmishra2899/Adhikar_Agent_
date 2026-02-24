import json

def find_eligible_schemes(user_income):
    with open("backend/schemes.json") as f:
        schemes = json.load(f)

    eligible = []
    for scheme in schemes:
        if user_income <= scheme["income_limit"]:
            eligible.append(scheme)

    return eligible
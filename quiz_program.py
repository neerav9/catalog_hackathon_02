import random

states_and_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata",
    "Jammu and Kashmir": "Srinagar (Summer), Jammu (Winter)"
}

def conduct_quiz():
    score = 0
    total_questions = len(states_and_capitals)
    questions_asked = random.sample(list(states_and_capitals.items()), total_questions)

    print("Welcome to the States and Capitals Quiz!")
    print("Identify the capital of the given state.\n")

    for state, capital in questions_asked:
        answer = input(f"What is the capital of {state}? ")
        if answer.lower() == capital.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {capital}.")
        print()

    print(f"Quiz Over! You scored {score} out of {total_questions}.")

conduct_quiz()


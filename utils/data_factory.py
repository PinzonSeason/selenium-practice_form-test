# utils/data_factory.py
from faker import Faker
import random
import os

fake = Faker("es_MX")  # localización en español de México

# Mapeo de XPATH para State y City
state_xpath_map = {
    "NCR": "//*[@id='react-select-3-option-0']",
    "Uttar Pradesh": "//*[@id='react-select-3-option-1']",
    "Haryana": "//*[@id='react-select-3-option-2']",
    "Rajasthan": "//*[@id='react-select-3-option-3']"
}

city_xpath_map = {
    "Agra": "//*[@id='react-select-4-option-0']",
    "Lucknow": "//*[@id='react-select-4-option-1']",
    "Merrut": "//*[@id='react-select-4-option-2']",
    "Delhi": "//*[@id='react-select-4-option-0']",
    "Gurgaon": "//*[@id='react-select-4-option-1']",
    "Noida": "//*[@id='react-select-4-option-2']",
    "Karnal": "//*[@id='react-select-4-option-0']",
    "Panipat": "//*[@id='react-select-4-option-1']",
    "Jaipur": "//*[@id='react-select-4-option-0']",
    "Jaiselmer": "//*[@id='react-select-4-option-1']"
}

def user_data():
    """Genera datos de usuario para el formulario DemoQA."""
    # Hobbies disponibles
    hobbies = ["Sports", "Reading", "Music"]
    selected_hobbies = random.sample(hobbies, k=random.randint(1, 3))
    
    # States y Cities (dependencias de DemoQA)
    states = {
        "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
        "NCR": ["Delhi", "Gurgaon", "Noida"],
        "Haryana": ["Karnal", "Panipat"],
        "Rajasthan": ["Jaipur", "Jaiselmer"]
    }
    state = random.choice(list(states.keys()))
    city = random.choice(states[state])
    
    # Subjects válidos en DemoQA
    subjects = ["Maths", "English", "Chemistry", "Physics", "Computer Science", "Economics"]
    selected_subjects = random.sample(subjects, k=random.randint(1, 2))
    
    # Ruta de imagen de prueba 
    picture_path = os.path.abspath(os.path.join("tests", "resources", "love_bug.jpg"))
    
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": ''.join(filter(str.isdigit, fake.msisdn()))[:10],
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=60).strftime("%d %B %Y"),
        "subjects": selected_subjects,
        "hobbies": selected_hobbies,
        "picture": picture_path,
        "current_address": fake.address(),
        "state": state,
        "city": city,
        "state_xpath": state_xpath_map[state],
        "city_xpath": city_xpath_map[city]
    }

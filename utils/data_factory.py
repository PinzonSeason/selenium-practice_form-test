# utils/data_factory.py
from faker import Faker
import random
import os

fake = Faker("es_MX")  # localización en español de México

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
        # Fecha con mes completo
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=60).strftime("%d %B %Y"),
        "subjects": selected_subjects,
        "hobbies": selected_hobbies,
        "picture": picture_path,
        "current_address": fake.address(),
        "state": state,
        "city": city,
    }

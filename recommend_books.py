import json
import random

def load_books():
    with open('data/book_database.json', 'r') as file:
        return json.load(file)

def recommend_books(user_profile):
    books = load_books()
    user_genres = user_profile['preferred_genres']
    recommendations = [book for book in books if book['genre'] in user_genres]
    return random.sample(recommendations, min(5, len(recommendations)))

# Example usage
with open('data/user_data.json', 'r') as file:
    user_profile = json.load(file)[0]  # Assuming the first user profile for demo purposes

recommendations = recommend_books(user_profile)
print("Book Recommendations:", recommendations)

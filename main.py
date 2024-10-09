

from scripts.recommend_books import recommend_books
from scripts.update_user_data import update_user_data
from scripts.process_feedback import process_feedback

def main():
    user_id = 1
    # Load user profile (for demo purposes)
    with open('data/user_data.json', 'r') as file:
        user_profiles = json.load(file)
    user_profile = user_profiles[0]  # Assuming the first user profile

    # Generate book recommendations
    recommendations = recommend_books(user_profile)
    print("Book Recommendations:", recommendations)

    # Update user data (for demo purposes)
    new_data = {
        'last_book_read': '1984',
        'preferred_genres': ['Dystopian', 'Science Fiction']
    }
    update_user_data(user_id, new_data)

    # Process feedback (for demo purposes)
    feedback = {
        'book_id': '456',
        'rating': 4,
        'comments': 'Interesting read, but a bit slow in the middle.'
    }
    process_feedback(user_id, feedback)

if __name__ == "__main__":
    main()

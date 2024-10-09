import json

def process_feedback(user_id, feedback):
    with open('data/user_data.json', 'r') as file:
        user_profiles = json.load(file)

    for user in user_profiles:
        if user['id'] == user_id:
            user['feedback'].append(feedback)
            break

    with open('data/user_data.json', 'w') as file:
        json.dump(user_profiles, file)

# Example usage
feedback = {
    'book_id': '123',
    'rating': 5,
    'comments': 'Loved it!'
}
process_feedback(user_id=1, feedback=feedback)

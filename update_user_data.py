import json

def update_user_data(user_id, new_data):
    with open('data/user_data.json', 'r') as file:
        user_profiles = json.load(file)

    for user in user_profiles:
        if user['id'] == user_id:
            user.update(new_data)
            break

    with open('data/user_data.json', 'w') as file:
        json.dump(user_profiles, file)

# Example usage
new_data = {
    'last_book_read': 'To Kill a Mockingbird',
    'preferred_genres': ['Classics', 'Historical Fiction']
}
update_user_data(user_id=1, new_data=new_data)

def save_user(**user):
    print(f'user saved:{user}', type(user))


save_user(id=1, name="Admin")


def save_user_id(**user):
    print(f'id saved: {user["id"]}')


save_user_id(id=1, name="Admin")



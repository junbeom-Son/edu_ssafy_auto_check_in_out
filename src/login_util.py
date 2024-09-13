def get_user_info():
    with open('login_information.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    userEmail, userPassword = content.split()
    return userEmail, userPassword
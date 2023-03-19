import random


def handle_response(user_message:str) -> str:
    p_m = str(user_message).lower()


    if p_m== 'hello':
        return 'Hi'
    
    if user_message == 'roll':
        return str (random.randint(1,6))
    
    if not user_message:
        return 'You didn\'t type anything'
    
    if p_m == '!help':
        return 'modifyable help message'
    
    return 'i didn\'t understand, Try "!help" to get assistance'
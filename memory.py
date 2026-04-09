memory = []

def save(user_input):
    memory.append(user_input)

def get():
    return memory[-3:]  # last 3 interactions
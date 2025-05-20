history = []

def remember(utterance):
    history.append(utterance)

def recall():
    return history[-5:]
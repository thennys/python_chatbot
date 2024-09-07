from difflib import get_close_matches


def get_best_match(user_question:str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: str = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0]
    

def chat_bot(knowledge: dict):
    while True:
        user_input: str = input('You: ')
        best_match: str|None = get_best_match(user_input, knowledge)

        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')

        else:
            print("Hey, Yo...... I dont undert you!!!")


if __name__ == '__main__':
    brain: dict = {
                   'hello, yo,hey': 'Hey buddy!!',
                   ' yo': 'Hey buddy!!',
                   'hey': 'Hey buddy!!',
                   'how are you?': 'I am very good, thanks for asking, what about you',
                   'Do you know what time is it?' : 'Not a clue',
                   'What can you do?': 'I can answer questions',
                   'I am fine, good': 'That feels good to hear',
                   'ok' : 'great'}
    
    chat_bot(knowledge=brain)
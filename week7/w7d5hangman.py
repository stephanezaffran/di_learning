import random

def show_hangman(score):
    print("   +----------+")
    print("   |          |")
    print(f"   |          {'O' if score > 0 else ' '}")
    print(f"   |        {'/' if score > 2 else ' '}{'| |' if score > 1 else '   '}{chr(92) if score > 3 else ' '}")
    print(f"   |       {'^' if score > 2 else ' '} {'|_|' if score > 1 else '   '} {'^' if score > 3 else ' '}")
    print(f"   |        {'/' if score > 4 else ' '}   {chr(92) if score > 5 else ' '} ")
    print(f"   |       {'^' if score > 4 else ' '}     {'^' if score > 5 else ' '}")
    print(" =================")
    print()



wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)
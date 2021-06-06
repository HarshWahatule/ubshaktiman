import random
def clap(msg):
    return "👏".join(msg.split())

def dance(msg):
    dancing_emoji = ["💃","🕺","👯‍♀️"]
    splited_msg = msg.split()
    
    for i in range(len(splited_msg)):
        for rand_emoji in random.choice(dancing_emoji):
            random_emoji = rand_emoji.join(splited_msg)
        return random_emoji
    
    # input : let's go to a party.
    # output : 



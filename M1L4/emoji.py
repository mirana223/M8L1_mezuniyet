import random


def emoji_olusturucu(kemoji):
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"
             ,"\U0001F60E"
             , "\U0001F47E"
             ]
    random_emoji = ""
    for i in range(kemoji):
        random_emoji += random.choice(emoji)
    return random_emoji
def yazi_tura_atici():
    liste = ["yazi", "tura"]
    
    answer = random.choice(liste)

    return answer

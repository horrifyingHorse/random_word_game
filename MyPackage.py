from random import randint

def isvowel(al):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for k in vowels:
        if al == k: return True

    return False

def updatingword(sword, tguess, gi):
    upws = ""
    guess = False
    ex = False
    for i in sword:
        if isvowel(i):
            upws += i + ' '
            continue

        for k in range(len(tguess)):
            if tguess[k] == ' ': continue
            ex = False
            if tguess[k] == i:
                upws += i + ' '
                if k == gi:
                    guess = True
                ex = True
                break

        if ex: continue

        upws += "_ "

    return [upws[:len(upws) - 1], guess]


def rndword():
    wordlist = ['chubby', 'close', 'clam', 'festive', 'cannon', 'auspicious', 'curl', 'owe', 'plane', 'acceptable', 'jelly', 'economic', 'serious', 'murky', 'known', 'cluttered', 'overflow', 'rainstorm', 'wail', 'sugar', 'steel', 'spiky', 'simplistic', 'pray', 'hunt', 'punish', 'mouth', 'communicate', 'ludicrous', 'panoramic', 'tough', 'big', 'calm', 'exotic', 'lamp', 'disastrous', 'condition', 'quixotic', 'root', 'odd', 'stupid', 'lewd', 'skin', 'summer', 'grease', 'cheat', 'tremble', 'cheerful', 'eager', 'shaky', 'poor', 'distance', 'print', 'painful', 'repeat', 'squealing', 'billowy', 'wriggle', 'sick', 'dull', 'remarkable', 'sleep', 'tiresome', 'nod', 'cautious', 'complete', 'apparel', 'burly', 'scattered', 'handy', 'scream', 'zonked', 'toothpaste', 'crib', 'heal', 'efficacious', 'consider', 'ocean', 'adaptable', 'wind', 'perform', 'better', 'acoustic', 'compete', 'grumpy', 'inquisitive', 'noxious', 'far-flung', 'wooden', 'savory', 'smiling', 'pin', 'high-pitched', 'snake', 'ethereal', 'skirt', 'repulsive', 'grieving', 'brief', 'scarecrow', 'pipe', 'release', 'tease', 'reaction', 'creepy', 'mellow', 'unfasten', 'witty', 'self', 'rabid', 'sticky', 'disapprove', 'superficial', 'eggnog', 'lamentable', 'bit', 'horrible', 'undress', 'sable', 'introduce', 'anxious', 'vigorous', 'feeling', 'pan', 'able', 'scrub', 'shirt', 'ticket', 'many', 'chess', 'partner', 'husky', 'splendid', 'profit', 'jump', 'cheap', 'servant', 'aromatic', 'boundary', 'attractive', 'cross', 'craven', 'enjoy', 'fallacious', 'zoom', 'cent', 'charge', 'machine', 'attract', 'abstracted', 'voice', 'tricky', 'trashy', 'embarrass', 'wistful', 'sack', 'cherry', 'fertile', 'type', 'wall', 'concerned', 'rainy', 'development', 'permissible', 'button', 'blushing', 'shade', 'deserve', 'smoke', 'aboriginal', 'magical', 'remove', 'practice', 'wreck', 'warn', 'misty', 'pretend', 'coach', 'slippery', 'stocking', 'ill-fated', 'swing', 'umbrella', 'clap', 'connect', 'cry', 'plan', 'rinse', 'absorbing', 'science', 'mine', 'blink', 'secretive', 'event', 'stage', 'approval', 'glib', 'fly', 'fluffy', 'can', 'nonstop', 'marble', 'shrill', 'start', 'pets', 'drum', 'deserted', 'petite', 'capricious', 'tan', 'war', 'possible', 'lopsided', 'ajar', 'shelf', 'lumber', 'friend', 'found', 'infamous', 'tiny', 'tremendous', 'wait', 'trace', 'writing', 'hurt', 'mess', 'up', 'badge', 'uppity', 'bell', 'pink', 'knowledge', 'volatile', 'impolite', 'sad', 'symptomatic', 'blue', 'messy', 'debonair', 'blush', 'pleasure', 'complex', 'tomatoes', 'van', 'discovery', 'desire', 'color', 'society', 'harmony', 'busy', 'rings']
    selecindex = randint(0, len(wordlist) - 1)
    return wordlist[selecindex]

def endgame(res, sword):
    if res:
        print("Congratulations! You Guessed The Correct Word!")
    else:
        print("GGWP. Better Luck Next Time.")

    print("The Word Was:", sword)
    exit()

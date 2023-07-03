from MyPackage import *

if __name__ == "__main__":
    selecword = rndword()
    s = updatingword(selecword, [], 0)[0]
    storei = 0
    lives = 9
    store = [' '] * (lives * len(selecword))

    while True:
        print(s + "\t\t\t <3 x", lives, "remaining")
        userin = input("Take a Guess: ")
        userin = userin[0].lower()
        store[storei] = userin

        if isvowel(userin):
            print("Vowels are already provided!\n")
            continue

        ls = updatingword(selecword, store, storei)
        s = ls[0]

        if ls[1]:
            print("Correct Guess!!")

            ls1 = s.split()
            gword = ""
            for i in ls1:
                gword += i

            if gword == selecword:
                endgame(True, selecword)

        else:
            lives -= 1
            if lives > 0:
                print("Incorrect Guess.")
            else:
                endgame(False, selecword)


        # print("Lives left: <3 x", lives, "\n\n")
        print("\n")

        storei += 1

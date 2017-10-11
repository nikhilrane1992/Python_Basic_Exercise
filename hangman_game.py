# Hangman game implemenation
"""
Guess a word.
The word to guess is represented by a row of dashes, representing
each letter of the word.

Write a programm to guess a word by the user.

for example
word = "anaconda"
body_part = ["Hair", "Eyes", "Arm", "Shoulder", "Stomach", "Leg"]

- Take a input from user in lower alphabet
- Check the alphabet with your word if match then show the match string
  and remaining dash. if guess alphabet is a then show string  a_a____a
- If you give 6 wrong input then you loose
- On each wrong guess remove one body part from body part list
- If you guess right word then you win
Try your luck ** ^_^ **"""

b_part = ["Hair", "Eyes", "Arm", "Shoulder", "Stomach", "Leg"]
s = "Anaconda"
g_list, w_guess = list(), list()


def show_string(inv, s_list):
    for i in range(len(s_list)):
        if inv != s_list[i] and s_list[i] not in g_list:
            s_list[i] = '-'
    return "".join(s_list)


def print_output(ot):
    if ot == 'l':
        print "************************"
        print "You Loose"
        print "************************"
    elif ot == 'w':
        print "************************"
        print "You Win"
        print "************************"


def main():
    while True:
        s_list = list(s.lower())
        if len(w_guess) > 5:
            print_output('l')
            break
        inv = raw_input("Enter Alphabet: ")
        if not inv.islower():
            print "Please enter lower case alphabet"
            break
        if inv in s_list:
            g_list.append(inv.strip())
            f_str = show_string(inv, s_list)
            if f_str == s.lower():
                print "Guess string: " + f_str
                print_output('w')
                break
            else:
                print "Guess string: " + f_str
        else:
            w_guess.append(inv)
            print "Body part removed: ", b_part.pop()


# Run main function
if __name__ == "__main__":
    main()

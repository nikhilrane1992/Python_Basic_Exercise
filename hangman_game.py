# Hangman game implemenation
# if 6 guess wrong you loose
# if you guess currect then you win
# Try your luck ** ^_^ **

b_part = ["Hair", "Eyes", "Arm", "Shoulder", "Stomach", "Leg"]
s = "Anaconda"
g_list, w_guess = list(), list()


def show_tring(inv, s_list):
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
            f_str = show_tring(inv, s_list)
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
main()

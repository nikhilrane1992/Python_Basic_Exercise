# Find full poker
# In this tutorial we take a input as space seperated.
# Then find out given input is full house or not

LINE_CHAR = 20


def ret_count(n, cards):
    for i in cards:
        if cards.count(i) == n:
            return True


def check_poker_hand(cards):
    if ret_count(2, cards) and ret_count(3, cards):
        print "Full House"
    elif ret_count(4, cards) and ret_count(1, cards):
        print "Four of a kind"
    else:
        print "Poker hand not found"


def main():
    while True:
        cards = raw_input("Enter cards space seperted:\n").split()
        if len(cards) != 5:
            print "Please enter five cards"
            print "-" * LINE_CHAR
            continue
        check_poker_hand(cards)
        print "-" * LINE_CHAR


# Run main function
if __name__ == "__main__":
    main()

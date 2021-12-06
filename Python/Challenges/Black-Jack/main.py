import random as r

cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10] #,11,11,11,11,12,12,12,12,13,13,13,13
total = 0
bot_total = 0
card_count = 0
bot_choices = ["twist", "stick"]

while total < 21 and bot_total < 21: # just doesnt work atm
    cards_left = len(cards)
    r_num = r.randint(0, cards_left-1)
    card = cards[r_num]
    cards.pop(card)
    total += card
    bot_cards_left = len(cards)
    bot_r_num = r.randint(0, cards_left-1)
    bot_card = cards[bot_r_num]
    cards.pop(bot_card)
    bot_total += bot_card
    card_count += 1
    print(f"You have had: {card_count} cards and the total is: {total}")
    if bot_total > 21:
        print("Dealer Bust!")
        break
    else:
        bot_choice = r.choice(bot_choices)
        if bot_choice == "twist":
            pass
        elif bot_choice == "stick":
            break
    if total > 21:
        print("Bust!")
        break
    else:
        choice = input("Twist or stick? ").lower()
        if choice == "twist":
            pass
        elif choice == "stick":
            print(f"Your total is: {total}, the dealer's total was: {bot_total}")
            break

# Deck of cards
import random
import os
import art


def clear():
    return os.system('cls' if os.name in ('nt', 'dos') else 'clear')


set_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def start_over():
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\t")
    if 'y' in start:
        clear()
        print(art.logo)
        start_game(player_cards=[], computer_cards=[], next_card='n')
    elif 'n' in start:
        return 0


def game_final_hand(player, computer, player_sum, computer_sum):
    print(f"    Your Final Hand: {player}, score: {player_sum}")
    print(f"    Computer's Final Hand: {computer}, score: {computer_sum}")


def ace_card(cards_deck):
    index = cards_deck.index(11)
    cards_deck[index] = 1
    return cards_deck


def who_win(user_evaluation, computer_evaluation, user_cards_deck, comp_cards_deck):
    if user_evaluation > computer_evaluation:
        game_final_hand(user_cards_deck, comp_cards_deck, user_evaluation, computer_evaluation)
        print("You Win!!")
        start_over()
    elif user_evaluation < computer_evaluation:
        game_final_hand(user_cards_deck, comp_cards_deck, user_evaluation, computer_evaluation)
        print("You Loose.")
        start_over()


def start_game(player_cards, computer_cards, next_card):
    # Need to import a logo
    # player_card_total = 0
    # comp_card_total = 0
    if next_card == 'n':
        player_cards += random.sample(set_of_cards, 2)
        computer_cards += random.sample(set_of_cards, 2)
        print(f"    Your Cards: {player_cards}")
        print(f"    Computer's First Card: {computer_cards[0]}")
    else:
        player_cards += random.sample(set_of_cards, 1)
        computer_cards += random.sample(set_of_cards, 1)
        print(f"    Your Cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"    Computer's First Card: {computer_cards[0]}")

    player_card_total = sum(player_cards)
    comp_card_total = sum(computer_cards)

    next_card = input("Type 'y' to get another card, type 'n' to pass:\t")
    if next_card == 'y':
        start_game(player_cards=player_cards, computer_cards=computer_cards, next_card=next_card)
    else:
        if player_card_total < 17:
            print(f"Your Card total is less than 16 you need to take card again")
            start_game(player_cards=player_cards, computer_cards=computer_cards, next_card='y')
        elif player_card_total == comp_card_total:
            print(f"It is a Draw both score is {player_card_total}")
        elif ((player_card_total > 21) and (11 in set(player_cards))) and ((comp_card_total > 21) and (11 in set(computer_cards))):
            user_final_eval_cards = ace_card(player_cards)
            user_final_eval_total = sum(user_final_eval_cards)
            comp_final_eval_cards = ace_card(computer_cards)
            comp_final_eval_total = sum(comp_final_eval_cards)
            who_win(user_final_eval_total, comp_final_eval_total, user_final_eval_cards, comp_final_eval_cards)
        elif (player_card_total > 21) and (11 in set(player_cards)):
            final_evaluation_cards = ace_card(player_cards)
            final_evaluation_total = sum(final_evaluation_cards)
            who_win(final_evaluation_total, comp_card_total, final_evaluation_cards, computer_cards)
        elif (comp_card_total > 21) and (11 in set(computer_cards)):
            comp_final_eval_cards = ace_card(computer_cards)
            comp_final_eval_total = sum(comp_final_eval_cards)
            who_win(player_card_total, comp_final_eval_total, player_cards, comp_final_eval_cards)
        elif player_card_total > 21:
            game_final_hand(player_cards, computer_cards, player_card_total, comp_card_total)
            print("That's a Bust.")
            print("You Loose!!")
            start_over()
        elif comp_card_total > 21:
            game_final_hand(player_cards, computer_cards, player_card_total, comp_card_total)
            print("Computer had a Bust.")
            print("You Win!!")
            start_over()
        else:
            who_win(player_card_total, comp_card_total, player_cards, computer_cards)


start_over()

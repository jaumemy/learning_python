import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,'Nine':9, 'Ten':10, 'Jack':10, 
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()
    
    def decklist(self):
        return self.deck


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1



class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet




def take_bet():
    while True:
        try:    
            while True:
                
                bet = int(input(f'How many chips do you want to bet? (You have {chips.total}) '))
                if bet > chips.total:
                    print('Insufficient chips')
                else:
                    return bet

        except:
            print('Please, add a correct number')



def hit(deck,hand):
    
    hitcard = deck.deal()
    hand.add_card(hitcard)
    hand.adjust_for_ace()



def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    ##print(hitcard)
    ##print(hand.value)
    
    while True:
        x = input('Do you want to hit? (Y or N)').lower()
        if x == 'y':
            hit(deck, hand)
            break
        elif x == 'n':
            print("Player stands. Dealer's turn")
            playing = False
            break
        else:
            print('Please just Y or N')
    print('\n'*100)



def show_some(player,dealer):
    
    listplayer = []
    for i in player.cards:
        listplayer.append(i)
    print('\nPlayer has the following cards:\n')
    for i in listplayer:
        print(i)
    print(f"Value = {player.value}")
    
    listdealer = []
    for i in dealer.cards:
        listdealer.append(i)
    print('\n\nDealer has the following cards:\n')
    print('Secret card')
    for i in listdealer[1::]:
        print(i)
    print('\n\n')
        
    
def show_all(player,dealer):
    
    listplayer = []
    for i in player.cards:
        listplayer.append(i)
    
    listdealer = []
    for i in dealer.cards:
        listdealer.append(i)
        
    print(f'\nPlayer value is {player.value} and has the following cards:\n')
    for i in listplayer:
        print(i)
    print(f'\n\nDealer value is {dealer.value} and has the following cards:\n')
    for i in listdealer:
        print(i)
    print('\n\n')




def player_busts(player,chips):
    global playing
    print(f"Player loses. Player's card value is {player.value}. Dealer wins")
    chips.lose_bet()
    print(f'Player has now {chips.total} chips')
    playing = False
        
def player_wins(player, dealer, chips):
    global playing
    if player.value == 21:
        print('Player wins! Cards value is exactly 21!')
        chips.win_bet()
        print(f'Player has now {chips.total} chips')
        playing = False
    
    elif player.value > dealer.value and player.value < 21:
        print(f"Player wins! Player's cards value is {player.value} and Dealer's cards value is {dealer.value} ")
        chips.win_bet()
        print(f'Player has now {chips.total} chips')
        playing = False
        

def dealer_busts(player, dealer, chips):
    global dealerplaying
    print(f"Player wins! Player's cards value is {player.value} and Dealer's cards value is {dealer.value}")
    chips.win_bet()
    print(f'Player has now {chips.total} chips')
    dealerplaying = False
    
def dealer_wins(player, dealer, chips):
    global dealerplaying
    if dealer.value == 21:
        print('Dealer wins. Cards value is exactly 21.')
        chips.lose_bet()
        print(f'Player has now {chips.total} chips')
        dealerplaying = False
    
    elif dealer.value > player.value and dealer.value < 21:
        print(f"Player loses. Player's cards value is {player.value} and Dealer's cards value is {dealer.value}")
        chips.lose_bet()
        print(f'Player has now {chips.total} chips')
        dealerplaying = False
    
def push(player, dealer):
    global dealerplaying
    print(f'Push. Player and dealer tie.{player.value}/{dealer.value} Bet is returned')
    print(f'Player has now {chips.total} chips')
    dealerplaying = False




# Presents a text so the player decides to start playing
startgame = input('Welcome to Blackjack! Enter any key to play ...')
print('\n'*100)

# Creates the deck, shuffles it, creates the two players and deals two cards to each
deck = Deck()
deck.shuffle()
player = Hand()
dealer = Hand()
player.add_card(deck.deal())
player.add_card(deck.deal())
player.adjust_for_ace()
dealer.add_card(deck.deal())
dealer.add_card(deck.deal())
dealer.adjust_for_ace()

# Prepares the chips and asks player for the bet/Start of the playagain loop
chips = Chips()

playagain = True
while playagain:
    print('\n'*100)
    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    player.adjust_for_ace()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    dealer.adjust_for_ace()

    chips.bet = take_bet()

    # Shows the cards, except one hidden for the dealer
    show_some(player,dealer)

    #starts the rounds
    playing = True
    dealerplaying = True
    while playing:

        #asks for hit or pass and shows the cards and value
        if player.value != 21:
        	hit_or_stand(deck, player)
        show_some(player, dealer)

        #checks for player's win or bust
        if player.value == 21:
            print('\n'*100)
            player_wins(player,dealer,chips)
            dealerplaying = False
        elif player.value > 21:
            print('\n'*100)
            player_busts(player, chips)
            dealerplaying = False

        #dealer's turn

    while dealerplaying:


        while dealer.value < player.value and dealer.value <= 21 :
            hit(deck, dealer)

        #shows all cards and checks for different ending scenarios


        if dealer.value > player.value and dealer.value < 21:
            print('\n'*100)
            dealer_wins(player, dealer, chips)
        elif dealer.value > 21:
            print('\n'*100)
            dealer_busts(player, dealer, chips)
        elif player.value == dealer.value:
            print('\n'*100)
            push(player, dealer)
            

    if chips.total == 0:
        print('You ran out of chips. GAME OVER')
        playagain = False
    else:
        
        while True:
            x = input('Do you want to play again? (Y or N)')
            if x.lower() == 'y':
                print(f'Good luck! Next round coming. You have {chips.total} chips')
                break
            elif x.lower() == 'n':
                print(f'Thanks for playing. You leave with {chips.total} chips')
                playagain = False
                break
            else:
                print('Please just Y or N')

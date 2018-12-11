import random

class Card:

    def __init__(self, val, suit):
        self.suit = suit
        self.rank = val

    # Implementing build in methods so that you can print a card object

    def __repr__(self):
        return self.show()

    def show(self):
        return "{} {}".format(self.rank, self.suit)


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    # Display all cards in the deck
    def show(self):
        for card in self.cards:
            print card.show()

    # Generate 52 cards
    def build(self):
        self.cards = []
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            for val in [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']:
                self.cards.append(Card(val, suit))

    # Shuffle the deck
    def shuffle(self):
        random.shuffle(self.cards)

    # Return the top card
    def deal(self):
        return self.cards.pop()


class Player:

    def __init__(self, name):

        self.name = name
        self.hand = []
        self.fakeHand=[]
        self.Clubs=[]
        self.Diamonds=[]
        self.Hearts=[]
        self.Spades=[]
    # Draw n number of cards from a deck
    # Returns true in n cards are drawn, false if less then that

    def draw(self, deck):

        self.Clubs=[]
        self.Diamonds=[]
        self.Hearts=[]
        self.Spades=[]

        for i in range(13):
            card = deck.deal()
            self.hand.append(card)
        for i in self.hand:
            if i.suit == "Clubs":
                self.Clubs.append(i)
            elif i.suit == "Diamonds":
                self.Diamonds.append(i)
            elif i.suit == "Hearts":
                self.Hearts.append(i)
            elif i.suit == "Spades":
                self.Spades.append(i)
        ranks=[2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        self.fakeHand=[self.Clubs,self.Diamonds,self.Hearts,self.Spades]
        for i in self.fakeHand:
            for k in range(len(i)):
                least=i[k]
                for j in range(len(i)):
                    if ranks.index(i[j].rank)<ranks.index(least.rank):
                        least=i[j]
                        i[j]=i[k]
                        i[k]=least
        self.hand=self.Clubs+self.Diamonds+self.Hearts+self.Spades

    def showHand(self):

        print "{}'s hand: {} \n".format(self.name,self.hand)

    def discard(self):
        return self.hand.pop()

def getSuit(x):

    return x.suit

def distribute():

    # function distributing cards to players and making the players global variable for later use

    myDeck = Deck()
    myDeck.shuffle()
    global player1
    global yourName
    yourName=raw_input("Enter name: ")
    player1 = Player(yourName)
    player1.draw(myDeck)
    player1.showHand()
    global player2
    player2 = Player("Player 2")
    player2.draw(myDeck)
    # player2.showHand()
    global player3
    player3 = Player("Player 3")
    player3.draw(myDeck)
    # player3.showHand()
    global player4
    player4 = Player("Player 4")
    player4.draw(myDeck)
    # player4.showHand()

def play():

    # main functions with bidding and playing for user and AI

    print "\nWelcome to my Tarneeb game!!"
    print "\n"
    distribute()
    bids = []
    players=[player1,player2,player3,player4]

    def resort(players,x):

        # helper function for resotring players after each round

        for i in players:

            if i.name==x:
                players=players[players.index(i):]+players[:players.index(i)]

        return players

    def bid():

        x = raw_input(yourName+"'s bid: ")

        if x in ["7","8","9","10","11","12","13"]:

            bids.append(x)

        elif x=="pass":

            bids.append(x)

        else:

            print "Input should be an integer from 7 to 13 or 'pass' "
            bid()

    bid()

    #AI for bidding

    bs=["7","8","9","10","11","12","13"]

    if bids[0]!="pass":

        bs=bs[bs.index(bids[0]):]

    trump=""
    trumps=[]
    bidsNumber=0

    for p in [player2,player3,player4]:

        change=False
        bidsNumber=0

        for s in p.fakeHand:

            if len(s)>bidsNumber:

                bidsNumber=len(s)
                big=s
                change=True

                if p.fakeHand.index(s)==0:

                    trump="Clubs"

                elif p.fakeHand.index(s)== 1:

                    trump="Diamonds"

                elif p.fakeHand.index(s) == 2:

                    trump = "Hearts"

                elif p.fakeHand.index(s) == 3:

                    trump = "Spades"

        trumps.append(trump)

        p.fakeHand.pop(p.fakeHand.index(big))

        for cs in p.fakeHand:

            for c in range(len(cs)):

                if cs[c].rank in ["Ace","King","Queen"]:

                    bidsNumber+=1

        if str(bidsNumber) not in bids and str(bidsNumber) in bs:

            bids.append(str(bidsNumber))
            bs=bs[bs.index(str(bidsNumber)):]

        elif bidsNumber>13:

            bids.append("13")

        else:

            bids.append("pass")

    trumps=[""]+trumps

    for i in range(1,4):

        print "Player " + str(i + 1)+ " bid: " + str(bids[i])

    for b in range(len(bids)):

        try:

            int(bids[b])
            bids[b]=int(bids[b])

        except:

            pass

    greatest=0

    for i in bids:

        if type(i)==int:

            if i>greatest:

                greatest=i
                trump=trumps[bids.index(greatest)]

    if bids.count("pass")==4:

        print random.choice(["Player 2","Player 3"])+ " says: You can't do that Player 4, you gotta bid"
        bids[-1]=7
        greatest=7
        trump=trumps[-1]
        print "Ok fine, we will play for a 7"

    if greatest==bids[0]:

        greatestBidder=yourName

    else:

        greatestBidder="Player "+str(bids.index(greatest)+1)

    for p in players:

        if p.name==greatestBidder:

            if p.name==yourName:

                print "\nHey "+greatestBidder+" , please select Spades, Diamonds, Hearts, or Clubs"

                trump=raw_input("Select Suit:")

                while trump not in ["Spades", "Diamonds", "Hearts", "Clubs"]:

                    print "Wrong suit! choose Spades,Diamonds,Hearts,Clubs"
                    trump=raw_input("Select Suit:")

                print "\n"+random.choice(["Player 2","Player 3","Player4"])+" says: let's beat this tarneeb \n"

            else:

                print "\n"+greatestBidder+" , please select Spades, Diamonds, Hearts, or Clubs"
                print "Uhhhh, I choose: "+trump+"\n"
                print random.choice(["Player 2","Player 3","Player 4"])+" says: let's beat this tarneeb \n"

    discardedCards=[]
    yourTricks=0
    opponentTricks=0

    for i in range (13):

        print "\n"
        player1.showHand()
        players=resort(players,greatestBidder)
        playedCards=[]
        winner=""
        if greatestBidder==yourName or greatestBidder=="Player 3":

            if yourTricks==greatest:

                print "Congratulations, you beat this tarneeb"
                exit()

            elif opponentTricks>13-greatest:

                print "Congratulations, you played yourself. In other words, You took an L :) "
                exit()
        else:

            if opponentTricks==greatest:

                print "Congratulations, you played yourself. In other words, You took an L :) "
                exit()

            elif yourTricks>13-greatest:

                print "Congratulations, you beat this tarneeb"
                exit()

        for j in players:

            if j.name==yourName:

                if playedCards==[]:

                    card=False
                    length=len(j.hand)

                    while not card:

                        k=0
                        played=raw_input(yourName+" plays: ")
                        played=played.split(" ")

                        while len(j.hand)==length and k<length:

                            if played[0]==str(j.hand[k].rank) and played[1]==j.hand[k].suit:
                                p=j.hand.pop(k)
                                playedCards.append(p)
                                card=True

                            k+=1

                        if card==False:

                            print random.choice(["Player 2","Player 4"])+" says: Please stop cheating and play a valid card smh"

                elif playedCards!=[]:

                    su=playedCards[0].suit
                    lst=map(getSuit,j.hand)
                    card=False

                    if su not in lst:

                        card=False
                        length=len(j.hand)

                        while not card:

                            k=0
                            played=raw_input(yourName+" plays: ")
                            played=played.split(" ")

                            while len(j.hand)==length and k<length:

                                if played[0]==str(j.hand[k].rank) and played[1]==j.hand[k].suit:

                                    p=j.hand.pop(k)
                                    playedCards.append(p)
                                    card=True

                                k+=1

                            if card==False:

                                print random.choice(["Player 2","Player 4"])+" says: Please stop cheating and play a valid card smh"

                    else:

                        card=False
                        length=len(j.hand)

                        while not card:

                            k=0
                            played=raw_input(yourName+" plays: ")
                            played=played.split(" ")

                            while len(j.hand)==length and k<length:

                                if played[0]==str(j.hand[k].rank) and played[1]==j.hand[k].suit and played[1]==su:

                                    p=j.hand.pop(k)
                                    playedCards.append(p)
                                    card=True

                                k+=1

                            if card==False:

                                print random.choice(["Player 2","Player 4"])+" says: Please stop cheating and play a valid card smh."

            else:

                if playedCards==[]:

                    temp=filter(lambda x:x.suit!=trump,j.hand)

                    if temp!=[]:

                        g=temp[-1]
                        ranks=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']

                        for i in temp:

                            if ranks.index(i.rank)>ranks.index(g.rank) and \
                                    True not in [u.suit==i.suit and ranks.index(u.rank)>ranks.index(i.rank) for u in discardedCards]:
                                g=i

                        if g==temp[-1]:

                            y=temp[-1]
                            if [x for x in temp if ranks.index(x.rank)<ranks.index(y.rank)]:
                                g=[x for x in temp if ranks.index(x.rank)<ranks.index(y.rank)][0]

                        playedCards.append(g)
                        p=j.hand.pop(j.hand.index(g))

                    else:

                        temp=filter(lambda x:x.suit==trump,j.hand)
                        g=temp[-1]
                        ranks=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']

                        for i in temp:

                            if ranks.index(i.rank)>ranks.index(g.rank) and \
                                    True not in [u.suit==i.suit and ranks.index(u.rank)>ranks.index(temp[-1].rank) for u in discardedCards]:
                                g=i
                        playedCards.append(g)
                        p=j.hand.pop(j.hand.index(g))

                else:

                    temp=filter(lambda x:x.suit==playedCards[0].suit,j.hand)

                    if temp==[]:

                        test=[x.suit==trump for x in playedCards]
                        temp1=filter(lambda x:x.suit==trump,j.hand)
                        # use other algorithm here with change
                        gr=None
                        temp1.reverse()

                        for i in temp:
                            test=[x>i.rank for x in playedCards]
                            if False in test:
                                gr=i
                                break

                        if gr!=None and temp!=[]:

                            playedCards.append(gr)
                            p=j.hand.pop(j.hand.index(gr))

                        elif gr==None and temp!=[]:

                            temp.reverse()
                            playedCards.append(temp[-1])
                            p=j.hand.pop(j.hand.index(temp[-1]))

                        else:

                            playedCards.append(j.hand[-1])
                            p=j.hand.pop(-1)

                    else:

                        ranks=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
                        gr=temp[-1]
                        test=[x.suit==trump for x in playedCards]

                        if True in test:

                            playedCards.append(temp[-1])
                            p=j.hand.pop(j.hand.index(temp[-1]))

                        else:

                            gr=None
                            temp.reverse()
                            for i in temp:
                                test=[ranks.index(x.rank)>ranks.index(i.rank) for x in playedCards]
                                if False in test:
                                    gr=i
                                    break

                            if gr!=None and temp!=[]:

                                playedCards.append(gr)
                                p=j.hand.pop(j.hand.index(gr))

                            elif gr==None and temp!=[]:

                                temp.reverse()
                                playedCards.append(temp[-1])
                                p=j.hand.pop(j.hand.index(temp[-1]))

                            else:

                                playedCards.append(j.hand[-1])
                                p=j.hand.pop(-1)

                print j.name+" plays: "+str(p.rank)+" "+p.suit

        plays=playedCards

        if True in [x.suit==trump for x in plays] and [x.suit==trump for x in plays].count(True)>1:

            ranks
            plays=[x for x in plays if x.suit==trump]
            t=plays[0]
            for i in plays:
                if ranks.index(i.rank)>ranks.index(t.rank):
                    t=i
            t=playedCards.index(t)
            winner=players[t]
            players=resort(players,winner.name)

            if winner.name==yourName or winner.name=="Player 3":
                yourTricks+=1

            else:
                opponentTricks+=1


        elif True in [x.suit==trump for x in plays] and [x.suit==trump for x in plays].count(True)==1:

            plays=[x for x in plays if x.suit==trump]
            t=plays[0]
            t=playedCards.index(t)
            winner=players[t]
            players=resort(players,winner.name)

            if winner.name==yourName or winner.name=="Player 3":
                yourTricks+=1

            else:
                opponentTricks+=1

        elif True not in [x.suit==trump for x in plays]:

            plays=[x for x in plays if x.suit==playedCards[0].suit]
            t=plays[0]
            for i in plays:
                if ranks.index(i.rank)>ranks.index(t.rank):
                    t=i
            t=playedCards.index(t)
            winner=players[t]
            players=resort(players,winner.name)

            if winner.name==yourName or winner.name=="Player 3":
                yourTricks+=1

            else:
                opponentTricks+=1

        print "\nWinner is: " + winner.name + "\n"
        print "Your team's tricks: " + str(yourTricks)
        print "Opponents' tricks: " + str(opponentTricks)

play()

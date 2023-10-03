import random

print( "Welcome to the Blackjack table partner! 'Sit down' to start playing or if you don't want to, just 'leave.'" )
nextInput = input( "Type action: " )

while nextInput != "leave":
    if nextInput == "sit down":
        card1 = random.randint( 1, 11 )
        card2 = random.randint( 1, 11 )
        dealerCard1 = random.randint( 1, 11 )
        dealerCard2 = random.randint( 1, 11 )
        print( "You have two cards, {0} and {1}.".format( card1, card2 ) )
        print( "I have one {0}.".format( dealerCard1 ) )
        print( "Would you like to 'hit' or 'stick'?" )
    elif nextInput == "stick":
        totalPlayer = card1 + card2
        totalDealer = dealerCard1 + dealerCard2
        
        
    else:
        print( "What do you want to do, partner?" )

    nextInput = input( "Type action: " )

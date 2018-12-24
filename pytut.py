import random
print("Hello, World!")
name = input ("What is your name?")
print ("Hello," + name)
usrhltst = input ("User Highlight Ticket:")
print ("[Now Initalizing]")
pause = input ("[Press enter to CONTINUE]")
yous=random.randint(0, 1000)
def lead():
    import random
    one=random.randint(0, 1000)
    two=random.randint(0, 1000)
    three=random.randint(0, 1000)
    four=random.randint(0, 1000)
    five=random.randint(0, 1000)
    player1="Tom"
    player2="James"
    player3="George"
    player4="Charlton"
    player5="Branden"
    print ("You:Player:" + str(name) + "  Score:" + str(yous))
    print ("Stranger:Player:" + str(player1) + "  Score:" + str(one))
    print ("Stranger:Player:" + str(player2) + "  Score:" + str(two))
    print ("Stranger:Player:" + str(player3) + "  Score:" + str(three))
    print ("Stranger:Player:" + str(player4) + "  Score:" + str(four))
    print ("Stranger:Player:" + str(player5) + "  Score:" + str(five))
    input ("")
    print("Refresh:")
    lead()
lead()

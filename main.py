# This is a sample Python script.
import random

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
cards = []


def generateDeck():
    # card = (suit, number)
    suits = ['h', 'd', 's', 'c']

    for i in range(13):
        for suit in suits:
            card = (suit, i + 1)
            cards.append(card)
    # print(cards)


def shuffle():
    midOfDeck = int(len(cards) / 2)
    # print(midOfDeck)
    randDist = 2
    randMid = random.randint(midOfDeck - randDist, midOfDeck + randDist)
    p1 = randMid
    p2 = randMid + 1
    shuffled = []
    while (p2 < len(cards) and p1 > 0):
        shuffled.append(cards[p1])
        shuffled.append(cards[p2])
        p1 -= 1
        p2 += 1

    while p1 > 0:
        shuffled.append(cards[p1])
        p1 -= 1

    while p2 < len(cards):
        shuffled.append(cards[p2])
        p2 += 1

    cards.clear()
    for card in shuffled:
        cards.append(card)


def shuffleMultiple(times):
    for i in range(times):
        shuffle()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generateDeck()
    shuffleMultiple(5)
    print(cards)
    players = [[], [], [], [], []]
    for i in range(5 * len(players)):
        playerNum = i % 5
        players[playerNum].append(cards.pop())
        # print(f"added to player {playerNum}")

    for player in players:
        print(player)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

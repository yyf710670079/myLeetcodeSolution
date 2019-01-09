# coding = utf-8
__author__ = "Yufeng Yang"

"""
In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.

Initially, all the cards start face down (unrevealed) in one deck.

Now, you do the following steps repeatedly, until all cards are revealed:

    Take the top card of the deck, reveal it, and take it out of the deck.
    If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
    If there are still unrevealed cards, go back to step 1.  Otherwise, stop.

Return an ordering of the deck that would reveal the cards in increasing order.

The first entry in the answer is considered to be the top of the deck.

 

Example 1:

Input: [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]
Explanation: 
We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter), and reorder it.
After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
We reveal 13, and move 17 to the bottom.  The deck is now [17].
We reveal 17.
Since all the cards revealed are in increasing order, the answer is correct.

"""


def is_reveal_increasing(deck):
    """

    :param deck: List[int]
    :return: bool
    """
    last_revealed = deck.pop(0)
    deck.append(deck.pop(0))

    while deck:
        if deck[0] < last_revealed:
            return False
        else:
            last_revealed = deck.pop(0)
            if deck:
                deck.append(deck.pop(0))

    return True


def deckRevealedIncreasing(deck):
    """
    :param deck: List[int]
    :return: List[int]

    explanation:
        This is a simulation solution.
        We first sort the deck in increasing order.
        Then we create an index list.
        Because we reveal one and take the second to the bottom,
        so we will reveal the ans[0] and take the ans[1] to the bottom.
        After that, we reveal ans[2]!

        so the index list denotes the following order which we place our ans list temporarily.


    """

    N = len(deck)
    index = [i for i in range(N)]
    ans = [0] * N

    for card in sorted(deck):
        ans[index.pop(0)] = card
        if index:
            index.append(index.pop(0))

    return ans


if __name__ == "__main__":
    t1 = [17, 13, 11, 2, 3, 5, 7]
    t1_out = deckRevealedIncreasing(t1)

    assert(is_reveal_increasing(t1_out))

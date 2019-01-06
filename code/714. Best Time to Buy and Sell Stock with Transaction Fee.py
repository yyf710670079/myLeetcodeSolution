# coding = utf-8
__author__ = "Yufeng Yang"

"""
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i;
and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
"""


def maxProfit(prices, fee):
    """
    :param prices: List[int]
    :param fee: int
    :return: int

    cash means the maximum profit if we did not held the stock at i-1 th step
    hold means the maximum profit if we hold the stock at i-1 th step

    """

    cash, hold = 0, -prices[0]

    for i in range(1, len(prices)):
        # if we do not held the stock at i th step, we might either sell it at i-1 th step
        # or continue to held no stock from i-1 th step
        cash = max(cash, hold + prices[i] - fee)

        # if we hold the stock at i th step, we might either held it at i-1 th step
        # or buy one at i-1 th step
        hold = max(hold, cash - prices[i])

    return cash


if __name__ == "__main__":
    assert(maxProfit([1, 3, 2, 8, 4, 9], 2) == 8)
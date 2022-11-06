def maxProfit(prices: list[int]):
    buy = prices[0]
    maxProfit = -1
    for sell in prices:
        if sell - buy < 0: buy = sell
        maxProfit = max(maxProfit, sell - buy)




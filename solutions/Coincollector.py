from math import inf


def solve(partition, listings, n):
    """
    Solve the problem here.
    :return: The expected output.
    """


    # Setwise min-max bounds:
        # min: {min(min(coin_stock) over coinlistings) over coinset}
        # max: {min(sum(coin_stock) over coin_type) over coinset}

    p1, p2, p3 = partition

    set_bounds = [
        (inf, inf),
        (inf, inf),
        (inf, inf)
        ]

    can_touch = [
        p1.intersection(set(listings)) == p1,
        p2.intersection(set(listings)) == p2,
        p3.intersection(set(listings)) == p3
        ]

    for coin in listings:
        stocks = []
        prices = []

        for a, b in listings[coin]:
            stocks.append(a)
            prices.append(b)

        if coin in p1 and can_touch[0]:
            prev_min, prev_max = set_bounds[0]
            set_bounds[0] = (min(prev_min, min(stocks)), min(prev_max, sum(stocks)))

        elif coin in p2 and can_touch[1]:
            prev_min, prev_max = set_bounds[1]
            set_bounds[1] = (min(prev_min, min(stocks)), min(prev_max, sum(stocks)))

        elif coin in p3 and can_touch[2]:
            prev_min, prev_max = set_bounds[2]
            set_bounds[2] = (min(prev_min, min(stocks)), min(prev_max, sum(stocks)))

    # print(set_bounds)

    largest_possible = sum(set_bounds[i][1] for i in range(3))
    if n > largest_possible:
        return 'impossible'


    coins_dp = dict()

    coin_stocks = dict()

    for coin in listings:
        stocks = []
        prices = []
        
        for a, b in listings[coin]:
            stocks.append(a)
            prices.append(b)
        coin_stocks[coin] = stocks


        if (coin in p1 and can_touch[0]) or (coin in p2 and can_touch[1]) or (coin in p3 and can_touch[2]):
            top = sum(stocks)
            
            target = -1

            if coin in p1 and can_touch[0]:
                target = set_bounds[0][0]
            elif coin in p2 and can_touch[1]:
                target = set_bounds[1][0]
            elif coin in p3 and can_touch[2]:
                target = set_bounds[2][0]
            if target != -1:
                dp = knapsack(target, stocks, prices)
        coins_dp[coin] = dp
    

    def x_c(x, c):
        top = sum(coin_stocks[c])
        return coins_dp[c][top - x]

    def x_s_i(x, i):
        val = 0
        for coin in coins_dp:
            if coin in p1 and i == 1:
                val += x_c(x, coin)
            elif coin in p2 and i == 2:
                val += x_c(x, coin)
            elif coin in p3 and i == 3:
                val += x_c(x, coin)
        return val


    boss_stock = []
    boss_prices = []
    boss_target = n

    for i in range(len(set_bounds)):
        start, end = set_bounds[i]
        if max(start, end) != inf:
            for z in range(start, end + 1):
                boss_stock.append(z)
                boss_prices.append(x_s_i(z, i+1))

    if len(boss_stock) == 0 or sum(boss_stock) < boss_target:
        return 'impossible'

    boss_dp = knapsack(boss_target, boss_stock, boss_prices)
    boss_top = sum(boss_stock)

    return boss_dp[boss_top - boss_target]


def knapsack(target, stocks, prices):
    """
    Minimize sum(prices)
    w.r.t sum(stocks) >= target
    
    Binary knapsack.

    """
    highest = sum(prices)
    top = sum(stocks)
    dp = [[highest for _ in range(top + 1)] for _ in range(len(stocks) + 1)]

    for i in range(len(stocks)+1):
        for j in range(top):
            if i == 0:
                dp[i][j] = highest
            elif j >= stocks[i - 1]:
                prev = dp[i-1][j]
                curr = dp[i-1][j - stocks[i - 1]] - prices[i - 1]
                dp[i][j] = min(prev, curr)
            else:
                dp[i][j] = dp[i-1][j]
    for i in range(len(stocks) + 1):
        dp[i][-1] = 0

    return dp[-1]

    # min_cost(x copies of c1)
    return

def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.
    """

    n, m = list(map(int, input().split(' ')))
    pure_names = [
        'Zulian',
        'Sandfury',
        'Skullsplitter',
        'Bloodscalp',
        'Razzashi',
        'Hakkari',
        'Witherbark',
        'Gurubashi',
        'Vilebranch'
        ]

    listings = dict()

    for _ in range(m):
        coin, stock, price = input().split(' ')
        if coin in listings:
            listings[coin].append((int(stock), int(price)))
        else:
            listings[coin] = [(int(stock), int(price))]

    partition = [
        {'Zulian', 'Razzashi', 'Hakkari'},
        {'Sandfury', 'Skullsplitter', 'Bloodscalp'},
        {'Gurubashi', 'Vilebranch', 'Witherbark'}
    ]

    if all(len(list(p.intersection(listings))) < 3 for p in partition):
        print('impossible')
        return 'impossible'

    min_price = solve(partition, listings, n)
    print(min_price)



    # Setwise min-max bounds:
        # min: {min(min(coin_stock) over coinlistings) over coinset}
        # max: {min(sum(coin_stock) over coin_type) over coinset}
    # x|s1| + y|s2| + z|s3| >= N
    # minimize cost(x copies of |s1| + ... + z copies of |s3|)

    # minimize cost(q copies of |sj|) for q in (x, y, z)
    # and j in (1, ..., j)


    # x(c1 + c2 + c3) + y(c4 + c5 + c6) + z(c7 + c8 + c9) >= N
    # minimize 

    # k copies of ci. Fill using DP.

    # x|s1| = min_cost(x copies of c1) + ... + min_cost(x copies of c3)

    return min_price


def main():
    # def pretty(arr):
    #     for idx, row in enumerate(arr):
    #         print(row)
    #     return
    
    # stocks = [3, 5, 7]
    # prices = [100, 400, 60]
    # target = 8

    # dp = knapsack(target, stocks, prices)
    # pretty(dp)
    
    return driver()


if __name__ == '__main__':
    main()

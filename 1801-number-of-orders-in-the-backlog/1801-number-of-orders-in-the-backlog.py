import heapq
class Solution:
    def getNumberOfBacklogOrders(self, orders) -> int:
        '''
        orderType :-
        0 - it is a batch of buy orders
        1 - it is a batch of sell orders
        
        Condition 1:
            - `buy` order:
                - look for the sell order with the smallest price in the backlog
                - if that sell order's price is smaller than or equal to the current
                  buy order's price, they will match and be executed, and that sell will be 
                  removed from the backlog.
        Condition 2:
            - `sell` order:
                - look for the buy order with the largest price in the backlog
                - if that buy order's price is larger than or equal to the current
                  sell order's price, they will match and be executed, and that buy will be 
                  removed from the backlog.
          
        '''
        
        # buy = 0
        # sell = 1
        
        # sell <= buy
        # buy >= sell
        
            
        sell, buy = [], []
        for p, a, t in orders:
            if t == 0:
                heapq.heappush(buy, [-p, a])
            else:
                heapq.heappush(sell, [p, a])
            while sell and buy and sell[0][0] <= -buy[0][0]:
                k = min(buy[0][1], sell[0][1])
                buy[0][1] -= k
                sell[0][1] -= k
                if buy[0][1] == 0: heapq.heappop(buy)
                if sell[0][1] == 0: heapq.heappop(sell)
        return sum(a for p, a in buy + sell) % (10**9 + 7)
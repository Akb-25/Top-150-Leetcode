profit=0
        max=0
        buy=0
        min=float("inf")
        area=len(prices)
        for i in range(area):
            if prices[i]<min:
                min=prices[i]
            if i!=area-1:
                if prices[i]>prices[i+1]:
                    profit+=prices[i]-min
                    min=float("inf")
            if i == area-1:
                profit+=prices[i]-min
        return profit
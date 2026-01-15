class Solution(object):
   def shoppingOffers(self, price, special, needs):
        memo = {}

        def dfs(curr_needs):
            if tuple(curr_needs) in memo:
                return memo[tuple(curr_needs)]

        
            min_cost = sum(curr_needs[i] * price[i] for i in range(len(price)))

           
            for offer in special:
                new_needs = []
                for i in range(len(price)):
                    if curr_needs[i] < offer[i]:
                        break  
                    new_needs.append(curr_needs[i] - offer[i])
                else:
                    
                    min_cost = min(min_cost, offer[-1] + dfs(new_needs))

            memo[tuple(curr_needs)] = min_cost
            return min_cost

        return dfs(needs)

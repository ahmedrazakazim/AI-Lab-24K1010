class UtilityAgent:
    def __init__(self, data):
        self.restaurants = data

    def select(self):
        best_r = None
        max_u = -float('inf')
        for name, info in self.restaurants.items():
            u = info['Rating'] - info['Distance']
            print(f"Restaurant {name} Utility = {u}")
            if u >= max_u:
                max_u = u
                best_r = name
        print(f"Selected Restaurant: {best_r}")

data = {'A': {'Distance': 3, 'Rating': 7}, 'B': {'Distance': 5, 'Rating': 9}}
agent = UtilityAgent(data)
agent.select()

class TrafficEnvironment:
    def __init__(self, status):
        self.status = status

    def get_percept(self):
        return self.status

class ReflexAgent:
    def act(self, percept):
        if percept == "Heavy Traffic":
            return "Extend Green Time"
        return "Normal Green"

def run_task1():
    states = ["Heavy Traffic", "Light Traffic"]
    for s in states:
        env = TrafficEnvironment(s)
        agent = ReflexAgent()
        percept = env.get_percept()
        action = agent.act(percept)
        print(f"Percept: {percept} -> Action: {action}")

run_task1()

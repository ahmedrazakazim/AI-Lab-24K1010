class Environment:
    def __init__(self):
        self.states = ["Yes", "No", "Yes", "Yes", "No", "No", "Yes", "No"]
        self.step = 0
    def get_percept(self):
        state = self.states[self.step]
        self.step += 1
        return state

class ModelBasedAgent:
    def __init__(self):
        self.model = {"previous": None, "light": "OFF"}
    def act(self, percept):
        if percept == "Yes" and self.model["light"] == "OFF":
            action = "Turn lights ON"
            self.model["light"] = "ON"
        elif percept == "No" and self.model["light"] == "ON":
            action = "Turn lights OFF"
            self.model["light"] = "OFF"
        else:
            action = "No action"
        self.model["previous"] = percept
        return action

def run_task():
    env = Environment()
    agent = ModelBasedAgent()
    for i in range(8):
        p = env.get_percept()
        a = agent.act(p)
        print(f"Step {i+1}: Presence: {p}, Action: {a}, Model: {agent.model}")

run_task()

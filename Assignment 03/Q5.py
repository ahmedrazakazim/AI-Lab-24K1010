class LearningAgent:
    def __init__(self):
        self.q_table = {"Play": 0, "Rest": 0}
        self.alpha = 0.1

    def update(self, action, reward):
        self.q_table[action] += self.alpha * (reward - self.q_table[action])

def run_task5():
    agent = LearningAgent()
    for i in range(1, 11):
        action = "Play"
        reward = 5
        agent.update(action, reward)
        print(f"Step {i}: Action {action} Reward {reward}")
    print("Q-table Updated:", agent.q_table)

run_task5()

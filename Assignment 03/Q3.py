class GoalBasedAgent:
    def __init__(self, subjects):
        self.subjects = subjects
        self.goal = "All subjects completed"

    def study(self):
        while self.subjects:
            subject = self.subjects.pop(0)
            print(f"Studying {subject}")
        print(f"Goal Achieved: {self.goal}")

agent = GoalBasedAgent(["AI", "Math", "Physics"])
agent.study()

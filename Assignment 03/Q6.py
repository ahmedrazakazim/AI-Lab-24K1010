class Building:
    def __init__(self):
        self.rooms = ['safe', 'safe', 'fire', 'safe', 'fire', 'safe', 'safe', 'safe', 'fire']
        self.names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']

    def show(self):
        for i in range(0, 9, 3):
            line = ""
            for status in self.rooms[i:i+3]:
                symbol = "🔥" if status == "fire" else " "
                line += f"[{symbol}] "
            print(line)

def start_fire_mission():
    b = Building()
    for idx, room_name in enumerate(b.names):
        print(f"Entering Room: {room_name}")
        if b.rooms[idx] == 'fire':
            print("Action: Extinguishing Fire")
            b.rooms[idx] = 'safe'
        b.show()
    print("Mission Complete.")
    b.show()

start_fire_mission()

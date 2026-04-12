total = 52
red = 26
p_red = red / total
print(f"\nP(Red card) = {red}/{total} = {p_red:.4f}")
 
hearts = 13
p_heart = hearts / red
print(f"P(Heart | Red) = {hearts}/{red} = {p_heart:.4f}")
 
face_total = 12
face_dia = 3
p_dia = face_dia / face_total
print(f"P(Diamond | Face card) = {face_dia}/{face_total} = {p_dia:.4f}")
 
face_spade_q = 6
p_spade_q = face_spade_q / face_total
print(f"P(Spade or Queen | Face card) = {face_spade_q}/{face_total} = {p_spade_q:.4f}")

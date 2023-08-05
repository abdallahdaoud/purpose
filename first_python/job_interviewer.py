
name = input("Enter your name pleas: ")

questions = (
             ("What is the type of 2.1?\n", "flout"), 
             ("If we run blow code, then printed value is\nx = 4//3\nprint(x)\n", "1"),
             ("If we run blow code, then printed value is:\n  print(2.1 > 2)\n", "true")
            )

mark = 3
for q in questions:
    if input(q[0]).lower() != q[1]:
        mark -= 1

print(f"Thank you {name} Your mark is {mark}")
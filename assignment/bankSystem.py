"""
a simple bank system that allows users to assign their name and will have their own id correlating to their order of arrival
"""
names = []
while True:
    inp = input("Enter name or ID: ").strip()
    if not inp:
        continue
    try:
        id_val = int(inp)
        if id_val < 1 or id_val > len(names):
            print("Invalid ID")
        else:
            print(names[id_val - 1])
    except ValueError:
        names.append(inp)
        print(f"Assigned ID: {len(names)}")
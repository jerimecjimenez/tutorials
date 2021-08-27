# Ex. 3-4
nameInvite = ["Nesha", "Kayeh", "Zion"]
addInvite = ["Carlo", "Joash", "Jerome"]

print(nameInvite[0] + " You are invited to a dinner!")
print(nameInvite[1] + " You are invited to a dinner!")
print(nameInvite[2] + " You are invited to a dinner!")

# Ex. 3-5
print(nameInvite[1] + " can't make it to dinner!")
nameInvite.pop(1)
nameInvite.insert(1, "Jam")

print(nameInvite[0] + " You are invited to a dinner!")
print(nameInvite[1] + " You are invited to a dinner!")
print(nameInvite[2] + " You are invited to a dinner!")

# Ex. 3-6
print("There's a new table available for guests!")
nameInvite.insert(0, "Carlo")
nameInvite.insert(2, "Joash")
nameInvite.append("Jerome")

print(nameInvite[0] + " You are invited to a dinner!")
print(nameInvite[1] + " You are invited to a dinner!")
print(nameInvite[2] + " You are invited to a dinner!")
print(nameInvite[3] + " You are invited to a dinner!")
print(nameInvite[4] + " You are invited to a dinner!")
print(nameInvite[5] + " You are invited to a dinner!")

# Ex. 3-7
print("I can only invite 2 people per table.")
popped_name = nameInvite.pop()
print("Sorry, " + popped_name)

popped_name = nameInvite.pop()
print("Sorry, " + popped_name)

popped_name = nameInvite.pop()
print("Sorry, " + popped_name)

popped_name = nameInvite.pop()
print("Sorry, " + popped_name)

print(nameInvite[0] + " You are invited to a dinner!")
print(nameInvite[1] + " You are invited to a dinner!")

del nameInvite[1]
del nameInvite[0]
print(nameInvite)

philosophers = ["Plato", "Socrates", "Kant", "Heidegger",
                "Hume", "Des Cartes", "Sartre", "Nietzsche"]

eastern = ["Lao Tzu", "Confucius"]

philosophers.append("Rawls")  # append list

philosophers.insert(2, "Aristotle")  # insert at position

print(philosophers)  # print list

print("Categorical Imperative: " + philosophers[2])  # concat and index

print("Platonism: " + philosophers[0])  # concat and index

print("Is Ought Problem: " + philosophers[4])  # concat and index

print(philosophers[2:])  # print all from position 2

print(philosophers.index("Socrates"))  # index of

philosophers.sort() # sort list
print(philosophers)

philosophers.reverse() # reverse list
print(philosophers)

philosophers.extend(eastern) #extend list with another list
print(philosophers)

philosophers2 = philosophers.copy() #copy list
print(philosophers2)

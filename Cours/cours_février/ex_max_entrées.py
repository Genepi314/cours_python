#  Trouvé sur google:
max_entries = 5
user_entries = []
count = 0

while count < max_entries:
    entry = input("Enter a value: ")
    user_entries.append(entry)
    count += 1

print("User entries:", user_entries)
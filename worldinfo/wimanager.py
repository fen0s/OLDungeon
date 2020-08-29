import json
path = input("Any world info file you'd want to edit inside the folder? Leave empty if not. ")
if path:
    with open(f"./{path}.json") as worldinfo:
        worldinfo = list(json.load(worldinfo))
else:
    worldinfo = []
while True:
    print("Currently in WI:\n")
    for enum, entry in enumerate(worldinfo):
        for value in entry.values():
            if type(value) == list:
                print(f"KEYWORDS: {value}")
            else:
                print(f"ENTRY #{enum}: {value}")
        print("\n")
    choice = input("1) Add entry\n2) Edit entry\n3) Delete entry\n4) Save worldinfo\n")
    if choice == "1":
        new_entry = input("Enter what should be added to context? ")
        keywords = input("What keywords should trigger this entry? Separate with commas! ").split(", ")
        worldinfo.append({"context": new_entry,
                          "keywords": keywords})
        continue
    elif choice =="2":
        to_edit = int(input("Enter number of entry to edit: "))
        new_entry = input("Enter what should be added to context? ")
        keywords = input("What keywords should trigger this entry? Separate with commas!" ).split(", ")
        try:
            worldinfo[to_edit] = {"context": new_entry,
                          "keywords": keywords}
        except IndexError:
            print("\nENTRY NUMBER DOESN'T EXIST")
            input()
        continue

    elif choice == "3":
        to_delete = int(input("Enter number of entry to delete: "))
        try:
            del(worldinfo[to_delete])
        except IndexError:
            print("\nENTRY NUMBER DOESN'T EXIST")
            input()
        continue
    elif choice =="4":
        to_save = input("file of name to save to: ")
        with open(f"./{to_save}.json", "w") as json_file:
            json.dump(worldinfo, json_file)
        break

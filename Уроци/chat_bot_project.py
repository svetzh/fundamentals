from collections import Counter

issue = input("Please specify your issue by choosing - 1-hardware or 2-software or EXIT to quit: ").lower()
name = input("What is your name: ")
is_salable = False

changeable = []
salable = []
count_salable = 0
count_changeable = 0
while issue != "EXIT".lower():
    is_salable = False
    if issue == "1" or issue == "2":
        if issue == "1":
            print("You chose HARDWARE. "
                  "Please specify if it's related to:"
                  " 1-MotherBoard;"
                  " 2-RAM;"
                  " 3-SSD;"
                  " 4-CPU;"
                  " 5-VideoCard")
            hardware_issue_choice = input(f"Your choice of hardware {name}: ")
            if hardware_issue_choice == "1":
                replaceable = input("Choose 1-BUY or 2-CHANGE: ")
                module = "MotherBoard"
                if replaceable == "1":
                    is_salable = True
                    if is_salable:
                        salable.append(module)
                        count_salable += 1
                        print(f"You need to buy new laptop since {module} can't be replaced.")
                else:
                    print(f"You can change the {module}")
                    changeable.append(module)
                    count_changeable += 1

            elif hardware_issue_choice == "2":
                module = "RAM"
                print(f"You can replace {module} and check the laptop model how much memory can be added.")
                changeable.append(module)
                count_changeable += 1

            elif hardware_issue_choice == "3":
                module = "SSD"
                salable.append(module)
                count_salable += 1
                print(f"You need to buy new laptop since {module} couldn't be repaired.")

            elif hardware_issue_choice == "4":
                module = "CPU"
                salable.append(module)
                count_salable += 1
                print(f"You have to buy new laptop because {module} isn't replaceable.")

            elif hardware_issue_choice == "5":
                replaceable = input("Choose 1-BUY or 2-CHANGE: ")
                module = "VideoCard"
                if replaceable == "1":
                    is_salable = True
                    if is_salable:
                        salable.append(module)
                        count_salable += 1
                        print(f"You need to buy new laptop since {module} can't be replaced. Soldered onto motherboard")
                else:
                    print(f"You can replace {module} and check if the {module} is compatible with the laptop")
                    changeable.append(module)
                    count_changeable += 1

        elif issue == "2":
            print("You chose SOFTWARE. "
                  "Please specify if it's related to:"
                  " 1-Corrupt Drivers;"
                  " 2-Malware Attack;"
                  " 3-Windows Displaying Blue Screen;"
                  " 4-Outdated system")
            software_issue_choice = input(f"Your choice of software {name}: ")
            if software_issue_choice == "1":
                module = "Drivers"
                count_salable += 1
                print(f"Need to buy and install new {module}")
                changeable.append(module)
            elif software_issue_choice == "2":
                module = "Malware"
                count_salable += 1
                print(f"Buy new AV program {module}")
                changeable.append(module)
            elif software_issue_choice == "3":
                module = "BlueScreen"
                count_salable += 1
                print(f"{module} is the new weapon of uncle Billy")
            elif software_issue_choice == "4":
                module = "UpdateNeeded"
                count_salable += 1
                print(f"{module} and lot's of restarts.")
                changeable.append(module)
    else:
        print("Please enter either 1 or 2")

    issue = input("Please specify your issue by choosing - 1-hardware or 2-software or EXIT to quit: ").lower()

if not issue == "EXIT".lower():
    print(f"Good bye, {name}")

else:
    print(f"Purchasable items: {count_salable}")
    print(f"Changeable items: {count_changeable}")
    overall_items = count_salable + count_changeable
    print(f"Total items: {overall_items}")
    salable.extend(changeable)
    print(" ".join(salable))

    count_list = Counter(salable)
    for word, count in count_list.items():
        if count == 1:
            print(word)
        else:
            print(f"{word} appeared: {count} times")
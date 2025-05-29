import os
from datetime import datetime

class FileHandle:

    def add_new_entry(self):
        print("Enter Your Journal Entry")
        entry = input("")  # Taking the entry from the user
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("journal.txt", "a") as file:
            file.write(f"[{timestamp}]\n{entry}\n\n")
        print("Entry Added Successfully!")    

    def view_all_entry(self):
        if os.path.exists("journal.txt"):
            with open("journal.txt", "r") as file:
                content = file.read()
                print("Your Journal Entry")
                print("----------------------------------------------------")
                if content.strip() == "":
                    print("No entries yet. Start by adding a new journal entry!")
                else:
                    print(content)
        else:
            print("No Journal Entry Found. Start by adding a new entry.")

    def search_entries(self):
        if not os.path.exists("journal.txt"):
            print("No journal file found to search.\n")
            return

        keyword = input("Enter keyword or date to search: ").lower()
        with open("journal.txt", "r") as file:
            content = file.read()
            entries = content.split("\n\n")

            found = False
            print("\nMatching Entries:\n")
            print("*" * 30)
            for entry in entries:
                if keyword in entry.lower():
                    print(entry)
                    found = True

            if not found:
                print("No matching entries found.\n")

    def delete_all_entry(self):
        if not os.path.exists("journal.txt"):
            print("No journal entry to delete.")
            return

        userinput = input("Are you sure you want to delete all entries? (yes/no): ").strip().lower()
        if userinput == "yes":
            open("journal.txt", "w").close()
            print("All journal entries have been deleted.")
        else:
            print("Deletion cancelled.")


# Create an instance of FileHandle
journal = FileHandle()

print("Welcome to Personal Journal Manager!")

while True:
    print("--------------------------------------------------")
    print("Select an option:")
    print("1. Add a New Entry")
    print("2. View all Entries")
    print("3. Search for an Entry")
    print("4. Delete all Entries")
    print("5. Exit")
    print("--------------------------------------------------")

    choice = input("User Input: ").strip()

    match choice:
        case "1":
            journal.add_new_entry()
        case "2":
            journal.view_all_entry()
        case "3":
            journal.search_entries()
        case "4":
            journal.delete_all_entry()
        case "5":
            print("Thank you for using Journal Manager. Goodbye!")
            break
        case _:
            print("Invalid choice. Please enter a valid choice.")

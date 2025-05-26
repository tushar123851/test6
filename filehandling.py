from datetime import datetime  # Add this at the top of your script



def add_new_entry():
    print("Enter Your Journal Entry")
    entry = input("")#taking the entry from the user
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format: 2025-05-22 14:30:45
    with open("journal.txt","a") as file:#append mode for taking the previos entry
        file.write(f"[{timestamp}]\n{entry}\n\n")#Each entry in new line
    print("Entry Added Successfully!")    

def view_all_entry():
    try:
        with open("journal.txt", "r") as file:#opening the file in read mode
            content = file.read()
            print("Your Journal Entry")
            print("----------------------------------------------------")
            if content.strip() == "":#if file is empty or blank
                print("No entries yet. Start by adding a new journal entry!")
            else:#if file is exit print the content of the file
                print(content)

    except FileNotFoundError:#if file does not exist
        print("No Journal Entry Found. Start by adding a new entry.")


def search_entries():
    keyword = input("Enter keyword or date to search: ").lower()
    try:
        with open("journal.txt", "r") as file:
            content = file.read()
            entries = content.split("\n\n")  # Each entry is separated by double newlines

            found = False
            print("\n Matching Entries:\n")
            print("*"*30)
            for entry in entries:
                if keyword in entry.lower():
                    print(entry)
                    found = True

            if not found:
                print("No matching entries found.\n")

    except FileNotFoundError:
        print("No journal file found to search.\n")

def delete_all_entry():
    try:
        #take user input from user for delete or not
        userinput = input("Are you sure you want to delete all entries? (yes/no):").strip().lower()
        if userinput =="yes":#if user press:yes
             open("journal.txt","w").close()#delete all files
             print("All journal entries have been deleted")
        else:#if user press:no
              print("Deletion cancelled")
    except FileNotFoundError:#if file does not exist
        print("No journal entry to delete")           
       

     
print("Welcome to personal journal manager!")

while True:

    print("--------------------------------------------------")
    print("Select an option:")
    print("1.Add a New Entry")
    print("2.View all Entries")
    print("3.Search for an Entry")
    print("4.Delete all Entries")
    print("5.Exit")
    print("--------------------------------------------------")

    choice = str(input("User Input:"))

    match choice:
        case "1":
            add_new_entry()
            
        case "2":
            view_all_entry()
           
        case "3":
            search_entries()
        case "4":
            delete_all_entry()        
        case "5":
            print("Thank you for using journal manager.Goodbye!")
        case _:
            print("Invalid choice.plaese enter valid choice.")

        
      

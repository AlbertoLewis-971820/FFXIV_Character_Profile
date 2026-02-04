#Run application
from character import Character
from Job import Job, JobType
def main():
    print("Welcome to the FFXIV Character Profile App!")
    # Here you can add code to create Character and Job instances
    # and display their information.
    
    while True:
        print("\nWelcome to the FFXIV Character Profile App!")
        print("1. Create a new character profile")
        print("2. Add a new job to a character")
        print("3. View existing character profiles")
        print("4. Exit")
        choice = input("Please enter your choice (1-4): ")

        if choice =='1':
            name = input("Enter character name: ")
            server = input("Enter character server: ")
            race = input("Enter character race: ")
            character = Character(name, server, race)
            character.add_profile()
        elif choice =='2':
            name = input("Enter job name: ")
            job_type = input("Enter job type: ")
            level = input("Enter job level: ")
            job = JobType(name, level, job_type)
            print("Job added:")
            pass
        elif choice =='3':
            # Load and display existing character profiles
            characters = Character.load_characters()
            if characters:
                print("Existing Character Profiles:")
                for char in characters:
                    print(f"Name: {char['name']}, Server: {char['server']}, Race: {char['race']}")
            else:
                print("No character profiles found.")

        elif choice =='4':
            print("Exiting the application. Goodbye!")
            break



            

if __name__ == "__main__":
    main()

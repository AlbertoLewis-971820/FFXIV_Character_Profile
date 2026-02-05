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
        print("4. Delete a character profile")
        print("5. Exit")
        choice = input("Please enter your choice (1-5): ")

        if choice =='1':
            name = input("Enter character name: ")
            server = input("Enter character server: ")
            race = input("Enter character race: ")
            character = Character(name, server, race)
            character.add_profile()
        elif choice =='2':
            #Ask user what profile to add job to
            character_name = input("Enter the name of the character to add a job to: ").strip("")
            job_name = input("Enter job name: ")
            level = input("Enter job level: ")
            job_type = input("Enter job type (Crafter, Gatherer, Combat): ")
            job = JobType(job_name, level, job_type)
            job.add_job_type(job_type, level, character_name, job_name)
        elif choice =='3':
            # Load and display existing character profiles
            characters = Character.load_characters()
            characters_jobs = JobType.load_jobs()
            if characters:
                print("Existing Character Profiles:")
                for char in characters:
                    print(f"Name: {char['name']}, Server: {char['server']}, Race: {char['race']}")
                    if 'jobs' in char and char['jobs']:
                        print("  Jobs:")
                        for job in char['jobs']:
                            print(f"    Job Name: {job['job_name']}, Level: {job['level']}, Type: {job['job_type']}")
            else:
                print("No character profiles found.")

        elif choice =='4':
            character_name = input("Enter the name of the character to delete: ").strip("")
            Character.delete_character(character_name)
    

        elif choice =='5':
            print("Exiting the application. Goodbye!")
            break



            

if __name__ == "__main__":
    main()

#Create a job class for FFXIV characters and their types of jobs
import json
import os

class Job:
    def __init__(self, job_name, level):
        self.job_name = job_name
        self.level = level

    def display_job_info(self):
        return f"Job: {self.job_name}, Level: {self.level}"
    

class JobType(Job):
    def __init__(self, job_name, level, job_type):
        # Initialize the parent Job class
        super().__init__(job_name, level)
        # Add the job_type attribute 
        self.job_type = job_type


    def add_job_type(self, job_type, level,character_name, job_name, filename="data/character_profile.json"):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        self.job_type = job_type
        self.level = level
        self.job_name = job_name
        self.character_name = character_name
        

        if job_type not in ["Crafter", "Gatherer", "Combat"]:
            print("Invalid job type. Please choose from 'Crafter', 'Gatherer', or 'Combat'.")
            return
        
        try:
            with(open(filename, 'r') as file):
                characters = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Character profile not found. Please create a character profile first.")
            return

        for character in characters:
            if character.get("name", "").lower() == character_name.lower():
                # Add job to the character's job list
                character.setdefault("jobs", [])
                character["jobs"].append({
                    "job_name": self.job_name,
                    "level": self.level,
                    "job_type": self.job_type
                })
                with open(filename, 'w') as file:
                    json.dump(characters, file, indent=4)
                print(f"Job added to '{character_name}' successfully.")
                return

        print(f"Character '{character_name}' not found.")


    @staticmethod
    def load_jobs(filename="data/character_profile.json"):
        try:
            with open(filename, 'r') as file:
                characters = json.load(file)    
        except FileNotFoundError:
            print("No existing character profiles found.")
            
    
    
    



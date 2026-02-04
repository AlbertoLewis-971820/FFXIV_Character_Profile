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
    def __init__(self, job_name, level, job_type=""):
        # Initialize the parent Job class
        super().__init__(job_name, level)
        # Add the job_type attribute 
        self.job_type = job_type


    def add_job_type(self, job_type, level, filename="data/character_jobs.json"):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        self.job_type = job_type
        self.level = level

        try:
            with open(filename, 'r') as file:
                jobs = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file does not exist yet or is corrupted, create an empty list
            jobs = []
            #Append the new job type to the list of the selected character profile
        jobs.append({
            "job_name": self.job_name,
            "level": self.level,
            "job_type": self.job_type
        })
        with open(filename, 'w') as file:
            json.dump(jobs, file, indent=4)
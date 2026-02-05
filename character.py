#class for FFXIV character
import json
import os
class Character:
    
    def __init__(self, name, server, race, jobs=None):
        self.name = name
        self.server = server
        self.race = race
        self.jobs = jobs if jobs is not None else []
    #Add character to json file
    def add_profile(self, filename="data/character_profile.json"):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        try:
            with open(filename, 'r') as file:
                characters = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file does not exist yet or is corrupted, create an empty list
            characters = []
        characters.append({
            "name": self.name,
            "server": self.server,
            "race": self.race,
            "jobs": self.jobs,
        })
        with open(filename, 'w') as file:
            json.dump(characters,file, indent=4)

        print("Character profile saved successfully.")
        
        
    #Load existing characters from the JSON file
    @staticmethod
    def load_characters(filename="data/character_profile.json"):
        try:
            with open(filename, 'r') as file:
                characters = json.load(file)
            return characters
        except FileNotFoundError:
            print("No existing character profiles found.")
            return []
        
    @staticmethod
    def delete_character(character_name, filename="data/character_profile.json"):
        try:
            with open(filename, 'r') as file:
                characters = json.load(file)
        except FileNotFoundError:
            print("No existing character profiles found.")
            return
        
        for character in characters:
            if character.get("name", "").lower() == character_name.lower():
                characters.remove(character)
                with open(filename, 'w') as file:
                    json.dump(characters, file, indent=4)
                print(f"Character '{character_name}' deleted successfully.")
                return
        print(f"Character '{character_name}' not found.")
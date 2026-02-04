#class for FFXIV character
import json
import os
class Character:
    
    def __init__(self, name, server, race):
        self.name = name
        self.server = server
        self.race = race

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
            "race": self.race
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
        except FileNotFoundError:
            print("No existing character profiles found.")
            characters = []
        return characters
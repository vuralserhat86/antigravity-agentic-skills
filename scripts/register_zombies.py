import json
import os

MANIFEST_FILE = os.path.expanduser("~/.skillport/skills_manifest.json")
SKILLS_DIR = os.path.expanduser("~/.skillport/skills")

def load_manifest():
    with open(MANIFEST_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_manifest(data):
    with open(MANIFEST_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_registered_skills(data):
    skills = set()
    for kit in data.get('kits', {}).values():
        for skill in kit.get('core_skills', []):
            skills.add(skill)
    return skills

def main():
    data = load_manifest()
    registered = get_registered_skills(data)
    
    fs_skills = set()
    if os.path.exists(SKILLS_DIR):
        for name in os.listdir(SKILLS_DIR):
            if os.path.isdir(os.path.join(SKILLS_DIR, name)):
                fs_skills.add(name)

    zombies = list(fs_skills - registered)
    # Filter out 'core' which we want to delete
    if 'core' in zombies:
        zombies.remove('core')
    
    zombies.sort()
    
    print(f"Found {len(zombies)} zombie skills.")

    if not zombies:
        print("No zombies to register.")
        return

    # Add to UniversalKit
    if "UniversalKit" not in data['kits']:
        data['kits']['UniversalKit'] = {
            "description": "Expanded library of all available specialized skills.",
            "auto_triggers": ["*"], 
            "core_skills": []
        }
    
    # Merge existing universal skills if any
    current_universal = set(data['kits']['UniversalKit']['core_skills'])
    current_universal.update(zombies)
    
    data['kits']['UniversalKit']['core_skills'] = sorted(list(current_universal))
    data['total_skills'] = len(fs_skills) # Update total count

    save_manifest(data)
    print(f"Registered {len(zombies)} skills into UniversalKit.")
    print("Updated total_skills count.")

if __name__ == "__main__":
    main()

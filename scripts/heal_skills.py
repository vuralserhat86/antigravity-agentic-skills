import os
import json
import re

MANIFEST_FILE = os.path.expanduser("~/.skillport/skills_manifest.json")
SKILLS_DIR = os.path.expanduser("~/.skillport/skills")

def load_manifest():
    with open(MANIFEST_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_triggers_from_manifest(manifest, skill_id):
    # Find which kit contains the skill
    for kit_name, kit_data in manifest.get('kits', {}).items():
        if skill_id in kit_data.get('core_skills', []):
            # Using Kit triggers as a baseline fallback
            return kit_data.get('auto_triggers', [])
    return []

def heal_skill(skill_path, skill_name, triggers):
    skill_file = os.path.join(skill_path, "SKILL.md")
    if not os.path.exists(skill_file):
        print(f"Skipping {skill_name}: File not found")
        return False

    with open(skill_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Detect Frontmatter
    match = re.search(r'^---\s+(.*?)\s+---', content, re.DOTALL)
    if not match:
        print(f"Skipping {skill_name}: No frontmatter found")
        return False
    
    frontmatter = match.group(1)
    
    # Check if we need to add metadata/tags
    # Strategy: Replace the entire frontmatter with a reconstructed one OR inject
    # Injection is safer to preserve other fields
    
    new_frontmatter = frontmatter
    
    # Construct the tags block
    tags_yaml = "\nmetadata:\n  skillport:\n    category: auto-healed\n    tags:\n"
    for tag in triggers:
        tags_yaml += f"      - {tag}\n"
        
    # Add skill name itself as a tag
    tags_yaml += f"      - {skill_name}\n"

    # If metadata exists, we might need a more complex merge, 
    # but for "broken" skills, usually metadata is totally missing.
    if "metadata:" not in frontmatter:
        new_frontmatter += tags_yaml
    else:
        # Simple heuristic: If tags are missing, append them to the metadata block
        if "tags:" not in frontmatter:
             new_frontmatter = new_frontmatter.replace("metadata:", f"{tags_yaml}")
    
    # Reassemble file
    new_content = content.replace(frontmatter, new_frontmatter)
    
    with open(skill_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"✅ Healed {skill_name}")
    return True

def main():
    manifest = load_manifest()
    print("Loaded Manifest. Starting Mass Healing...")
    
    count = 0
    for skill_name in os.listdir(SKILLS_DIR):
        skill_path = os.path.join(SKILLS_DIR, skill_name)
        if os.path.isdir(skill_path):
            triggers = get_triggers_from_manifest(manifest, skill_name)
            if triggers:
                # Add generic synonyms for better finding
                triggers.extend([skill_name.replace('_', ' '), "expert", "guide"])
                if heal_skill(skill_path, skill_name, triggers):
                    count += 1
            else:
                # Even if no kit triggers, at least add self-name as tag
                heal_skill(skill_path, skill_name, [skill_name])
                count += 1

    print(f"Mass Healing Complete. Processed {count} files.")

if __name__ == "__main__":
    main()

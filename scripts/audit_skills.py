import os
import re
import json

SKILLS_DIR = os.path.expanduser("~/.skillport/skills")
# Use a local report file to avoid path issues
REPORT_FILE = "C:/Users/mSv/.gemini/antigravity/brain/b1718088-806e-466d-becc-c57425f15bc7/SKILL_HEALTH_REPORT.md"
MANIFEST_FILE = os.path.expanduser("~/.skillport/skills_manifest.json")

def load_manifest_skills():
    try:
        with open(MANIFEST_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            skills = set()
            for kit_name, kit_data in data.get('kits', {}).items():
                for skill in kit_data.get('core_skills', []):
                    skills.add(skill)
            return skills
    except Exception as e:
        print(f"Manifest Error: {e}")
        return set()

def parse_frontmatter(content):
    match = re.search(r'^---\s+(.*?)\s+---', content, re.DOTALL)
    if not match:
        return None
    return match.group(1)

def audit_skill(skill_path, skill_name, manifest_skills):
    is_registered = skill_name in manifest_skills
    
    skill_file = os.path.join(skill_path, "SKILL.md")
    if not os.path.exists(skill_file):
        return {"status": "MISSING_FILE", "name": skill_name, "registered": is_registered}

    try:
        with open(skill_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {"status": "READ_ERROR", "name": skill_name, "error": str(e), "registered": is_registered}

    frontmatter = parse_frontmatter(content)
    if not frontmatter:
        return {"status": "INVALID_FORMAT", "name": skill_name, "registered": is_registered}

    # Simple text parsing for speed (yaml lib might not be available)
    has_tags = "tags:" in frontmatter
    description_match = re.search(r'description:\s*(.+)', frontmatter)
    
    desc_length = 0
    if description_match:
        desc_length = len(description_match.group(1).split())

    issues = []
    if not has_tags:
        issues.append("MISSING_TAGS")
    if desc_length < 3: # Relaxed slightly
        issues.append(f"WEAK_DESCRIPTION (Words: {desc_length})")
    
    if not is_registered:
        issues.append("ZOMBIE (Not in Manifest)")

    if issues:
        return {"status": "WEAK", "name": skill_name, "issues": issues, "registered": is_registered}
    
    return {"status": "HEALTHY", "name": skill_name, "registered": is_registered}

def main():
    print("Starting Deep Audit...")
    results = []
    manifest_skills = load_manifest_skills()
    print(f"Manifest expects {len(manifest_skills)} unique skills.")
    
    if not os.path.exists(SKILLS_DIR):
        print(f"Error: Skills dir not found at {SKILLS_DIR}")
        return

    fs_skills = set()
    for skill_name in os.listdir(SKILLS_DIR):
        skill_path = os.path.join(SKILLS_DIR, skill_name)
        if os.path.isdir(skill_path):
            fs_skills.add(skill_name)
            result = audit_skill(skill_path, skill_name, manifest_skills)
            if result:
                results.append(result)

    # Check for GHOSTS (In manifest, not on disk)
    ghosts = manifest_skills - fs_skills
    for ghost in ghosts:
        results.append({"status": "GHOST", "name": ghost, "issues": ["In Manifest but not on Disk"]})

    # Generate Report
    weak_skills = [r for r in results if r['status'] != 'HEALTHY']
    healthy_skills = [r for r in results if r['status'] == 'HEALTHY']

    report_content = f"""# Skill Health Report
**Total Skills Scanned:** {len(results)}
**Healthy Skills:** {len(healthy_skills)}
**Weak/Broken/Zombie/Ghost Skills:** {len(weak_skills)}

---

## 🚨 Critical Issues (Action Required)

"""
    if not weak_skills:
        report_content += "No critical issues found! System is 100% healthy.\n"
    else:
        for skill in weak_skills:
            report_content += f"- **{skill['name']}**: {', '.join(skill.get('issues', [skill['status']]))}\n"

    print(report_content)
    
    # Save to file
    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(report_content)
    print(f"Report saved to {REPORT_FILE}")

if __name__ == "__main__":
    main()

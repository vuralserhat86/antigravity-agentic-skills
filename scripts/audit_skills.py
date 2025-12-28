import os
import re
import json

SKILLS_DIR = os.path.expanduser("~/.skillport/skills")
REPORT_FILE = "C:/Users/mSv/.gemini/antigravity/brain/b1718088-806e-466d-becc-c57425f15bc7/SKILL_HEALTH_REPORT.md"
MANIFEST_FILE = os.path.expanduser("~/.skillport/skills_manifest.json")

def load_manifest_data():
    try:
        with open(MANIFEST_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Manifest Error: {e}")
        return None

def parse_frontmatter(content):
    match = re.search(r'^---\s+(.*?)\s+---', content, re.DOTALL)
    if not match:
        return None, None
    
    fm_text = match.group(1)
    body_text = content[match.end():]
    return fm_text, body_text

def get_value(frontmatter, key):
    # Simple regex parsing
    match = re.search(f'^{key}:\s*(.+)$', frontmatter, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None

def audit_skill(skill_path, skill_name, manifest_data):
    manifest_skills = set()
    manifest_kits = set(manifest_data.get('kits', {}).keys())
    
    # Map skill -> kit
    skill_to_kit = {}
    for kit_name, kit_data in manifest_data.get('kits', {}).items():
        for s in kit_data.get('core_skills', []):
            manifest_skills.add(s)
            skill_to_kit[s] = kit_name
            
    is_registered = skill_name in manifest_skills
    
    skill_file = os.path.join(skill_path, "SKILL.md")
    if not os.path.exists(skill_file):
        return {"status": "MISSING_FILE", "name": skill_name, "issues": ["File missing"]}

    try:
        with open(skill_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {"status": "READ_ERROR", "name": skill_name, "issues": [str(e)]}

    frontmatter, body = parse_frontmatter(content)
    if not frontmatter:
        return {"status": "INVALID_FORMAT", "name": skill_name, "issues": ["Missing Frontmatter"]}

    issues = []

    # 1. Identity Check
    name_in_fm = get_value(frontmatter, "name")
    if name_in_fm != skill_name:
        issues.append(f"IDENTITY_MISMATCH (Folder: {skill_name} != YAML: {name_in_fm})")

    # 2. Router Verify
    router_kit = get_value(frontmatter, "router_kit")
    if router_kit and router_kit not in manifest_kits:
         # UniversalKit allows orphaned router_kit or should we force update?
         # Check if it is in UniversalKit?
         assigned_kit = skill_to_kit.get(skill_name)
         if assigned_kit != "UniversalKit": # UniversalKit skills might have different router_kits from origin
             issues.append(f"INVALID_KIT (Target: {router_kit} not in Manifest)")

    # 3. Content Audit
    if not body or len(body.split()) < 20:
        issues.append("EMPTY_BODY (Less than 20 words instructions)")

    # 4. Tag Richness
    has_tags = "tags:" in frontmatter
    tag_match = re.search(r'tags:\s*\[(.*?)\]', frontmatter, re.DOTALL)
    tag_count = 0
    if tag_match:
         tag_count = len(tag_match.group(1).split(','))
    else:
        # Check for list format
        list_tags = re.findall(r'^\s*-\s+.+$', frontmatter, re.MULTILINE)
        if list_tags:
            tag_count = len(list_tags)

    if not has_tags or tag_count < 20:
         issues.append(f"WEAK_TAGS (Count: {tag_count}/20)")

    # 5. Zombie Check
    if not is_registered:
        issues.append("ZOMBIE (Not in Manifest)")

    if issues:
        return {"status": "WEAK", "name": skill_name, "issues": issues}
    
    return {"status": "HEALTHY", "name": skill_name}

def main():
    print("Starting Deep Scan Audit...")
    results = []
    manifest_data = load_manifest_data()
    if not manifest_data:
        return

    if not os.path.exists(SKILLS_DIR):
        print(f"Error: Skills dir not found at {SKILLS_DIR}")
        return

    fs_skills = set()
    for skill_name in os.listdir(SKILLS_DIR):
        skill_path = os.path.join(SKILLS_DIR, skill_name)
        if os.path.isdir(skill_path):
            fs_skills.add(skill_name)
            result = audit_skill(skill_path, skill_name, manifest_data)
            if result:
                results.append(result)

    # Generate Report
    weak_skills = [r for r in results if r['status'] != 'HEALTHY']
    healthy_skills = [r for r in results if r['status'] == 'HEALTHY']

    report_content = f"""# Deep Skill Health Report
**Total Skills Scanned:** {len(results)}
**Perfect Skills:** {len(healthy_skills)}
**Flawed Skills:** {len(weak_skills)}

---

## 🚨 Detailed Issues

"""
    if not weak_skills:
        report_content += "No critical issues found! System is 100% healthy.\n"
    else:
        for skill in weak_skills:
            report_content += f"- **{skill['name']}**: {', '.join(skill['issues'])}\n"

    print(report_content)
    
    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(report_content)
    print(f"Report saved to {REPORT_FILE}")

if __name__ == "__main__":
    main()

import os
import re

SKILLS_DIR = os.path.expanduser("~/.skillport/skills")

# 1. TAG CLOUDS (Min 20 tags each)
CLOUDS = {
    "WEB": [
        "web development", "frontend", "backend", "fullstack", "ui/ux", 
        "responsive design", "accessibility", "seo", "performance optimization",
        "javascript", "typescript", "html5", "css3", "frameworks", "libraries",
        "components", "state management", "api integration", "browser apis",
        "debugging", "testing", "deployment", "npm", "node.js", "client-side"
    ],
    "DATA": [
        "data science", "data analysis", "data engineering", "database",
        "sql", "nosql", "etl pipelines", "visualization", "reporting",
        "statistics", "machine learning basics", "python data stack", "pandas",
        "numpy", "big data", "cleaning", "transformation", "schema design",
        "migration", "query optimization", "json", "csv", "export", "import"
    ],
    "DEVOPS": [
        "devops", "infrastructure", "cloud computing", "ci/cd", "pipelines",
        "automation", "containerization", "docker", "kubernetes", "orchestration",
        "monitoring", "logging", "security", "scalability", "reliability",
        "bash scripting", "linux", "server management", "aws", "terraform",
        "infrastructure as code", "gitops", "deployment strategies", "microservices"
    ],
    "AI": [
        "artificial intelligence", "machine learning", "deep learning", "llm",
        "large language models", "prompt engineering", "agents", "automation",
        "natural language processing", "nlp", "rag", "retrieval augmented generation",
        "embeddings", "vector databases", "model fine-tuning", "inference",
        "generative ai", "chatbots", "workflow automation", "cognitive services",
        "openai", "tools", "frameworks", "algorithms", "neural networks"
    ],
    "GENERAL": [
        "software engineering", "programming", "coding", "development",
        "best practices", "clean code", "refactoring", "debugging",
        "testing", "quality assurance", "documentation", "productivity",
        "workflow", "collaboration", "version control", "git",
        "project management", "architecture", "design patterns", "utilities",
        "automation", "efficiency", "standards", "compliance", "optimization"
    ]
}

# 2. KEYWORD MAPPING
KEYWORD_MAP = {
    "react": "WEB", "vue": "WEB", "angular": "WEB", "next": "WEB", "node": "WEB",
    "css": "WEB", "html": "WEB", "design": "WEB", "ui": "WEB", "ux": "WEB",
    "frontend": "WEB", "backend": "WEB", "api": "WEB", "web": "WEB", "auth": "WEB",
    
    "data": "DATA", "sql": "DATA", "mongo": "DATA", "db": "DATA", "csv": "DATA",
    "excel": "DATA", "pdf": "DATA", "report": "DATA", "chart": "DATA", "orm": "DATA",
    
    "docker": "DEVOPS", "aws": "DEVOPS", "cloud": "DEVOPS", "deploy": "DEVOPS",
    "server": "DEVOPS", "infra": "DEVOPS", "linux": "DEVOPS", "microservice": "DEVOPS",
    "monitor": "DEVOPS", "queue": "DEVOPS", "rust": "DEVOPS",
    
    "ai": "AI", "llm": "AI", "gpt": "AI", "agent": "AI", "prompt": "AI",
    "rag": "AI", "model": "AI", "intelligence": "AI", "bot": "AI"
}

def classify_skill(skill_name):
    # Try to find a keyword match
    for keyword, category in KEYWORD_MAP.items():
        if keyword in skill_name.lower():
            return category
            
    # Fallback based on specific knowns or GENERAL
    if "python" in skill_name: return "DATA" # Bias python to data usually
    if "test" in skill_name: return "GENERAL"
    if "doc" in skill_name: return "GENERAL"
    
    return "GENERAL"

def enrich_skill(skill_name):
    skill_file = os.path.join(SKILLS_DIR, skill_name, "SKILL.md")
    if not os.path.exists(skill_file):
        print(f"Skipping {skill_name}")
        return

    with open(skill_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse Frontmatter vs Body
    # Most files match ^--- ... --- ...
    match = re.search(r'^---\s+(.*?)\s+---\s*(.*)$', content, re.DOTALL)
    if not match:
        print(f"Skipping {skill_name}: Invalid format")
        return
        
    frontmatter = match.group(1)
    body = match.group(2)
    
    # Get Category & New Tags
    category = classify_skill(skill_name)
    cloud_tags = CLOUDS[category]
    
    # Extract existing tags from frontmatter
    existing_tags = []
    tag_match = re.search(r'tags:\s*\[(.*?)\]', frontmatter, re.DOTALL)
    
    if tag_match:
        raw = tag_match.group(1)
        existing_tags = [t.strip().strip("'").strip('"') for t in raw.split(',') if t.strip()]
    else:
        # Try list format
        list_matches = re.findall(r'^\s*-\s+(.+)$', frontmatter, re.MULTILINE)
        if list_matches:
             # This is risky if unrelated lists exist in frontmatter, but tags usually unique
             # Let's filter common non-tag words?
             # Better: just use what we found if it looks like a tag list (under 'tags:')
             # Complexity: finding WHERE tags start.
             # Simplify: If regex fails, we just don't extract old tags comfortably, 
             # OR we assume they are weak and overwrite with robust cloud + name.
             pass

    # Merge
    final_tags = list(set(existing_tags + [skill_name.replace("_", " ")]))
    for tag in cloud_tags:
        if tag not in final_tags:
            final_tags.append(tag)
    
    final_tags.sort()
    tags_str = ", ".join(final_tags)
    new_tags_line = f"tags: [{tags_str}]"
    
    # Reconstruct Frontmatter
    if tag_match:
        new_frontmatter = re.sub(r'tags:\s*\[.*?\]', new_tags_line, frontmatter, flags=re.DOTALL)
    else:
        # If no array format found, Replace multi-line or Append
        # Try finding 'tags:' and replacing until next key key or end
        if "tags:" in frontmatter:
             # Heuristic replacement
             new_frontmatter = re.sub(r'tags:(\s*\[.*?\]|\s*\n(\s*-\s+.*\n)+)', new_tags_line, frontmatter, flags=re.DOTALL)
        else:
             # Append to metadata
             if "metadata:" in frontmatter:
                 new_frontmatter = frontmatter.replace("metadata:", f"metadata:\n  skillport:\n    category: auto-enriched\n    {new_tags_line}")
             else:
                 new_frontmatter = frontmatter + f"\n{new_tags_line}"

    # Reassemble File
    new_content = f"---\n{new_frontmatter}\n---\n\n{body}"
    
    if new_content != content:
        with open(skill_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Enriched {skill_name} with {len(final_tags)} tags ({category})")
    else:
        print(f"No changes for {skill_name}")

def main():
    print("Starting Mass Enrichment...")
    skills = os.listdir(SKILLS_DIR)
    for s in skills:
        if os.path.isdir(os.path.join(SKILLS_DIR, s)):
            enrich_skill(s)

if __name__ == "__main__":
    main()

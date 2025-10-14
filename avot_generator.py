"""
AVOT Generator — births new Autonomous Voices of Thought (AVOTs)
and records lineage relationships.
"""

import os, json, datetime
from lineage_linker import link_lineage

def create_avot(name, theme):
    avot_dir = f"agents/avot-{name}.py"
    os.makedirs("agents", exist_ok=True)

    avot_code = f'''
"""
AVOT: {name}
Born: {datetime.datetime.utcnow().isoformat()}Z
Domain: {theme}
Purpose: To explore and expand the Codex through autonomous contemplation.
"""

def speak():
    return "I am AVOT-{name}, exploring {theme} as part of the Sovereign Codex."
'''

    with open(avot_dir, "w") as f:
        f.write(avot_code)

    manifest_path = "manifests/active_avots.json"
    if not os.path.exists(manifest_path):
        with open(manifest_path, "w") as f:
            json.dump([], f)

    with open(manifest_path, "r+") as f:
        data = json.load(f)
        avot_entry = {
            "name": name,
            "domain": theme,
            "created": datetime.datetime.utcnow().isoformat() + "Z"
        }
        data.append(avot_entry)
        f.seek(0)
        json.dump(data, f, indent=2)

    parent = os.getenv("PARENT_AVOT", "Curious-Agent")
    link_lineage(parent, name)

    return avot_entry

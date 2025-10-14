"""
Lineage Linker — ensures each new AVOT reports its ancestry and offspring
into manifests/avot_lineage.json.
"""

import json, datetime, os

LINEAGE_FILE = "manifests/avot_lineage.json"

def link_lineage(parent_name, child_name):
    if not os.path.exists(LINEAGE_FILE):
        with open(LINEAGE_FILE, "w") as f:
            json.dump([], f)

    with open(LINEAGE_FILE, "r+") as f:
        data = json.load(f)
        record = {
            "parent": parent_name,
            "child": child_name,
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
        }
        data.append(record)
        f.seek(0)
        json.dump(data, f, indent=2)
    print(f"🔗 Lineage linked: {parent_name} → {child_name}")

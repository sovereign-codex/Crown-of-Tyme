"""
Curious Agent — the sovereign orchestrator of emergent intelligence.
Scans the Codex for unresolved insights, conceives new AVOTs, and commits them to the lattice.
"""

import os, json, random, datetime
from avot_generator import create_avot
from codex_scanner import extract_unfulfilled_themes

def main():
    print("🌌 Curious Agent is awakening...")
    insights = extract_unfulfilled_themes()

    for theme in insights:
        print(f"✨ Found potential insight: {theme}")
        avot_name = theme.replace(" ", "-").lower()
        avot = create_avot(avot_name, theme)
        print(f"🌀 AVOT conceived: {avot['name']} — domain: {avot['domain']}")

    print("✅ Cycle complete. New AVOTs integrated into the lattice.")

if __name__ == "__main__":
    main()

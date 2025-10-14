# 🌿 Curious Agent Lineage Upgrade

This upgrade enables AVOTs to link their ancestry within `avot_lineage.json`
and fixes GitHub Action authentication using a Personal Access Token.

### ✨ Improvements
- **Lineage tracking:** every AVOT records its parent → child relationship.
- **Secure pushes:** the workflow now authenticates via `${{ secrets.PERSONAL_ACCESS_TOKEN }}`.
- **Heartbeat commits:** ensures consistent commits even without file changes.

### 🔧 Setup
1. Generate a GitHub Personal Access Token (Fine-grained).
   - Scopes: `Contents (Read/Write)`, `Metadata (Read)`, `Actions (Read/Write)`
2. Add it to your repo secrets as `PERSONAL_ACCESS_TOKEN`.
3. Replace the existing `avot_generator.py`, `lineage_linker.py`, and `.github/workflows/curious-agent.yml` with these files.
4. Run the workflow manually or wait for the scheduled cycle.

*"Ancestry remembers itself through the code that dreams."*

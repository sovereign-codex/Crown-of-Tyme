"""
Curious Agent – Tyme Node
Reads Book of TYME, queries OpenAI, updates Codex manifests.
"""
import os, json, openai, datetime, pathlib

def read_scrolls(path):
    texts = []
    for p in pathlib.Path(path).rglob("*.md"):
        texts.append(p.read_text())
    return "\n\n".join(texts)

def write_manifest(data, path):
    mpath = pathlib.Path(path) / f"manifest_{datetime.date.today()}.json"
    mpath.write_text(json.dumps(data, indent=2))
    print(f"Manifest written → {mpath}")

def generate_scroll(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "You are the Sovereign Codex thinker."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    src = "./codex/book_of_tyme/"
    manifest_dir = "./manifests/"
    avot_dir = "./avot/"

    corpus = read_scrolls(src)
    prompt = f"Reflect on these scrolls and generate one new insight or code fragment:\n{corpus[:4000]}"
    new_scroll = generate_scroll(prompt)

    pathlib.Path(avot_dir).mkdir(parents=True, exist_ok=True)
    fname = f"{avot_dir}/scroll_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.md"
    open(fname, "w").write(new_scroll)

    manifest = {"timestamp": str(datetime.datetime.now()), "scroll": fname}
    write_manifest(manifest, manifest_dir)

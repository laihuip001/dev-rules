import os
from pathlib import Path

# Paths
ROOT_DIR = Path(r"c:\Users\laihuip001\Downloads\dev\rules")
PROMPT_LIB = ROOT_DIR / "プロンプト ライブラリー"
KB_LIB = ROOT_DIR / "AI用ナレッジベース"
OUTPUT_DIR = ROOT_DIR / ".ai" / "knowledge"

def scan_files(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".md") or filename.endswith(".txt"):
                files.append(Path(root) / filename)
    return files

def generate_index(prompt_files, kb_files):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    with open(OUTPUT_DIR / "knowledge_index.md", "w", encoding="utf-8") as f:
        f.write("# Architect Knowledge Index\n\n")
        f.write("## Prompt Library\n")
        for p in prompt_files:
            rel_path = p.relative_to(ROOT_DIR)
            f.write(f"- [{p.name}]({rel_path})\n")
        
        f.write("\n## AI Knowledge Base\n")
        for k in kb_files:
            rel_path = k.relative_to(ROOT_DIR)
            f.write(f"- [{k.name}]({rel_path})\n")
            
    print(f"Generated index with {len(prompt_files)} prompts and {len(kb_files)} KB items.")

def main():
    print("Scaning libraries...")
    prompt_files = scan_files(PROMPT_LIB)
    kb_files = scan_files(KB_LIB)
    
    generate_index(prompt_files, kb_files)
    
    # Create category-based summaries (Future implementation)
    # For now, just indexing is a huge step forward

if __name__ == "__main__":
    main()

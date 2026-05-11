import os
import shutil
import sys
from pathlib import Path

def add_image():
    print("🚀 Study-Saathi Image Manager")
    print("----------------------------")

    # 1. Get source image
    source_path = input("Enter the path to the source image: ").strip().strip("'").strip('"')
    if not os.path.exists(source_path):
        print(f"❌ Error: Source file not found: {source_path}")
        return

    # 2. Get target note
    note_path = input("Enter the path to the Markdown note (e.g., docs/Notes/Misc/DNS.md): ").strip().strip("'").strip('"')
    if not os.path.exists(note_path):
        print(f"❌ Error: Note not found: {note_path}")
        return

    # 3. Get image name (optional)
    default_name = os.path.basename(source_path)
    image_name = input(f"Enter target image name [default: {default_name}]: ").strip()
    if not image_name:
        image_name = default_name

    # 4. Determine paths
    docs_root = Path("docs")
    assets_root = docs_root / "assets" / "images"
    
    note_p = Path(note_path)
    # Relative path from docs/
    try:
        rel_note_path = note_p.relative_to(docs_root)
    except ValueError:
        # If path is not relative to docs/, assume it's just the name if it exists in docs
        print("❌ Error: Note path must be relative to the 'docs/' directory.")
        return

    # Create target directory mirroring the note's location
    # e.g., docs/Notes/Docker/Intro.md -> assets/images/Notes/Docker/
    target_dir = assets_root / rel_note_path.parent / rel_note_path.stem
    target_dir.mkdir(parents=True, exist_ok=True)
    
    target_path = target_dir / image_name

    # 5. Copy the file
    try:
        shutil.copy2(source_path, target_path)
        print(f"✅ Image copied to: {target_path}")
    except Exception as e:
        print(f"❌ Error copying file: {e}")
        return

    # 6. Calculate relative path for Markdown
    # We need to go up from the note's directory to docs/, then down to assets/images/...
    # Number of levels up to reach docs/ root
    levels_up = len(rel_note_path.parents) - 1
    prefix = "../" * levels_up
    
    # Path from docs/ to image
    rel_image_from_docs = target_path.relative_to(docs_root)
    
    final_md_path = f"{prefix}{rel_image_from_docs}"
    
    print("\n----------------------------")
    print("✨ Markdown snippet to insert:")
    print(f"![{rel_note_path.stem}]({final_md_path})")
    print("----------------------------\n")

if __name__ == "__main__":
    try:
        add_image()
    except KeyboardInterrupt:
        print("\n👋 Bye!")

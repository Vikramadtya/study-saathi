import os
from datetime import datetime

def define_env(env):
    @env.macro
    def leetcode(slug, difficulty="Easy"):
        # {{ leetcode("container-with-most-water", "Medium") }}
        # Set a colored circle based on difficulty
        color = "🟢" if difficulty == "Easy" else "🟡" if difficulty == "Medium" else "🔴"
        
        # Returns a beautifully formatted Markdown block
        return f"""
!!! question "Problem Details"
    **Difficulty:** {color} {difficulty}

    [Solve on LeetCode :fontawesome-solid-arrow-up-right-from-square:](https://leetcode.com/problems/{slug}/){{ .md-button .md-button--primary }}
"""

    @env.macro
    def recent_solves(location="",limit=5):
        # Scan your LeetCode directory for the most recently modified files
        path = f"docs/Code Scratch/{location}"
        files = []
        for root, _, filenames in os.walk(path):
            for f in filenames:
                if f.endswith(".md"):
                    full_path = os.path.join(root, f)
                    files.append((full_path, os.path.getmtime(full_path)))
        
        # Sort by modification time
        sorted_files = sorted(files, key=lambda x: x[1], reverse=True)[:limit]
        
        lines = ["| Problem | Solved On |", "| --- | --- |"]
        for fpath, mtime in sorted_files:
            name = os.path.basename(fpath).replace(".md", "").replace("-", " ").title()
            # Convert internal path to site URL
            url = fpath.replace("docs/", "").replace(".md", "/")
            date = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
            lines.append(f"| [{name}]({env.conf['site_url']}{url}) | {date} |")
            
        return "\n".join(lines)
# salva questo script come rename_imports.py
import os

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            new_content = content.replace("from verbamanent.", "from verbamanent.").replace("import verbamanent.", "import verbamanent.")
            if content != new_content:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)
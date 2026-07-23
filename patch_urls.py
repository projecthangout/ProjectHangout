import re
import os

def patch_file(filepath, has_ws=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for imports
    import_statement = 'import { API_BASE_URL' + (', WS_BASE_URL' if has_ws else '') + ' } from "../lib/utils";\n'
    if 'import { API_BASE_URL' not in content:
        # Add after other imports
        content = re.sub(r'(import .*?;?\n)', r'\1' + import_statement, content, count=1)
        
    # Replace URLs
    content = content.replace('"http://127.0.0.1:8000', '`${API_BASE_URL}')
    content = content.replace('\'http://127.0.0.1:8000', '`${API_BASE_URL}')
    content = content.replace('`http://127.0.0.1:8000', '`${API_BASE_URL}')
    
    if has_ws:
        content = content.replace('"ws://localhost:8000', '`${WS_BASE_URL}')
        content = content.replace('\'ws://localhost:8000', '`${WS_BASE_URL}')
        content = content.replace('`ws://localhost:8000', '`${WS_BASE_URL}')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
patch_file('frontend/src/pages/Home.jsx', has_ws=False)
patch_file('frontend/src/pages/Call.jsx', has_ws=True)
print("Patch applied successfully.")

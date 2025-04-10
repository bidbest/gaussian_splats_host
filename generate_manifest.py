import os
import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
GAUSSIANS_DIR = os.path.join(ROOT_DIR, 'gaussians')
OUTPUT_FILE = os.path.join(ROOT_DIR, 'manifest.json')

manifest = []

for entry in os.scandir(GAUSSIANS_DIR):
    if entry.is_dir():
        gaussian_name = entry.name
        gaussian_path = os.path.join(GAUSSIANS_DIR, gaussian_name)
        
        ply_file = None
        for file in os.listdir(gaussian_path):
            if file.endswith('.ply'):
                ply_file = os.path.join('gaussians', gaussian_name, file)
                break
        
        if ply_file:
            manifest.append({
                "name": gaussian_name,
                "path": ply_file
            })

# Save manifest.json
with open(OUTPUT_FILE, 'w') as f:
    json.dump(manifest, f, indent=2)

print(f"✅ Manifest created at {OUTPUT_FILE} with {len(manifest)} entries.")

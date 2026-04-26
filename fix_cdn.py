import os

files_to_update = [
    'public/full_utopia.html',
    'public/mirror/www.utopiatokyo.com/minigame.html'
]

for filepath in files_to_update:
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The previous script broke the CDN URLs because it replaced "Utopia" leaving "Toyko" as it was originally misspelled "UtopiaToyko" in the CDN URLs.
    content = content.replace("Snug MasksToyko", "UtopiaToyko")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed CDN URLs in {filepath}")

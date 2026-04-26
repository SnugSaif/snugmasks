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

    # 1. Standard text replacements
    content = content.replace("Utopia Tokyo", "Snug Masks")
    content = content.replace("UTOPIA TOKYO", "SNUG MASKS")
    content = content.replace("utopia tokyo", "snug masks")
    content = content.replace("Utopia", "Snug Masks")
    
    # 2. Fix inner preloader HTML that spells U T O P I A T O K Y O
    # UTOPIA (6 letters) -> SNUG (4 letters)
    content = content.replace(
        '<div data-scramble="trigger">U</div><div data-scramble="trigger" class="u-text-center">T</div><div data-scramble="trigger" class="u-text-right">O</div></div><div aria-hidden="true" class="preloader__item"><div data-scramble="trigger">P</div><div data-scramble="trigger" class="u-text-center">I</div><div data-scramble="trigger" class="u-text-right">A</div>',
        '<div data-scramble="trigger">S</div><div data-scramble="trigger" class="u-text-center">N</div><div data-scramble="trigger" class="u-text-right">U</div></div><div aria-hidden="true" class="preloader__item"><div data-scramble="trigger">G</div><div data-scramble="trigger" class="u-text-center">-</div><div data-scramble="trigger" class="u-text-right">-</div>'
    )
    
    # TOKYO (5 letters) -> MASKS (5 letters)
    content = content.replace(
        '<div data-scramble="trigger">T</div><div data-scramble="trigger" class="u-text-center">O</div><div data-scramble="trigger" class="u-text-center">K</div><div data-scramble="trigger" class="u-text-center">Y</div><div data-scramble="trigger" class="u-text-right">O</div>',
        '<div data-scramble="trigger">M</div><div data-scramble="trigger" class="u-text-center">A</div><div data-scramble="trigger" class="u-text-center">S</div><div data-scramble="trigger" class="u-text-center">K</div><div data-scramble="trigger" class="u-text-right">S</div>'
    )
    
    # Hero Title (Ut<strong>o</strong>pia)
    content = content.replace('Ut<strong>o</strong>pia', 'Sn<strong>u</strong>g')
    content = content.replace('Tok<strong>y</strong>o', 'Ma<strong>s</strong>ks')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filepath}")

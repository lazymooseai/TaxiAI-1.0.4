import os
import glob

def fix_typographic_quotes_in_directory(directory="."):
    """
    Käy läpi kaikki .py-tiedostot annetussa hakemistossa ja sen alihakemistoissa,
    ja korvaa typografiset lainausmerkit standardinmukaisilla Python-lainausmerkeillä.
    """
    replacements = {
        '“': '"',
        '”': '"',
        '”': '"',  # Varmuuden vuoksi erilaiset variaatiot
        '‘': "'",
        '’': "'"
    }

    # Etsi kaikki .py tiedostot rekursiivisesti
    search_pattern = os.path.join(directory, "**", "*.py")
    files = glob.glob(search_pattern, recursive=True)
    
    fixed_count = 0
    
    for filepath in files:
        # Älä korjaa tätä skriptiä itseään
        if filepath.endswith("fix_quotes.py"):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        for bad_quote, good_quote in replacements.items():
            new_content = new_content.replace(bad_quote, good_quote)
            
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Korjattu tiedosto: {filepath}")
            fixed_count += 1
            
    print(f"\nValmis! Korjattiin lainausmerkit yhteensä {fixed_count} tiedostosta.")

if __name__ == "__main__":
    fix_typographic_quotes_in_directory()

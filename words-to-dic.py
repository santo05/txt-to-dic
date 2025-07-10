def convert_wordlist_to_unicode_dic(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        words = [line.strip().strip('"') for line in f if line.strip()]

    unique_words = sorted(set(words))

    # Prepare content
    content = "#LID 1033\n" + "\n".join(unique_words) + "\n"

    # Write using UTF-16 LE with BOM
    with open(output_file, 'w', encoding='utf-16') as f:
        f.write(content)

    print(f"Unicode .dic file created: {output_file}")

# Usage
convert_wordlist_to_unicode_dic(r"words.txt", r"english.dic")


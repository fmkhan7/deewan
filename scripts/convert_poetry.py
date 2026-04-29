#!/usr/bin/env python3
"""
Poetry Converter: TXT to JSON
Converts plain text poetry files to 11ty-compatible JSON format.

Usage:
    python convert_poetry.py input.txt output.json
    python convert_poetry.py input.txt output.json --title "غزل کا عنوان" --meter "ہزجِ مثمن محذوف"
    python convert_poetry.py input_dir/ output_dir/ --type ghazal
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path


def parse_ghazal(text: str) -> dict:
    """Parse ghazal text into couplets."""
    couplets = []
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    for i in range(0, len(lines) - 1, 2):
        couplet = {
            "line1": lines[i],
            "line2": lines[i + 1] if i + 1 < len(lines) else ""
        }
        couplets.append(couplet)
    
    return couplets


def parse_multi_poem_file(input_path: str) -> list:
    """Parse a file containing multiple poems separated by 'غزل' markers.
    
    Handles variations:
    - غزل (alone on line)
    - غزل  (with trailing space)
    - غزل وہ آج... (غزل + poem start on same line)
    """
    
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by "غزل" marker - handle various patterns
    # Pattern 1: غزل at start of line (with optional trailing space)
    # Pattern 2: غزل followed by text on same line
    
    # First, normalize: add newline after pure "غزل" lines
    content = re.sub(r'^غزل\s*$', '\nغزل\n', content, flags=re.MULTILINE)
    
    # Now split by the marker
    parts = content.split('\nغزل\n')
    
    result = []
    for i, poem_text in enumerate(parts):
        poem_text = poem_text.strip()
        if not poem_text:
            continue
        
        # Check if poem starts with "غزل وہ آج..." or similar (غزل + text on same line)
        if poem_text.startswith('غزل '):
            poem_text = poem_text[4:]  # Remove "غزل " prefix
        
        lines = poem_text.split('\n')
        
        # Skip if first line is empty or too short
        first_line = lines[0].strip() if lines else ""
        if len(first_line) < 3:
            continue
        
        # Create title from first few words (up to 4 words)
        words = first_line.split()
        title = ' '.join(words[:4])
        if len(words) > 4:
            title += '...'
        
        # Parse couplets (pairs of lines)
        couplets = []
        valid_lines = [l.strip() for l in lines if l.strip() and len(l.strip()) > 2]
        
        for j in range(0, len(valid_lines) - 1, 2):
            couplet = {
                "line1": valid_lines[j],
                "line2": valid_lines[j + 1] if j + 1 < len(valid_lines) else ""
            }
            couplets.append(couplet)
        
        if couplets:
            result.append({
                "title": title,
                "slug": create_slug(title),
                "meter": "آزاد",
                "couplets": couplets
            })
    
    return result


def convert_multi_file(input_path: str, output_dir: str) -> int:
    """Convert a file with multiple poems into separate JSON files."""
    
    poems = parse_multi_poem_file(input_path)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    count = 0
    for i, poem in enumerate(poems):
        # Use index if slug might duplicate
        if i > 0:
            poem['slug'] = f"{poem['slug']}-{i+1}"
        
        output_file = output_path / f"{poem['slug']}.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(poem, f, ensure_ascii=False, indent=2)
        
        print(f"✓ {i+1}. {poem['title']} -> {output_file.name} ({len(poem['couplets'])} couplets)")
        count += 1
    
    return count


def parse_nazm(text: str) -> dict:
    """Parse nazm (free verse) text into verses."""
    verses = []
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    current_verse = []
    for line in lines:
        # Empty line indicates new verse
        if not line:
            if current_verse:
                verses.append({"text": '\n'.join(current_verse)})
                current_verse = []
        else:
            current_verse.append(line)
    
    # Add last verse if exists
    if current_verse:
        verses.append({"text": '\n'.join(current_verse)})
    
    return verses


def create_slug(title: str) -> str:
    """Create URL-friendly slug from title."""
    # Replace spaces with hyphens, keep Urdu chars
    slug = title.lower()
    slug = re.sub(r'[^\w\s\u0600-\u06FF-]', '', slug)
    slug = re.sub(r'[\s]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')


def convert_file(input_path: str, output_path: str, poetry_type: str = "ghazal",
                title: str = None, meter: str = None) -> dict:
    """Convert a single poetry file to JSON."""
    
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # If no title provided, use filename
    if not title:
        title = Path(input_path).stem
    
    # Parse based on type
    if poetry_type == "ghazal":
        content = parse_ghazal(text)
        structure = {"couplets": content}
    else:  # nazm
        content = parse_nazm(text)
        structure = {"verses": content}
    
    # Create output
    poem = {
        "title": title,
        "slug": create_slug(title),
        "meter": meter or "آزاد",
        **structure
    }
    
    # Write JSON
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(poem, f, ensure_ascii=False, indent=2)
    
    return poem


def convert_directory(input_dir: str, output_dir: str, poetry_type: str = "ghazal") -> int:
    """Convert all .txt files in a directory to JSON."""
    
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    count = 0
    for txt_file in input_path.glob('*.txt'):
        # Use filename as title (without extension)
        title = txt_file.stem
        output_file = output_path / f"{txt_file.stem}.json"
        
        try:
            convert_file(str(txt_file), str(output_file), poetry_type, title)
            print(f"✓ Converted: {txt_file.name} -> {output_file.name}")
            count += 1
        except Exception as e:
            print(f"✗ Error converting {txt_file.name}: {e}")
    
    return count


def main():
    parser = argparse.ArgumentParser(
        description='Convert poetry from TXT to JSON for 11ty',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Single file conversion
  python convert_poetry.py my-ghazal.txt output.json --title "میرا غزل" --meter "ہزج"
  
  # Batch convert directory
  python convert_poetry.py ghazals/ output/ghazals/ --type ghazal
  
  # Convert nazms
  python convert_poetry.py nazms/ output/nazms/ --type nazm
'''
    )
    
    parser.add_argument('input', help='Input file or directory')
    parser.add_argument('output', help='Output file or directory')
    parser.add_argument('--type', choices=['ghazal', 'nazm'], default='ghazal',
                       help='Poetry type (default: ghazal)')
    parser.add_argument('--multi', action='store_true',
                       help='Input file contains multiple poems separated by "غزل" markers')
    parser.add_argument('--title', help='Title for single file conversion')
    parser.add_argument('--meter', help='Meter/بحر for the poem')
    
    args = parser.parse_args()
    
    # Determine if input is file or directory
    input_path = Path(args.input)
    
    if args.multi and input_path.is_file():
        # Multi-poem file conversion
        count = convert_multi_file(args.input, args.output)
        print(f"\n✓ Converted {count} poems to {args.output}")
        
    elif input_path.is_file():
        # Single file conversion
        poem = convert_file(args.input, args.output, args.type, args.title, args.meter)
        print(f"✓ Converted: {poem['title']}")
        print(f"  Slug: {poem['slug']}")
        print(f"  Couplets: {len(poem.get('couplets', []))}")
        print(f"  Verses: {len(poem.get('verses', []))}")
        
    elif input_path.is_dir():
        # Directory batch conversion
        count = convert_directory(args.input, args.output, args.type)
        print(f"\n✓ Converted {count} files")
        
    else:
        print(f"Error: Input path '{args.input}' does not exist")
        sys.exit(1)


if __name__ == '__main__':
    main()
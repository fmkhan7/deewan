#!/usr/bin/env python3
"""
Convert preface.txt to preface.md format.
"""

import re

def parse_preface(input_path: str) -> str:
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Skip the first two lines: ﷽ and مقدمہ
    lines = lines[2:]
    
    output = []
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue
        
        # Count leading spaces
        leading_spaces = len(line) - len(line.lstrip())
        
        if leading_spaces >= 5:  # Assume couplets have more indentation
            # Collect all consecutive highly indented lines
            couplet_lines = []
            while i < len(lines) and (len(lines[i].rstrip()) - len(lines[i].rstrip().lstrip()) >= 5 or lines[i].strip() == ''):
                if lines[i].strip():
                    couplet_lines.append(lines[i].strip())
                i += 1
            if couplet_lines:
                output.append('<div class="couplet">' + '\n'.join(couplet_lines) + '</div>')
        else:
            # Prose paragraph
            para_lines = []
            while i < len(lines) and (len(lines[i].rstrip()) - len(lines[i].rstrip().lstrip()) < 5):
                if lines[i].strip():
                    para_lines.append(lines[i].strip())
                i += 1
            if para_lines:
                output.append('<p>' + ' '.join(para_lines) + '</p>')
    
    return '\n'.join(output)

if __name__ == '__main__':
    content = parse_preface('/Users/farooq/git/deewan/scripts/preface.txt')
    print(content)
import re
import os

def is_valid_line(line):

    line = line.strip()
    
    if ":" not in line:
        return False
    
    email, password = line.split(":", 1)
    
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        return False
    
    if not password:
        return False
    
    return True

def filter_combos(input_file="data/combo.txt"):

    os.makedirs(os.path.dirname(input_file), exist_ok=True)
    
    try:
        valid_lines_set = set()
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.strip()
                if line and is_valid_line(line):
                    valid_lines_set.add(line)
        
        valid_lines = list(valid_lines_set)
        
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(valid_lines))
            
        return True
    except Exception:
        return False

if __name__ == "__main__":
    filter_combos()
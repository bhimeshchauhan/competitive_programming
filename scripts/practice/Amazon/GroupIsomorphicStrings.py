# O(n) time and space in the length of string
def unique_iso_string(string: str) -> str:
    seen: Dict[str, str] = {}
    current, key = ord('a'), []
    for char in string:
        if char not in seen:
            seen[char] = chr(current)
            current += 1
        key.append(seen[char])
    return ''.join(key)

# O(n) time and space in the size of strings or O(nm) where n = length of 
# strings, m = length of strings[i]
def group_strings(strings: List[str]) -> List[str]:
    iso_strings: Dict[str, List[str]] = defaultdict(list)
    for string in strings:
        key = unique_iso_string(string)
        iso_strings[key].append(string)
    return list(iso_strings.values())
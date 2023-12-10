def get_duplicate_ids(ids):
    duplicates = []
    seen = set()
    for item in ids:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates

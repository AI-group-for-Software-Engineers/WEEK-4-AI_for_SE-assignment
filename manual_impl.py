# manual_impl.py
# Manual implementation without AI assistance

def sort_dicts_manual(data, key, reverse=False):
    """
    Manually sort a list of dictionaries by the specified key.
    Missing keys are placed at the end.
    """
    decorated = []
    for i, d in enumerate(data):
        val = d.get(key, None)
        # Use tuple for stable sorting and handle missing keys
        decorated.append(((val is None), val, i, d))
    decorated.sort(reverse=reverse)
    # Extract sorted dictionaries
    return [item[3] for item in decorated]

def sort_dicts_ai(data, key, reverse=False):
    """
    AI-style implementation using sorted().
    Handles mixed types (strings, numbers, None) safely.
    """

    def safe_get(d):
        val = d.get(key, None)
        if val is None:
            # Push missing values to the end
            return (2, float('inf')) if not reverse else (-2, float('-inf'))

        # Try to convert to float
        try:
            return (0, float(val))
        except (ValueError, TypeError):
            # Keep as string if not numeric
            return (1, str(val).lower())

    return sorted(data, key=safe_get, reverse=reverse)

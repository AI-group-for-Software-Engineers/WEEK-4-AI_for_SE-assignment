# sample_data.py
# Generates sample list of dictionaries for testing and benchmarking

import random

def make_data(n=10000):
    """Generate list of dictionaries with random 'age', 'name', and 'score'."""
    names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward']
    data = []
    for _ in range(n):
        d = {}
        # 10% chance of missing 'age'
        if random.random() > 0.1:
            d['age'] = random.randint(18, 80)
        # 50% chance of having a name
        if random.random() > 0.5:
            d['name'] = random.choice(names)
        d['score'] = round(random.random() * 100, 2)
        data.append(d)
    return data

if __name__ == "__main__":
    print(make_data(5))

# tests.py
# Verifies both functions produce identical results

from sample_data import make_data
from ai_impl import sort_dicts_ai
from manual_impl import sort_dicts_manual

def run_tests():
    data = make_data(20)
    keys = ['age', 'name', 'score']

    for key in keys:
        ai_sorted = sort_dicts_ai(data, key)
        manual_sorted = sort_dicts_manual(data, key)

        # Compare first 5 results for clarity
        print(f"\nTesting key: {key}")
        print("AI first 5:", ai_sorted[:5])
        print("Manual first 5:", manual_sorted[:5])
        assert [d.get(key) for d in ai_sorted] == [d.get(key) for d in manual_sorted], \
            f"Mismatch on key '{key}'"

    print("\n✅ All tests passed successfully.")

if __name__ == "__main__":
    run_tests()

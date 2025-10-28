# benchmarks.py
# Compare performance between AI-generated and manual functions

import time
from sample_data import make_data
from ai_impl import sort_dicts_ai
from manual_impl import sort_dicts_manual
import tracemalloc

def time_function(func, data, key, repeat=5):
    """Measure average runtime."""
    times = []
    for _ in range(repeat):
        test_data = list(data)
        start = time.perf_counter()
        func(test_data, key)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)

def measure_memory(func, data, key):
    """Measure peak memory usage."""
    tracemalloc.start()
    func(data, key)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1024  # KB

def benchmark():
    print("Running benchmarks...\n")
    for n in [1000, 10000, 50000]:
        data = make_data(n)
        key = 'age'

        ai_time = time_function(sort_dicts_ai, data, key)
        manual_time = time_function(sort_dicts_manual, data, key)

        ai_mem = measure_memory(sort_dicts_ai, data, key)
        manual_mem = measure_memory(sort_dicts_manual, data, key)

        print(f"Dataset size: {n}")
        print(f"  AI version:     {ai_time:.6f}s | {ai_mem:.2f} KB peak memory")
        print(f"  Manual version: {manual_time:.6f}s | {manual_mem:.2f} KB peak memory")
        print("-" * 60)

if __name__ == "__main__":
    benchmark()

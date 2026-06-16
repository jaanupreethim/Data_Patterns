from collections import Counter

def highest_frequency_chars(lines):
    results = []
    for line in lines:
        filtered = [c for c in line if c.isalpha()]
        if not filtered:
            results.append("")
            continue
        counts = Counter(filtered)
        max_freq = max(counts.values())
        highest_chars = [c for c, freq in counts.items() if freq == max_freq]
        
        caps = sorted([c for c in highest_chars if c.isupper()])
        smalls = sorted([c for c in highest_chars if c.islower()])
        results.append("".join(caps + smalls))
    return results

if __name__ == "__main__":
    n = int(input("Enter number of lines (N): "))
    user_lines = [input(f"Enter line {i+1}: ") for i in range(n)]
    freq_results = highest_frequency_chars(user_lines)
    for res in freq_results:
        print(res)

import re
import sys
from pathlib import Path

# Default log file path (can be overridden by CLI argument)
LOG_FILE = sys.argv[1] if len(sys.argv) > 1 else "ai/logs/sample_logs.txt"

# Patterns to extract (add more as needed)
PATTERNS = [
    re.compile(r"ERROR:"),
    re.compile(r"EXCEPTION:"),
    re.compile(r"FAIL:")
]

def scrape_log(log_path):
    results = []
    with open(log_path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, 1):
            for pat in PATTERNS:
                if pat.search(line):
                    results.append({
                        "line": idx,
                        "content": line.strip()
                    })
    return results

def main():
    log_path = Path(LOG_FILE)
    if not log_path.exists():
        print(f"Log file not found: {log_path}")
        sys.exit(1)
    results = scrape_log(log_path)
    if results:
        print("Detected issues in log file:")
        for entry in results:
            print(f"Line {entry['line']}: {entry['content']}")
    else:
        print("No issues found in log file.")

if __name__ == "__main__":
    main()

import argparse
import json
from .scoring import analyze

def main():
    parser = argparse.ArgumentParser(description="OBSIDIAN local heuristic security analyzer")
    parser.add_argument("kind", choices=("text", "url"))
    parser.add_argument("value")
    args = parser.parse_args()
    print(json.dumps(analyze(args.kind, args.value), indent=2))

if __name__ == "__main__":
    main()

#!/usr/bin/env bash

set -euo pipefail

# If less than two options provided, display use case and exit
if [[ $# -lt 2 ]]; then 
    echo "Usage: $0 <problem_number> <title>"
    exit 1 
fi 

problem_number="$1"
shift

title="$*"

padded=$(printf "%04d" "$problem_number")

slug=$(
    echo "$title" \
        | tr '[:upper:]' '[:lower:]' \
        | sed -E 's/[^a-z0-9]+/-/g' \
        | sed -E 's/^-+|-+$//g'
)

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
dir="${ROOT_DIR}/problems/${padded}-${slug}"

mkdir -p "$dir"

solution_file="${dir}/${padded}_solution.py"

cat > "$solution_file" <<EOF
"""
File: ${padded}_solution.py

Description: Project Euler Problem ${problem_number}: ${title}

Author: Spencer Veatch (sveatch@willamette.edu)

Last Modified: YYYY-MM-DD
"""

def main() -> None:
    pass


if __name__ == "__main__":
    main()
EOF

echo "Created $dir"

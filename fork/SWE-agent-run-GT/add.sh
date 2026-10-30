#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

# Match regular files strictly smaller than 80 MB (80,000,000 bytes).
# Pass paths directly to Git so spaces and other special characters are safe.
find \
  "$repo_root/fork/SWE-agent-get-factor/trajectories" \
  "$repo_root/fork/SWE-agent-run-GT/trajectories" \
  -type f \
  \( -name '*cost.json' -o -name '*.debug.log' -o -name '*.patch' \) \
  -size -80000000c \
  -exec git -C "$repo_root" add -f -- {} +

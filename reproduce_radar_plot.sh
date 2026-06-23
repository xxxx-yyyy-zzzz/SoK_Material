#!/bin/sh
set -eu

: "${RADAR_SCRIPT:=radar.py}"
: "${OUTPUT_FILE:=out/vfl_radar_comparison_feasibility.png}"

if [ ! -f "$RADAR_SCRIPT" ]; then
    echo "Radar plot script not found." >&2
    echo "Expected to find $RADAR_SCRIPT in the repository root." >&2
    echo "If the file was moved, set RADAR_SCRIPT to the new path." >&2
    exit 2
fi

echo "Running radar plot reproduction script: $RADAR_SCRIPT"
mkdir -p out

python "$RADAR_SCRIPT" ${RADAR_ARGS:-}

if [ -f "$OUTPUT_FILE" ]; then
    echo "Found expected output: $OUTPUT_FILE"
    ls -lh "$OUTPUT_FILE"
    exit 0
fi

found_output=$(
    find . -maxdepth 4 \( -name "*radar*.png" -o -name "vfl_radar_comparison_feasibility.*" \) -print |
        sort |
        head -n 1
)

if [ -n "$found_output" ]; then
    echo "Found radar plot output: $found_output"
    ls -lh "$found_output"
    exit 0
fi

echo "The script completed, but no radar plot output was found." >&2
echo "Set OUTPUT_FILE to the generated file path if the output has a different name." >&2
exit 3

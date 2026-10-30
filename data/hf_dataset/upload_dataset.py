"""Normalize the example datasets and upload them to Hugging Face.

Run with ``--dry-run`` to validate locally. Uploads use ``HF_TOKEN`` or the
credentials saved by the Hugging Face CLI. Dictionaries and complex lists
are stored as JSON strings; use ``json.loads`` to recover them. Simple lists
of strings remain native lists.
"""

import argparse
import json
from pathlib import Path

from datasets import Dataset, DatasetDict, Features, Sequence, Value


DATA_DIR = Path(__file__).resolve().parent
REPO_ID = "SWE-bench-Live/ORACLE-SWE"
DATASET_FIELDS = [
    "instance_id",
    "repo",
    "base_commit",
    "pull_number",
    "problem_statement",
    "addtional_setup_cmd",
    "before_repo_set_cmd",
    "patch",
    "test_patch",
    "FAIL_TO_PASS",
    "PASS_TO_PASS",
    "INVALID_TESTS",
    "f2p_parsed",
    "F2P_content",
    "test_cmd",
    "test_cmds",
    "f2p_cmd",
    "selected_test_files_to_run",
    "location",
    "location_content",
    "error_context",
    "api",
    "image",
]
# Hugging Face split names cannot contain slashes.
SPLIT_FILES = {
    "SWE_bench__Verified": "dataset_samples_from_SWE_bench_Verified.jsonl",
    "SWE_bench_Live__Verified": "dataset_samples_from_SWE_bench_Live.jsonl",
    "SWE_bench_Pro__Python": "dataset_samples_from_SWE_bench_Pro_Python.jsonl",
    "SWE_bench_Pro__Golang": "dataset_samples_from_SWE_bench_Pro_Golang.jsonl",
}


def infer_feature(values):
    """Choose one column type from all non-null values across every split."""
    values = [value for value in values if value is not None]
    types = {type(value) for value in values}
    if types == {list} and all(
        isinstance(item, str) for value in values for item in value
    ):
        return Sequence(Value("string"))
    if types == {bool}:
        return Value("bool")
    if types and types <= {int, float}:
        return Value("float64" if float in types else "int64")
    return Value("string")


def normalize_value(value, feature):
    """Preserve nulls and native values, and JSON-encode complex columns."""
    if value is None:
        return None
    if isinstance(feature, Value) and feature.dtype == "string":
        return value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)
    return value


def build_dataset(data_dir=DATA_DIR):
    """Load all four JSONL files with only the requested fields, in order."""
    samples = {}
    for split, filename in SPLIT_FILES.items():
        path = Path(data_dir) / filename
        records = []
        with path.open(encoding="utf-8") as stream:
            for line_number, line in enumerate(stream, start=1):
                if not line.strip():
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(
                        f"{path}:{line_number}: invalid JSON: {exc.msg}"
                    ) from exc
                if not isinstance(record, dict):
                    raise ValueError(f"{path}:{line_number}: expected a JSON object")
                records.append(record)
        samples[split] = records

    records = [record for split_records in samples.values() for record in split_records]
    if not records:
        raise ValueError("The input files contain no dataset records")
    features = Features(
        {
            field: infer_feature([record.get(field) for record in records])
            for field in DATASET_FIELDS
        }
    )
    # Explicit features keep all-null and empty columns consistent across splits.
    return DatasetDict(
        {
            split: Dataset.from_dict(
                {
                    field: [
                        normalize_value(record.get(field), features[field])
                        for record in rows
                    ]
                    for field in DATASET_FIELDS
                },
                features=features,
            )
            for split, rows in samples.items()
        }
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data-dir", type=Path, default=DATA_DIR, help="Directory of sample JSONL files"
    )
    parser.add_argument("--repo-id", default=REPO_ID, help="Hugging Face dataset repository")
    parser.add_argument(
        "--dry-run", action="store_true", help="Validate and summarize without uploading"
    )
    args = parser.parse_args()

    dataset = build_dataset(args.data_dir)
    print(dataset)
    if not args.dry_run:
        dataset.push_to_hub(args.repo_id)
        print(f"Uploaded to https://huggingface.co/datasets/{args.repo_id}")


if __name__ == "__main__":
    main()

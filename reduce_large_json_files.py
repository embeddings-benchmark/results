import json
from pathlib import Path

import mteb

RESULTS_DIR = Path(__file__).parent / "results"
# CI rejects anything above 10 MiB, so leave a bit of headroom.
MAX_SIZE = int(9.5 * 1024 * 1024)
COMPACT = (",", ":")


def resize_flores():
    """
    includes only relevant splits from the FloresBitextMining.json files
    """
    paths = RESULTS_DIR.glob("**/FloresBitextMining.json")

    for p in paths:
        if p.stat().st_size < MAX_SIZE:
            continue
        print(f"Filtering {p} down to the splits and subsets Flores defines")
        res = mteb.TaskResult.from_disk(p)
        res.validate_and_filter_scores().to_disk(p)


def remove_spaces():
    """
    removes spaces from the json files
    """
    for file in RESULTS_DIR.glob("**/*.json"):
        if file.stat().st_size < MAX_SIZE:
            continue
        print(f"Resizing {file} to have no indentations")
        with file.open("r") as f:
            data = json.load(f)

        with file.open("w") as f:
            json.dump(data, f, indent=None)


def collapse_run_settings():
    """
    merges the per-subset lines of the run_settings.jsonl files

    mteb writes one line per (task, split, subset), so a task like Flores with
    41k language pairs produces 41k near-identical lines. Lines that agree on
    everything but the subset -- the versions and the encode_kwargs included --
    are merged into one line carrying a `subsets` list.
    """
    for file in RESULTS_DIR.glob("**/run_settings.jsonl"):
        if file.stat().st_size < MAX_SIZE:
            continue
        print(f"Collapsing the per-subset lines of {file}")

        groups: dict[str, dict] = {}
        for line in file.read_text().splitlines():
            if not line.strip():
                continue
            record = json.loads(line)
            subsets = record.pop("subsets", None)
            if subsets is None:
                subsets = [record.pop("subset")]
            # everything but the subset has to match for a merge
            key = json.dumps(record, sort_keys=True, separators=COMPACT)
            groups.setdefault(key, {**record, "subsets": []})["subsets"].extend(subsets)

        with file.open("w") as f:
            for record in groups.values():
                f.write(json.dumps(record, separators=COMPACT) + "\n")


if __name__ == "__main__":
    resize_flores()
    remove_spaces()
    collapse_run_settings()

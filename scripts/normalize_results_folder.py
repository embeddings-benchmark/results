"""Normalize folder structure for the results folder such that results are on the same format as the mteb run command."""

import json
import logging
from pathlib import Path

import mteb
from packaging.version import Version
from tqdm import tqdm

logger = logging.getLogger(__name__)


def resolve_conflict_meta(current_path: Path, expected_path: Path) -> None:
    """Resolve conflict between two meta files."""
    with open(current_path, "r") as f:
        current_meta = json.load(f)

    with open(expected_path / "model_meta.json", "r") as f:
        expected_meta = json.load(f)

    if current_meta == expected_meta:
        logger.info("Meta file is the same, removing")
        current_path.unlink()
    else:
        logger.info("Meta file is different, please resolve manually.")


def resolve_conflict_result(currenet_path: Path, expected_path: Path) -> None:
    """Resolve conflict between two result files."""
    old_res = mteb.MTEBResults.from_disk(currenet_path)
    new_res = mteb.MTEBResults.from_disk(expected_path)
    if old_res == new_res:
        logger.info("Result file is the same, removing")
        currenet_path.unlink()
    else:
        # check version and keep the newest
        old_version = old_res.mteb_version
        new_version = new_res.mteb_version
        if Version(old_version) > Version(new_version):
            logger.info("Older version of result file, removing")
            currenet_path.unlink()
        elif Version(old_version) == Version(new_version):
            logger.info(
                "Same version of result file, removing, but scores are different. Please resolve manually."
            )
            logger.info(f"Old scores: {old_res.scores}")
            logger.info(f"New scores: {new_res.scores}")
        else:
            logger.info("Newer version of result file, moving")
            currenet_path.rename(expected_path / currenet_path.name)


def resolve_conflict(current_path: Path, expected_path: Path) -> None:
    """Resolve conflict between two files."""
    if current_path.name == "model_meta.json":
        resolve_conflict_meta(current_path, expected_path)
    else:
        resolve_conflict_result(current_path, expected_path)


def main(attempt_to_resolve_conflict: bool = False) -> None:
    """Main function."""
    results_folder = Path(__file__).parent.parent / "results"
    meta_files = results_folder.glob("**/model_meta.json")
    meta_files = list(meta_files)

    conflict_encountered = False

    for meta_file in tqdm(meta_files):
        with open(meta_file, "r") as f:
            meta = json.load(f)

        mdl_name, revision = meta["name"], meta["revision"]

        mdl_name = mdl_name.replace(" ", "_").replace("/", "__")

        if revision is None:
            revision = meta_file.parent.name

        expected_path = results_folder / mdl_name / revision
        if expected_path != meta_file.parent:
            logger.info(f"Moving {meta_file.parent}/*.json to {expected_path}")

            files_in_folder = meta_file.parent.glob("*.json")

            for file in files_in_folder:
                # check if file already exists
                if (expected_path / file.name).exists():
                    conflict_encountered = True
                    logger.info(f"File {file} already exists in {expected_path}")
                    if attempt_to_resolve_conflict is True:
                        resolve_conflict(file, expected_path / file.name)
                else:
                    # make sure the folder exists
                    expected_path.mkdir(parents=True, exist_ok=True)
                    file.rename(expected_path / file.name)

    if conflict_encountered and not attempt_to_resolve_conflict:
        raise Exception("Conflicts encountered.")


if __name__ == "__main__":
    main()

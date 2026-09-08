"""Shared git helpers for tests that compare a PR's result files against the base branch.

All helpers resolve a single ``base_ref`` (see :func:`get_base_ref`) and use it for
*both* the list of changed files and the "old" version of each file. Using two
different refs for those two purposes is what caused the false positives in
https://github.com/embeddings-benchmark/mteb/issues/5242.
"""

import os
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


def _run_git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def get_base_ref() -> str:
    """Return the commit that the checked-out changes should be compared against.

    This is the merge-base of ``main`` and ``HEAD``, i.e. the commit on main that the
    checked-out code actually branched off from. In CI, ``HEAD`` is GitHub's
    ``refs/pull/N/merge`` commit whose first parent is the tip of main at the time the
    merge commit was created; ``git merge-base`` recovers exactly that commit.

    Two tempting alternatives are deliberately *not* used:

    * ``github.event.pull_request.base.sha`` (``PR_BASE_SHA``) is a snapshot of main
      taken when the PR was opened and is not refreshed when main advances. Diffing
      against it includes every file that unrelated PRs changed on main since then.
    * ``origin/main`` is fetched fresh on every (re-)run, while ``HEAD`` may be a
      merge commit that was created earlier. Files updated on main in between then
      look as if this PR reverted them.

    ``PR_BASE_SHA`` is only used as a last-resort fallback when no main ref exists
    locally (e.g. a shallow checkout).
    """
    for ref in ("origin/main", "main"):
        res = _run_git("merge-base", ref, "HEAD")
        if res.returncode == 0 and res.stdout.strip():
            return res.stdout.strip()

    pr_base_sha = os.environ.get("PR_BASE_SHA")
    if pr_base_sha:
        return pr_base_sha

    raise RuntimeError(
        "Could not determine the base ref: neither origin/main nor main exists "
        "and PR_BASE_SHA is not set."
    )


def get_changed_json_files(base_ref: str) -> list[str]:
    """Repo-relative paths of ``*.json`` files that differ between ``base_ref`` and ``HEAD``."""
    res = _run_git("diff", "--name-only", base_ref, "HEAD", "--", "*.json")
    if res.returncode != 0:
        raise RuntimeError(f"git diff failed with code {res.returncode}: {res.stderr}")
    return sorted(line.strip() for line in res.stdout.splitlines() if line.strip())


def show_file_at_ref(relative_path: str, ref: str) -> str | None:
    """Content of ``relative_path`` at ``ref``, or ``None`` if the file does not exist there."""
    res = _run_git("show", f"{ref}:{relative_path}")
    if res.returncode != 0:
        return None
    return res.stdout

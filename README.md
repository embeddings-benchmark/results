# Cached Results Branch

**⚠️ DO NOT MERGE THIS BRANCH**

This is an orphaned branch that serves as a data storage for pre-computed MTEB leaderboard results.

## Purpose

- Stores `__cached_results.json.gz` - compressed benchmark results for the MTEB leaderboard
- Reduces leaderboard build times by 100+ seconds by pre-computing results
- Automatically updated by the `generate_cached_results.yml` GitHub Actions workflow

## Contents

- `__cached_results.json.gz`: Gzipped JSON containing all model benchmark results
- Updated automatically when changes are pushed to the `main` branch

## Usage

The leaderboard application downloads this file to avoid re-computing results on every build. This branch is managed entirely by automation and should not be manually modified.
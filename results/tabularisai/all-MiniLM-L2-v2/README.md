# MTEB Submission: tabularisai/all-MiniLM-L2-v2

This directory contains the submission files for the MTEB leaderboard.

## Model Information

- Name: tabularisai/all-MiniLM-L2-v2
- Languages: eng-Latn
- Embedding Dimension: 384
- Number of Parameters: 15,600,000
- Memory Usage: 87 MB
- Maximum Context Length: 512 tokens
- Reference: https://huggingface.co/tabularisai/all-MiniLM-L2-v2

## Manual Submission Instructions

1. Fork the [results repository](https://github.com/embeddings-benchmark/results)
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/results.git
   cd results
   ```

3. Create a new branch:
   ```bash
   git checkout -b submit-tabularisai-all-MiniLM-L2-v2
   ```

4. Copy the contents of this submission directory to the appropriate location:
   ```bash
   mkdir -p results/tabularisai/all-MiniLM-L2-v2
   cp -r submission/* results/tabularisai/all-MiniLM-L2-v2/
   ```

5. Commit and push your changes:
   ```bash
   git add .
   git commit -m "Add results for tabularisai/all-MiniLM-L2-v2"
   git push origin submit-tabularisai-all-MiniLM-L2-v2
   ```

6. Go to https://github.com/embeddings-benchmark/results and create a pull request

7. Once merged, your results will appear on the leaderboard within a day

For more information, see the [MTEB documentation](https://github.com/embeddings-benchmark/mteb).

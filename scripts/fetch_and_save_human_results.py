#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MTEB Human Results Fetcher and Saver

Fetches human evaluation results from Argilla and saves them in MTEB format.

USAGE:
    Run this script from the repository root directory:
    
    cd your-repo/
    python scripts/fetch_and_save_human_results.py

REQUIREMENTS:
    - Set environment variables: ARGILLA_API_KEY and HF_TOKEN
    - Install dependencies: argilla, pandas, numpy, scikit-learn, scipy

OUTPUT:
    - Creates timestamped aggregate results in: results/Human/{YYYY_MM_DD}/
    - Updates individual annotator results in: results/Human/annotator_{id}/
    - Generates model_meta.json with annotator information

BEHAVIOR:
    - Fetches ALL completed annotations from Argilla
    - Creates new timestamped directory for aggregate results
    - Updates existing annotator directories and creates new ones
    - Recalculates inter-annotator agreement with all available data
"""

import argilla as rg
import json
import os
import pandas as pd
import numpy as np
import sklearn.metrics
import scipy.stats as stats
from collections import defaultdict
from sklearn.metrics import cohen_kappa_score
from pathlib import Path
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Configuration
ARGILLA_API_URL = "https://mteb-human-evaluation.hf.space"
# You'll need to set these environment variables or modify the script
ARGILLA_API_KEY = os.getenv("ARGILLA_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

# Task mapping from Argilla dataset names to MTEB task names (matching existing files)
TASK_MAPPING = {
    # Classification tasks
    "mteb-emotion-classification": "HUMEEmotionClassification",
    "mteb-tweet-sentiment-classification": "HUMETweetSentimentExtractionClassification", 
    "mteb-toxicity-classification": "HUMEToxicConversationsClassification",
    
    # Clustering tasks
    "mteb-wikicities-clustering": "HUMEWikiCitiesClustering",
    "mteb-arxiv-clustering": "HUMEArxivClusteringP2P",
    "mteb-reddit-clustering": "HUMERedditClusteringP2P",
    
    # STS tasks
    "mteb-stsbenchmark-sts": "HUMESTSBenchmark",
    "mteb-sickr-sts": "HUMESICK-R",
    "mteb-sts12-sts": "HUMESTS12",
    
    # Reranking tasks
    "mteb-core17-reranking": "HUMECore17InstructionReranking",
    "mteb-news21-reranking": "HUMENews21InstructionReranking",
    "mteb-robust04-reranking": "HUMERobust04InstructionReranking",
}

# Multilingual tasks that need special handling (multiple languages in one file)
MULTILINGUAL_TASKS = {
    # Multilingual classification - combines all languages into one file
    "HUMEMultilingualSentimentClassification": [
        "mteb-multilingual-sentiment-en-classification",
        "mteb-multilingual-sentiment-ar-classification", 
        "mteb-multilingual-sentiment-no-classification",
        "mteb-multilingual-sentiment-ru-classification"
    ],
    
    # Multilingual clustering - combines all languages into one file  
    "HUMESIB200ClusteringS2S": [
        "mteb-sib200-en-clustering",
        "mteb-sib200-ar-clustering",
        "mteb-sib200-da-clustering", 
        "mteb-sib200-ru-clustering"
    ],
    
    # Multilingual STS - combines all languages into one file
    "HUMESTS22": [
        "mteb-sts22-en-sts",
        "mteb-sts22-ar-sts",
        "mteb-sts22-ru-sts"
    ],
    
    # Multilingual reranking - combines all languages into one file
    "HUMEWikipediaRerankingMultilingual": [
        "mteb-wiki-en-reranking",
        "mteb-wiki-da-reranking",
        "mteb-wiki-no-reranking"
    ]
}

# Language code mapping for hf_subset values
LANGUAGE_MAPPING = {
    "en": "eng",
    "ar": "ara", 
    "no": "nor",
    "ru": "rus",
    "da": "dan",
    "eng": "eng_Latn",
    "arb": "arb_Arab", 
    "dan": "dan_Latn",
    "rus": "rus_Cyrl"
}

def initialize_argilla_client():
    """Initialize Argilla client with authentication"""
    if not ARGILLA_API_KEY or not HF_TOKEN:
        raise ValueError("Please set ARGILLA_API_KEY and HF_TOKEN environment variables")
    
    client = rg.Argilla(
        api_url=ARGILLA_API_URL,
        api_key=ARGILLA_API_KEY,
        headers={"Authorization": f"Bearer {HF_TOKEN}"}
    )
    return client

def extract_annotations(dataset_name, client):
    """Extract annotations from Argilla datasets based on the actual record structure"""

    # Get the dataset
    dataset = client.datasets(dataset_name)

    # Filter for completed records
    status_filter = rg.Query(filter=rg.Filter(("status", "==", "completed")))
    completed_records = dataset.records(status_filter)
    completed_records = dataset.records()  # no status filter

    records = []
    task_type = "unknown"  # Default

    # Process each record based on task type
    for record in completed_records:
        # Get metadata
        metadata = record.metadata
        # Process records based on task type
        if "sentiment" in dataset_name:
            question_name = "sentiment"
            task_type = "classification"

            for response_value in record.responses[question_name]:
                records.append({
                    "record_id": record.id,
                    "metadata": metadata,
                    "annotator": response_value.user_id if hasattr(response_value, "user_id") else "unknown",
                    "prediction": response_value.value.strip() if hasattr(response_value, "value") else str(response_value).strip(),
                    "gold": metadata.get("true_label", "unknown")
                })
        elif "emotion" in dataset_name:
            question_name = "emotion"
            task_type = "classification"

            for response_value in record.responses[question_name]:
                records.append({
                    "record_id": record.id,
                    "metadata": metadata,
                    "annotator": response_value.user_id if hasattr(response_value, "user_id") else "unknown",
                    "prediction": response_value.value.strip() if hasattr(response_value, "value") else str(response_value).strip(),
                    "gold": metadata.get("true_label", "unknown")
                })

        elif "toxicity" in dataset_name:
            question_name = "toxicity"
            task_type = "classification"

            for response_value in record.responses[question_name]:
                records.append({
                    "record_id": record.id,
                    "metadata": metadata,
                    "annotator": response_value.user_id if hasattr(response_value, "user_id") else "unknown",
                    "prediction": response_value.value.strip() if hasattr(response_value, "value") else str(response_value).strip(),
                    "gold": metadata.get("true_label", "unknown")
                })

        elif "clustering" in dataset_name:
            task_type = "clustering"
            question_name = "cluster_id"

            for response_value in record.responses[question_name]:
                records.append({
                    "record_id": record.id,
                    "metadata": metadata,
                    "annotator": response_value.user_id if hasattr(response_value, "user_id") else "unknown",
                    "prediction": response_value.value.strip() if hasattr(response_value, "value") else str(response_value).strip(),
                    "gold": metadata.get("true_cluster", "unknown")
                })

        elif "sts" in dataset_name:
            task_type = "sts"
            question_name = "similarity_score"

            for response_value in record.responses[question_name]:

                records.append({
                    "record_id": record.id,
                    "metadata": metadata,
                    "annotator": response_value.user_id if hasattr(response_value, "user_id") else "unknown",
                    "prediction": response_value.value,
                    "gold": float(metadata.get("true_score", 0.0))
                })

        elif "reranking" in dataset_name:
            task_type = "reranking"

            # Build gold vector
            gold = metadata.get("is_positive", [False] * 7)
            gold_binary = [1 if val else 0 for val in gold]

            # Group responses per annotator
            annotator_responses = {}
            for i in range(1, 8):
                question_name = f"doc{i}_relevant"

                for response_value in record.responses[question_name]:
                    ann = response_value.user_id if hasattr(response_value, "user_id") else "unknown"
                    if ann not in annotator_responses:
                        annotator_responses[ann] = [None] * 7
                    if response_value.value == "Relevant":
                        annotator_responses[ann][i-1] = 1
                    elif response_value.value == "Not Relevant":
                        annotator_responses[ann][i-1] = 0
            # Save one row per annotator
            for ann, pred in annotator_responses.items():
                records.append({
                    "record_id": record.id,
                    "metadata": metadata,
                    "annotator": ann,
                    "prediction": pred,
                    "gold": gold_binary
                })


    if not records:
        print(f"No annotations found or could not parse annotations for {dataset_name}")

    return pd.DataFrame(records), task_type

def evaluate_classification(df, dataset_name):
    """Evaluate classification tasks and return MTEB-compatible results"""
    if df.empty:
        return None
    
    results = {}

    # Calculate per-annotator metrics
    annotators = df["annotator"].unique()
    for annotator in annotators:
        annotator_df = df[df["annotator"] == annotator]

        try:
            unique_gold = annotator_df["gold"].nunique()
            unique_pred = annotator_df["prediction"].nunique()

            if unique_gold == 1 or unique_pred == 1:
                # Single-label case
                accuracy = sklearn.metrics.accuracy_score(
                    annotator_df["gold"], annotator_df["prediction"]
                )
                f1_macro = accuracy
                f1_weighted = accuracy
                precision = accuracy
                recall = accuracy
            else:
                # Multi-class case
                accuracy = sklearn.metrics.accuracy_score(
                    annotator_df["gold"], annotator_df["prediction"]
                )
                f1_macro = sklearn.metrics.f1_score(
                    annotator_df["gold"], annotator_df["prediction"], average="macro", zero_division=0
                )
                f1_weighted = sklearn.metrics.f1_score(
                    annotator_df["gold"], annotator_df["prediction"], average="weighted", zero_division=0
                )
                precision = sklearn.metrics.precision_score(
                    annotator_df["gold"], annotator_df["prediction"], average="macro", zero_division=0
                )
                recall = sklearn.metrics.recall_score(
                    annotator_df["gold"], annotator_df["prediction"], average="macro", zero_division=0
                )

            results[f"annotator_{annotator}"] = {
                "accuracy": accuracy,
                "f1": f1_macro,
                "f1_weighted": f1_weighted,
                "precision": precision,
                "recall": recall,
                "main_score": accuracy
            }

        except Exception as e:
            print(f"Error evaluating annotator {annotator}: {e}")
            results[f"annotator_{annotator}"] = {
                "accuracy": 0.0, "f1": 0.0, "f1_weighted": 0.0,
                "precision": 0.0, "recall": 0.0, "main_score": 0.0
            }

    # Calculate aggregated metrics (majority vote)
    if len(annotators) > 1:
        try:
            aggregated_df = df.groupby("record_id").agg({
                "gold": "first",
                "prediction": lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0]
            }).reset_index()

            unique_gold_agg = aggregated_df["gold"].nunique()
            unique_pred_agg = aggregated_df["prediction"].nunique()

            if unique_gold_agg == 1 or unique_pred_agg == 1:
                agg_accuracy = sklearn.metrics.accuracy_score(
                    aggregated_df["gold"], aggregated_df["prediction"]
                )
                agg_f1_macro = agg_accuracy
                agg_f1_weighted = agg_accuracy
                agg_precision = agg_accuracy
                agg_recall = agg_accuracy
            else:
                agg_accuracy = sklearn.metrics.accuracy_score(
                    aggregated_df["gold"], aggregated_df["prediction"]
                )
                agg_f1_macro = sklearn.metrics.f1_score(
                    aggregated_df["gold"], aggregated_df["prediction"], average="macro", zero_division=0
                )
                agg_f1_weighted = sklearn.metrics.f1_score(
                    aggregated_df["gold"], aggregated_df["prediction"], average="weighted", zero_division=0
                )
                agg_precision = sklearn.metrics.precision_score(
                    aggregated_df["gold"], aggregated_df["prediction"], average="macro", zero_division=0
                )
                agg_recall = sklearn.metrics.recall_score(
                    aggregated_df["gold"], aggregated_df["prediction"], average="macro", zero_division=0
                )

            results["aggregated"] = {
                "accuracy": agg_accuracy,
                "f1": agg_f1_macro,
                "f1_weighted": agg_f1_weighted,
                "precision": agg_precision,
                "recall": agg_recall,
                "main_score": agg_accuracy
            }
        except Exception as e:
            print(f"Aggregation failed for {dataset_name}: {e}")
            # Fallback to mean of individual scores
            valid_results = [r for r in results.values() if isinstance(r, dict) and "accuracy" in r]
            if valid_results:
                results["aggregated"] = {
                    "accuracy": np.mean([r["accuracy"] for r in valid_results]),
                    "f1": np.mean([r["f1"] for r in valid_results]),
                    "f1_weighted": np.mean([r["f1_weighted"] for r in valid_results]),
                    "precision": np.mean([r["precision"] for r in valid_results]),
                    "recall": np.mean([r["recall"] for r in valid_results]),
                    "main_score": np.mean([r["accuracy"] for r in valid_results])
                }
    else:
        # Single annotator case
        annotator = annotators[0]
        results["aggregated"] = results[f"annotator_{annotator}"].copy()

    # Calculate inter-annotator agreement if multiple annotators
    agreement_info = {
        "n_annotators": len(annotators),
        "n_items": df["record_id"].nunique(),
        "total_annotations": len(df)
    }
    
    if len(annotators) > 1:
        try:
            # Try Fleiss' kappa first
            try:
                from statsmodels.stats.inter_rater import fleiss_kappa

                # Reshape data to the format needed for Fleiss' kappa
                all_records = df["record_id"].unique()
                all_labels = sorted(df["prediction"].unique())

                # Create a table where rows are records and columns are categories
                category_table = []

                for record_id in all_records:
                    record_df = df[df["record_id"] == record_id]

                    # Count annotations per category
                    category_counts = [0] * len(all_labels)
                    for i, label in enumerate(all_labels):
                        category_counts[i] = sum(record_df["prediction"] == label)

                    category_table.append(category_counts)

                # Calculate Fleiss' kappa
                kappa = fleiss_kappa(np.array(category_table))
                
                # Kappa interpretation
                if kappa > 0.8:
                    interpretation = "Almost perfect"
                elif kappa > 0.6:
                    interpretation = "Substantial"
                elif kappa > 0.4:
                    interpretation = "Moderate"
                elif kappa > 0.2:
                    interpretation = "Fair"
                else:
                    interpretation = "Poor"

                agreement_info.update({
                    "metric": "fleiss_kappa",
                    "value": kappa,
                    "interpretation": interpretation
                })

            except (ImportError, ValueError) as e:
                # Fallback to pairwise Cohen's kappa
                kappa_scores = []
                percentage_agreements = []

                for i, ann1 in enumerate(annotators):
                    for j, ann2 in enumerate(annotators):
                        if i < j:  # Only consider unique pairs
                            try:
                                ann1_preds = df[df["annotator"] == ann1].set_index("record_id")["prediction"]
                                ann2_preds = df[df["annotator"] == ann2].set_index("record_id")["prediction"]

                                # Align predictions
                                common_records = ann1_preds.index.intersection(ann2_preds.index)
                                if len(common_records) > 0:
                                    kappa = sklearn.metrics.cohen_kappa_score(
                                        ann1_preds.loc[common_records],
                                        ann2_preds.loc[common_records]
                                    )
                                    if np.isfinite(kappa):
                                        kappa_scores.append(kappa)
                                    
                                    # Percentage agreement
                                    agreement = (ann1_preds.loc[common_records] == ann2_preds.loc[common_records]).mean()
                                    percentage_agreements.append(agreement)
                            except Exception as e:
                                continue

                if kappa_scores:
                    mean_kappa = np.mean(kappa_scores)
                    
                    # Kappa interpretation
                    if mean_kappa > 0.8:
                        interpretation = "Almost perfect"
                    elif mean_kappa > 0.6:
                        interpretation = "Substantial"
                    elif mean_kappa > 0.4:
                        interpretation = "Moderate"
                    elif mean_kappa > 0.2:
                        interpretation = "Fair"
                    else:
                        interpretation = "Poor"
                    
                    agreement_info.update({
                        "metric": "fleiss_kappa",
                        "value": mean_kappa,
                        "interpretation": interpretation,
                        "mean_pairwise_kappa": mean_kappa,
                        "mean_percentage_agreement": np.mean(percentage_agreements) if percentage_agreements else 0.0
                    })
        except Exception as e:
            print(f"Agreement calculation failed for {dataset_name}: {e}")

    # Format results to match MTEB structure
    scores_per_experiment = [
        {
            "accuracy": results[f"annotator_{annotator}"]["accuracy"],
            "f1": results[f"annotator_{annotator}"]["f1"],
            "f1_weighted": results[f"annotator_{annotator}"]["f1_weighted"]
        } for annotator in annotators
    ]
    
    mteb_format = {
        "dataset_revision": "human_evaluation",
        "task_name": dataset_name,
        "mteb_version": "1.18.0",
        "scores": {
            "test": [
                {
                    "accuracy": results["aggregated"]["accuracy"],
                    "f1": results["aggregated"]["f1"],
                    "f1_weighted": results["aggregated"]["f1_weighted"],
                    "precision": results["aggregated"]["precision"],
                    "recall": results["aggregated"]["recall"],
                    "main_score": results["aggregated"]["accuracy"],
                    "scores_per_experiment": scores_per_experiment,
                    "agreement": agreement_info,
                    "hf_subset": "default",
                    "languages": ["eng-Latn"]
                }
            ]
        },
        "evaluation_time": 0,
        "kg_co2_emissions": None
    }

    return mteb_format

def evaluate_clustering(df, dataset_name):
    """Evaluate clustering tasks and return MTEB-compatible results"""
    if df.empty:
        return None
    
    results = {}

    # Handle cluster ID conversion
    df["prediction"] = df["prediction"].astype(str)
    df["gold"] = df["gold"].astype(str)

    # Calculate per-annotator metrics
    annotators = df["annotator"].unique()
    for annotator in annotators:
        annotator_df = df[df["annotator"] == annotator]

        try:
            # Use sklearn's built-in label handling
            human_labels = annotator_df["prediction"].values
            gold_labels = annotator_df["gold"].values

            # Check for sufficient diversity
            if len(set(human_labels)) == 1 or len(set(gold_labels)) == 1:
                v_measure = 0.0
                ari = 0.0
                ami = 0.0
            else:
                v_measure = sklearn.metrics.v_measure_score(gold_labels, human_labels)
                ari = sklearn.metrics.adjusted_rand_score(gold_labels, human_labels)
                ami = sklearn.metrics.adjusted_mutual_info_score(gold_labels, human_labels)

            # MTEB compatible metrics
            results[f"annotator_{annotator}"] = {
                "v_measure": v_measure,
                "ari": ari,
                "ami": ami,
                "main_score": v_measure
            }

        except Exception as e:
            print(f"Error evaluating clustering for annotator {annotator}: {e}")
            results[f"annotator_{annotator}"] = {
                "v_measure": 0.0, "ari": 0.0, "ami": 0.0, "main_score": 0.0
            }

    # Calculate aggregated metrics by averaging across annotators
    if annotators.size > 0:
        valid_results = [r for r in results.values() if isinstance(r, dict) and "v_measure" in r]
        if valid_results:
            results["aggregated"] = {
                "v_measure": np.mean([r["v_measure"] for r in valid_results]),
                "ari": np.mean([r["ari"] for r in valid_results]),
                "ami": np.mean([r["ami"] for r in valid_results]),
                "main_score": np.mean([r["v_measure"] for r in valid_results])
            }
        else:
            results["aggregated"] = {"v_measure": 0.0, "ari": 0.0, "ami": 0.0, "main_score": 0.0}

    # Inter-annotator agreement for clustering
    agreement_info = {
        "n_annotators": len(annotators),
        "n_items": df["record_id"].nunique(),
        "total_annotations": len(df)
    }
    
    if len(annotators) > 1:
        try:
            # Calculate pairwise ARI between annotators
            pairwise_ari = []
            for i, ann1 in enumerate(annotators):
                for j, ann2 in enumerate(annotators):
                    if i < j:  # Only consider unique pairs
                        try:
                            ann1_preds = df[df["annotator"] == ann1].set_index("record_id")["prediction"]
                            ann2_preds = df[df["annotator"] == ann2].set_index("record_id")["prediction"]

                            # Align predictions
                            common_records = ann1_preds.index.intersection(ann2_preds.index)
                            if len(common_records) > 0:
                                ari = sklearn.metrics.adjusted_rand_score(
                                    ann1_preds.loc[common_records],
                                    ann2_preds.loc[common_records]
                                )
                                pairwise_ari.append(ari)
                        except Exception as e:
                            continue

            if pairwise_ari:
                agreement_info.update({
                    "metric": "mean_pairwise_ari",
                    "value": np.mean(pairwise_ari)
                })
        except Exception as e:
            print(f"Agreement calculation failed for clustering {dataset_name}: {e}")

    # Format to match MTEB structure
    scores_per_experiment = [
        {
            "v_measure": results[f"annotator_{annotator}"]["v_measure"],
            "ari": results[f"annotator_{annotator}"]["ari"],
            "ami": results[f"annotator_{annotator}"]["ami"]
        } for annotator in annotators
    ]
    
    mteb_format = {
        "dataset_revision": "human_evaluation",
        "task_name": dataset_name,
        "mteb_version": "1.18.0",
        "scores": {
            "test": [
                {
                    "v_measure": results["aggregated"]["v_measure"],
                    "ari": results["aggregated"]["ari"],
                    "ami": results["aggregated"]["ami"],
                    "main_score": results["aggregated"]["v_measure"],
                    "scores_per_experiment": scores_per_experiment,
                    "agreement": agreement_info,
                    "hf_subset": "default",
                    "languages": ["eng-Latn"]
                }
            ]
        },
        "evaluation_time": 0,
        "kg_co2_emissions": None
    }

    return mteb_format

def evaluate_sts(df, dataset_name):
    """Evaluate semantic textual similarity tasks and return MTEB-compatible results"""
    if df.empty:
        return None
    
    results = {}

    # Calculate per-annotator metrics
    annotators = df["annotator"].unique()
    for annotator in annotators:
        annotator_df = df[df["annotator"] == annotator]

        try:
            # Ensure numeric and clean data
            predictions = pd.to_numeric(annotator_df["prediction"], errors='coerce')
            gold_scores = pd.to_numeric(annotator_df["gold"], errors='coerce')

            # Remove NaN values
            valid_mask = ~(np.isnan(predictions) | np.isnan(gold_scores))
            predictions = predictions[valid_mask]
            gold_scores = gold_scores[valid_mask]

            if len(predictions) > 1 and len(set(predictions)) > 1 and len(set(gold_scores)) > 1:
                # Calculate correlation metrics
                spearman = stats.spearmanr(gold_scores, predictions)[0]
                pearson = stats.pearsonr(gold_scores, predictions)[0]
                mse = sklearn.metrics.mean_squared_error(gold_scores, predictions)

                # Handle NaN correlations
                spearman = spearman if np.isfinite(spearman) else 0.0
                pearson = pearson if np.isfinite(pearson) else 0.0
            else:
                spearman = pearson = mse = 0.0

            results[f"annotator_{annotator}"] = {
                "spearman": spearman,
                "pearson": pearson,
                "mse": mse,
                "main_score": spearman
            }

        except Exception as e:
            print(f"Error evaluating STS for annotator {annotator}: {e}")
            results[f"annotator_{annotator}"] = {
                "spearman": 0.0, "pearson": 0.0, "mse": 0.0, "main_score": 0.0
            }

    # Calculate aggregated metrics (average score)
    if len(annotators) > 1:
        try:
            aggregated_df = df.groupby("record_id").agg({
                "gold": "first",
                "prediction": "mean"  # Average score across annotators
            }).reset_index()

            agg_predictions = pd.to_numeric(aggregated_df["prediction"], errors='coerce')
            agg_gold = pd.to_numeric(aggregated_df["gold"], errors='coerce')

            valid_mask = ~(np.isnan(agg_predictions) | np.isnan(agg_gold))
            agg_predictions = agg_predictions[valid_mask]
            agg_gold = agg_gold[valid_mask]

            if len(agg_predictions) > 1 and len(set(agg_predictions)) > 1 and len(set(agg_gold)) > 1:
                agg_spearman = stats.spearmanr(agg_gold, agg_predictions)[0]
                agg_pearson = stats.pearsonr(agg_gold, agg_predictions)[0]
                agg_mse = sklearn.metrics.mean_squared_error(agg_gold, agg_predictions)

                agg_spearman = agg_spearman if np.isfinite(agg_spearman) else 0.0
                agg_pearson = agg_pearson if np.isfinite(agg_pearson) else 0.0
            else:
                agg_spearman = agg_pearson = agg_mse = 0.0

            results["aggregated"] = {
                "spearman": agg_spearman,
                "pearson": agg_pearson,
                "mse": agg_mse,
                "main_score": agg_spearman  # MTEB uses spearman as the main score
            }
        except Exception as e:
            print(f"Aggregation failed for STS {dataset_name}: {e}")
            # Fallback to mean of individual scores
            valid_results = [r for r in results.values() if isinstance(r, dict) and "spearman" in r]
            if valid_results:
                results["aggregated"] = {
                    "spearman": np.mean([r["spearman"] for r in valid_results]),
                    "pearson": np.mean([r["pearson"] for r in valid_results]),
                    "mse": np.mean([r["mse"] for r in valid_results]),
                    "main_score": np.mean([r["spearman"] for r in valid_results])
                }
    else:
        # Single annotator
        annotator = annotators[0]
        results["aggregated"] = results[f"annotator_{annotator}"].copy()

    # Calculate inter-annotator agreement
    agreement_info = {
        "n_annotators": len(annotators),
        "n_items": df["record_id"].nunique(),
        "total_annotations": len(df)
    }
    
    if len(annotators) > 1:
        try:
            # Calculate pairwise correlations between annotators
            pairwise_spearman = []

            for i, ann1 in enumerate(annotators):
                for j, ann2 in enumerate(annotators):
                    if i < j:  # Only consider unique pairs
                        try:
                            ann1_scores = df[df["annotator"] == ann1].set_index("record_id")["prediction"]
                            ann2_scores = df[df["annotator"] == ann2].set_index("record_id")["prediction"]

                            # Align scores
                            common_records = ann1_scores.index.intersection(ann2_scores.index)
                            if len(common_records) > 0:
                                ann1_vals = pd.to_numeric(ann1_scores.loc[common_records], errors='coerce')
                                ann2_vals = pd.to_numeric(ann2_scores.loc[common_records], errors='coerce')

                                valid_mask = ~(np.isnan(ann1_vals) | np.isnan(ann2_vals))
                                ann1_vals = ann1_vals[valid_mask]
                                ann2_vals = ann2_vals[valid_mask]

                                if len(ann1_vals) > 1 and len(set(ann1_vals)) > 1 and len(set(ann2_vals)) > 1:
                                    corr = stats.spearmanr(ann1_vals, ann2_vals)[0]
                                    if np.isfinite(corr):
                                        pairwise_spearman.append(corr)
                        except Exception as e:
                            continue

            if pairwise_spearman:
                agreement_info.update({
                    "metric": "mean_pairwise_spearman",
                    "value": np.mean(pairwise_spearman)
                })

        except Exception as e:
            print(f"Agreement calculation failed for STS {dataset_name}: {e}")

    # Format to match MTEB structure
    scores_per_experiment = [
        {
            "spearman": results[f"annotator_{annotator}"]["spearman"],
            "pearson": results[f"annotator_{annotator}"]["pearson"],
            "mse": results[f"annotator_{annotator}"]["mse"]
        } for annotator in annotators
    ]
    
    mteb_format = {
        "dataset_revision": "human_evaluation",
        "task_name": dataset_name,
        "mteb_version": "1.18.0",
        "scores": {
            "test": [
                {
                    "spearman": results["aggregated"]["spearman"],
                    "pearson": results["aggregated"]["pearson"],
                    "mse": results["aggregated"]["mse"],
                    "main_score": results["aggregated"]["spearman"],
                    "scores_per_experiment": scores_per_experiment,
                    "agreement": agreement_info,
                    "hf_subset": "default",
                    "languages": ["eng-Latn"]
                }
            ]
        },
        "evaluation_time": 0,
        "kg_co2_emissions": None
    }

    return mteb_format

def evaluate_reranking(df, dataset_name):
    """Evaluate reranking tasks and return MTEB-compatible results"""
    if df.empty:
        return None
    
    from sklearn.metrics import average_precision_score

    results = {}

    # Calculate per-annotator metrics
    annotators = df["annotator"].unique()
    for annotator in annotators:
        annotator_df = df[df["annotator"] == annotator]

        mrr_scores = []
        map_scores = []
        ndcg_scores = []

        for _, row in annotator_df.iterrows():
            try:
                human_judgments = row["prediction"]  # List of relevance scores
                gold_relevance = row["gold"]         # Binary ground truth

                if not isinstance(human_judgments, list) or not isinstance(gold_relevance, list):
                    continue

                if len(human_judgments) != len(gold_relevance):
                    continue

                # Convert to numpy for easier handling
                human_scores = np.array(human_judgments, dtype=float)
                is_relevant = np.array(gold_relevance, dtype=bool)

                # Create ranking (higher scores = better rank)
                pred_ranking = np.argsort(-human_scores)

                # 1. MRR@10
                mrr_at_10 = 0.0
                for rank, doc_idx in enumerate(pred_ranking[:10]):
                    if is_relevant[doc_idx]:
                        mrr_at_10 = 1.0 / (rank + 1)
                        break
                mrr_scores.append(mrr_at_10)

                # 2. MAP
                map_score = average_precision_score(is_relevant, human_scores)
                map_scores.append(map_score)

                # 3. nDCG@10
                relevance_at_10 = [int(is_relevant[i]) for i in pred_ranking[:10]]
                ideal_relevance = sorted(is_relevant.astype(int), reverse=True)[:10]

                def dcg_at_k(relevance, k):
                    return sum((2**r - 1) / np.log2(i + 2) for i, r in enumerate(relevance[:k]))

                dcg_10 = dcg_at_k(relevance_at_10, 10)
                idcg_10 = dcg_at_k(ideal_relevance, 10)

                ndcg_10 = dcg_10 / idcg_10 if idcg_10 > 0 else 0.0
                ndcg_scores.append(ndcg_10)

            except Exception as e:
                print(f"Error processing reranking record: {e}")
                continue

        # Store metrics
        results[f"annotator_{annotator}"] = {
            "map": np.mean(map_scores) if map_scores else 0.0,
            "mrr@10": np.mean(mrr_scores) if mrr_scores else 0.0,
            "ndcg@10": np.mean(ndcg_scores) if ndcg_scores else 0.0,
            "main_score": np.mean(map_scores) if map_scores else 0.0
        }

    # Calculate aggregated metrics by averaging across annotators
    if annotators.size > 0:
        valid_results = [r for r in results.values() if isinstance(r, dict) and "map" in r]
        if valid_results:
            results["aggregated"] = {
                "map": np.mean([r["map"] for r in valid_results]),
                "mrr@10": np.mean([r["mrr@10"] for r in valid_results]),
                "ndcg@10": np.mean([r["ndcg@10"] for r in valid_results]),
                "main_score": np.mean([r["map"] for r in valid_results])
            }
        else:
            results["aggregated"] = {"map": 0.0, "mrr@10": 0.0, "ndcg@10": 0.0, "main_score": 0.0}

    # Calculate inter-annotator agreement
    agreement_info = {
        "n_annotators": len(annotators),
        "n_items": df["record_id"].nunique(),
        "total_annotations": len(df)
    }
    
    if len(annotators) > 1:
        try:
            # Multiple agreement measures for ranking data
            spearman_scores = []
            kendall_scores = []
            binary_kappa_scores = []

            for i, ann1 in enumerate(annotators):
                for j, ann2 in enumerate(annotators):
                    if i < j:
                        try:
                            ann1_data = df[df["annotator"] == ann1].set_index("record_id")["prediction"]
                            ann2_data = df[df["annotator"] == ann2].set_index("record_id")["prediction"]
                            common_records = ann1_data.index.intersection(ann2_data.index)

                            for record_id in common_records:
                                j1 = ann1_data.loc[record_id]
                                j2 = ann2_data.loc[record_id]

                                if isinstance(j1, list) and isinstance(j2, list) and len(j1) == len(j2):
                                    # Spearman correlation on relevance scores
                                    spearman, _ = stats.spearmanr(j1, j2)
                                    if np.isfinite(spearman):
                                        spearman_scores.append(spearman)

                                    # Kendall's τ on relevance scores
                                    kendall, _ = stats.kendalltau(j1, j2)
                                    if np.isfinite(kendall):
                                        kendall_scores.append(kendall)

                                    # Cohen's κ on binary relevance (relevant vs not relevant)
                                    binary_j1 = [1 if x > 0 else 0 for x in j1]
                                    binary_j2 = [1 if x > 0 else 0 for x in j2]
                                    kappa = cohen_kappa_score(binary_j1, binary_j2)
                                    if np.isfinite(kappa):
                                        binary_kappa_scores.append(kappa)

                        except Exception as e:
                            print(f"Reranking agreement calculation failed for {ann1}-{ann2}: {e}")
                            continue

            if spearman_scores:
                agreement_info.update({
                    "mean_spearman": np.mean(spearman_scores),
                    "mean_kendall_tau": np.mean(kendall_scores) if kendall_scores else 0.0,
                    "mean_binary_kappa": np.mean(binary_kappa_scores) if binary_kappa_scores else 0.0,
                    "spearman_std": np.std(spearman_scores) if len(spearman_scores) > 1 else 0.0,
                    "n_comparisons": len(spearman_scores)
                })
        except Exception as e:
            print(f"Agreement calculation failed for reranking {dataset_name}: {e}")

    # Format to match MTEB structure
    scores_per_experiment = [
        {
            "map": results[f"annotator_{annotator}"]["map"],
            "mrr@10": results[f"annotator_{annotator}"]["mrr@10"],
            "ndcg@10": results[f"annotator_{annotator}"]["ndcg@10"]
        } for annotator in annotators
    ]
    
    mteb_format = {
        "dataset_revision": "human_evaluation",
        "task_name": dataset_name,
        "mteb_version": "1.18.0",
        "scores": {
            "test": [
                {
                    "map": results["aggregated"]["map"],
                    "mrr@10": results["aggregated"]["mrr@10"],
                    "ndcg@10": results["aggregated"]["ndcg@10"],
                    "main_score": results["aggregated"]["map"],
                    "scores_per_experiment": scores_per_experiment,
                    "agreement": agreement_info,
                    "hf_subset": "default",
                    "languages": ["eng-Latn"]
                }
            ]
        },
        "evaluation_time": 0,
        "kg_co2_emissions": None
    }

    return mteb_format

# Multilingual handling is now integrated into the main processing loop

def save_human_result(result, df, output_dir="results/Human"):
    """Save human evaluation result in the exact format as existing files"""
    if result is None:
        return False
    
    # Create output directory structure - MAIN AGGREGATED RESULTS
    timestamp = datetime.now().strftime("%Y_%m_%d")
    output_path = Path(output_dir) / timestamp
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Save the main aggregated result
    task_name = result["task_name"]
    filename = f"{task_name}.json"
    filepath = output_path / filename
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        print(f"  Saved aggregated: {filepath}")
        
        # Save individual annotator results
        annotators = df["annotator"].unique()
        for annotator in annotators:
            if annotator != "unknown":
                # Create individual annotator directory
                annotator_dir = Path(output_dir) / f"annotator_{annotator}"
                annotator_dir.mkdir(parents=True, exist_ok=True)
                
                # Get this annotator's data
                annotator_df = df[df["annotator"] == annotator]
                
                # Create individual annotator result
                # Individual files show only that annotator's performance
                
                individual_result = {
                    "dataset_revision": "human_evaluation",
                    "task_name": task_name,
                    "mteb_version": "1.18.0",
                    "scores": {
                        "test": []
                    },
                    "evaluation_time": 0,
                    "kg_co2_emissions": None
                }
                
                # For multilingual tasks, only include languages this annotator worked on
                if 'language' in annotator_df.columns:
                    # Multilingual task - process each language this annotator worked on
                    for language in annotator_df['language'].unique():
                        lang_df = annotator_df[annotator_df['language'] == language]
                        if not lang_df.empty:
                            # Evaluate just this annotator's data for this language
                            individual_test_entry = create_individual_annotator_entry(lang_df, task_name, language)
                            if individual_test_entry:
                                individual_result["scores"]["test"].append(individual_test_entry)
                else:
                    # Regular task - single entry
                    individual_test_entry = create_individual_annotator_entry(annotator_df, task_name)
                    if individual_test_entry:
                        individual_result["scores"]["test"].append(individual_test_entry)
                
                # Save individual annotator result
                individual_filepath = annotator_dir / filename
                with open(individual_filepath, 'w', encoding='utf-8') as f:
                    json.dump(individual_result, f, indent=2, ensure_ascii=False)
                
                print(f"  Saved individual: {individual_filepath}")
        
        return True
    
    except Exception as e:
        print(f"  ❌ Error saving {filepath}: {e}")
        return False

def create_individual_annotator_entry(annotator_df, task_name, language=None):
    """Create individual test entry for a single annotator"""
    
    # Determine task type
    if "Classification" in task_name:
        task_type = "classification"
    elif "Clustering" in task_name:
        task_type = "clustering"
    elif "STS" in task_name or "SICK" in task_name:
        task_type = "sts"
    elif "Reranking" in task_name:
        task_type = "reranking"
    else:
        return None
    
    try:
        if task_type == "classification":
            accuracy = sklearn.metrics.accuracy_score(annotator_df["gold"], annotator_df["prediction"])
            f1_macro = sklearn.metrics.f1_score(annotator_df["gold"], annotator_df["prediction"], average="macro", zero_division=0)
            f1_weighted = sklearn.metrics.f1_score(annotator_df["gold"], annotator_df["prediction"], average="weighted", zero_division=0)
            precision = sklearn.metrics.precision_score(annotator_df["gold"], annotator_df["prediction"], average="macro", zero_division=0)
            recall = sklearn.metrics.recall_score(annotator_df["gold"], annotator_df["prediction"], average="macro", zero_division=0)
            
            entry = {
                "accuracy": accuracy,
                "f1": f1_macro,
                "f1_weighted": f1_weighted,
                "precision": precision,
                "recall": recall,
                "main_score": accuracy
            }
            
        elif task_type == "clustering":
            human_labels = annotator_df["prediction"].astype(str).values
            gold_labels = annotator_df["gold"].astype(str).values
            
            if len(set(human_labels)) == 1 or len(set(gold_labels)) == 1:
                v_measure = ari = ami = 0.0
            else:
                v_measure = sklearn.metrics.v_measure_score(gold_labels, human_labels)
                ari = sklearn.metrics.adjusted_rand_score(gold_labels, human_labels)
                ami = sklearn.metrics.adjusted_mutual_info_score(gold_labels, human_labels)
            
            entry = {
                "v_measure": v_measure,
                "ari": ari,
                "ami": ami,
                "main_score": v_measure
            }
            
        elif task_type == "sts":
            predictions = pd.to_numeric(annotator_df["prediction"], errors='coerce')
            gold_scores = pd.to_numeric(annotator_df["gold"], errors='coerce')
            
            valid_mask = ~(np.isnan(predictions) | np.isnan(gold_scores))
            predictions = predictions[valid_mask]
            gold_scores = gold_scores[valid_mask]
            
            if len(predictions) > 1 and len(set(predictions)) > 1 and len(set(gold_scores)) > 1:
                spearman = stats.spearmanr(gold_scores, predictions)[0]
                pearson = stats.pearsonr(gold_scores, predictions)[0]
                mse = sklearn.metrics.mean_squared_error(gold_scores, predictions)
                
                spearman = spearman if np.isfinite(spearman) else 0.0
                pearson = pearson if np.isfinite(pearson) else 0.0
            else:
                spearman = pearson = mse = 0.0
            
            entry = {
                "spearman": spearman,
                "pearson": pearson,
                "mse": mse,
                "main_score": spearman
            }
            
        elif task_type == "reranking":
            from sklearn.metrics import average_precision_score
            
            map_scores = []
            mrr_scores = []
            ndcg_scores = []
            
            for _, row in annotator_df.iterrows():
                human_judgments = row["prediction"]
                gold_relevance = row["gold"]
                
                if isinstance(human_judgments, list) and isinstance(gold_relevance, list) and len(human_judgments) == len(gold_relevance):
                    human_scores = np.array(human_judgments, dtype=float)
                    is_relevant = np.array(gold_relevance, dtype=bool)
                    
                    pred_ranking = np.argsort(-human_scores)
                    
                    # MRR@10
                    mrr_at_10 = 0.0
                    for rank, doc_idx in enumerate(pred_ranking[:10]):
                        if is_relevant[doc_idx]:
                            mrr_at_10 = 1.0 / (rank + 1)
                            break
                    mrr_scores.append(mrr_at_10)
                    
                    # MAP
                    map_score = average_precision_score(is_relevant, human_scores)
                    map_scores.append(map_score)
                    
                    # nDCG@10
                    relevance_at_10 = [int(is_relevant[i]) for i in pred_ranking[:10]]
                    ideal_relevance = sorted(is_relevant.astype(int), reverse=True)[:10]
                    
                    def dcg_at_k(relevance, k):
                        return sum((2**r - 1) / np.log2(i + 2) for i, r in enumerate(relevance[:k]))
                    
                    dcg_10 = dcg_at_k(relevance_at_10, 10)
                    idcg_10 = dcg_at_k(ideal_relevance, 10)
                    
                    ndcg_10 = dcg_10 / idcg_10 if idcg_10 > 0 else 0.0
                    ndcg_scores.append(ndcg_10)
            
            entry = {
                "map": np.mean(map_scores) if map_scores else 0.0,
                "mrr@10": np.mean(mrr_scores) if mrr_scores else 0.0,
                "ndcg@10": np.mean(ndcg_scores) if ndcg_scores else 0.0,
                "main_score": np.mean(map_scores) if map_scores else 0.0
            }
        
        # Add language-specific fields
        if language:
            # Multilingual task
            entry["hf_subset"] = language
            if language in ["eng", "eng_Latn", "en"]:
                entry["languages"] = ["eng-Latn"]
            elif language in ["ara", "arb_Arab", "ar"]:
                entry["languages"] = ["ara-Arab"]
            elif language in ["nor", "no"]:
                entry["languages"] = ["nor-Latn"]
            elif language in ["rus", "rus_Cyrl", "ru"]:
                entry["languages"] = ["rus-Cyrl"]
            elif language in ["dan_Latn", "da"]:
                entry["languages"] = ["dan-Latn"]
        else:
            # Regular task
            entry["hf_subset"] = "default"
            entry["languages"] = ["eng-Latn"]
        
        return entry
        
    except Exception as e:
        print(f"Error creating individual entry: {e}")
        return None

def create_model_meta(output_dir="results/Human", annotator_dirs=None):
    """Create model_meta.json file matching the existing format"""
    timestamp = datetime.now().strftime("%Y_%m_%d")
    
    # Create model_meta for main aggregated directory
    output_path = Path(output_dir) / timestamp
    
    model_meta = {
        "name": "Human Performance",
        "revision": "human_evaluation",
        "release_date": timestamp.replace("_", "-"),
        "languages": None,
        "n_parameters": None,
        "memory_usage_mb": None,
        "max_tokens": None,
        "embed_dim": None,
        "license": None,
        "open_weights": False,
        "public_training_code": None,
        "public_training_data": None,
        "framework": ["Human"],
        "reference": "MTEB Human Benchmark Evaluation",
        "similarity_fn_name": None,
        "use_instructions": False,
        "training_datasets": None,
        "adapted_from": None,
        "superseded_by": None,
        "is_cross_encoder": None,
        "modalities": ["text"],
        "loader": "HumanAnnotator"
    }
    
    filepath = output_path / "model_meta.json"
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(model_meta, f, indent=2, ensure_ascii=False)
        
        print(f"  Saved model metadata: {filepath}")
        
        # Also create model_meta.json for each individual annotator directory
        if annotator_dirs:
            for annotator_id in annotator_dirs:
                annotator_dir = Path(output_dir) / f"annotator_{annotator_id}"
                if annotator_dir.exists():
                    individual_meta = model_meta.copy()
                    individual_meta["name"] = f"Human Performance - Annotator {annotator_id}"
                    individual_meta["reference"] = f"MTEB Human Benchmark Evaluation - Individual Annotator {annotator_id}"
                    
                    individual_filepath = annotator_dir / "model_meta.json"
                    with open(individual_filepath, 'w', encoding='utf-8') as f:
                        json.dump(individual_meta, f, indent=2, ensure_ascii=False)
                    
                    print(f"  Saved individual model metadata: {individual_filepath}")
        
        return True
    
    except Exception as e:
        print(f"  ❌ Error saving model metadata: {e}")
        return False

def verify_output_format(result_file_path):
    """Verify that generated files match the exact format of existing human results"""
    try:
        with open(result_file_path, 'r') as f:
            result = json.load(f)
        
        # Check required top-level fields
        required_fields = ["dataset_revision", "task_name", "mteb_version", "scores", "evaluation_time", "kg_co2_emissions"]
        for field in required_fields:
            if field not in result:
                print(f"  ❌ Missing required field: {field}")
                return False
        
        # Check scores structure
        if "test" not in result["scores"] or not isinstance(result["scores"]["test"], list):
            print(f"  ❌ Invalid scores structure")
            return False
        
        test_scores = result["scores"]["test"][0]
        
        # Check required test score fields
        required_test_fields = ["main_score", "scores_per_experiment", "agreement", "hf_subset", "languages"]
        for field in required_test_fields:
            if field not in test_scores:
                print(f"  ❌ Missing required test field: {field}")
                return False
        
        # Check agreement structure
        agreement = test_scores["agreement"]
        required_agreement_fields = ["n_annotators", "n_items", "total_annotations"]
        for field in required_agreement_fields:
            if field not in agreement:
                print(f"  ❌ Missing required agreement field: {field}")
                return False
        
        print(f"  Format validation passed")
        return True
        
    except Exception as e:
        print(f"  ❌ Format validation failed: {e}")
        return False

def main():
    """Main function to fetch and save all human results"""
    print("🚀 MTEB Human Results Fetcher")
    print("=" * 50)
    print("📊 Fetching human evaluation results from Argilla")
    print("📁 Creating timestamped aggregate results")
    print("👥 Updating individual annotator directories")
    print("� RecalHculating inter-annotator agreement")
    print("=" * 50)
    
    # Initialize Argilla client
    try:
        client = initialize_argilla_client()
        print("Connected to Argilla")
    except Exception as e:
        print(f"❌ Failed to connect to Argilla: {e}")
        return
    
    # Process all datasets (including multilingual)
    results_saved = 0
    all_annotator_ids = set()
    processed_multilingual = set()
    
    # First, process regular datasets
    for argilla_dataset, mteb_task_name in TASK_MAPPING.items():
        print(f"\n📁 Processing: {argilla_dataset} -> {mteb_task_name}")
        
        try:
            df, task_type = extract_annotations(argilla_dataset, client)
            
            if df.empty:
                print(f"  ⚠️ No annotations found for {argilla_dataset}")
                continue
            
            print(f"  📊 Found {len(df)} annotations from {df['annotator'].nunique()} annotators")
            
            # Collect annotator IDs
            annotators = df["annotator"].unique()
            for annotator in annotators:
                if annotator != "unknown":
                    all_annotator_ids.add(annotator)
            
            # Evaluate and save
            result = None
            if task_type == "classification":
                result = evaluate_classification(df, mteb_task_name)
            elif task_type == "clustering":
                result = evaluate_clustering(df, mteb_task_name)
            elif task_type == "sts":
                result = evaluate_sts(df, mteb_task_name)
            elif task_type == "reranking":
                result = evaluate_reranking(df, mteb_task_name)
            
            if result and save_human_result(result, df):
                results_saved += 1
            
        except Exception as e:
            print(f"  ❌ Error processing {argilla_dataset}: {e}")
            continue
    
    # Process multilingual datasets - combine multiple languages into single files
    for mteb_task_name, argilla_datasets in MULTILINGUAL_TASKS.items():
        if mteb_task_name in processed_multilingual:
            continue
            
        print(f"\n📁 Processing multilingual: {mteb_task_name}")
        
        try:
            test_entries = []
            combined_df_for_annotators = pd.DataFrame()
            task_type = "unknown"
            
            # Process in the same order as the original data (not alphabetical)
            for argilla_dataset in argilla_datasets:
                print(f"  🌍 Language variant: {argilla_dataset}")
                df, current_task_type = extract_annotations(argilla_dataset, client)
                
                if df.empty:
                    continue
                    
                task_type = current_task_type
                
                # Determine language codes based on dataset name
                if "-en-" in argilla_dataset:
                    hf_subset = "eng" if "sentiment" in argilla_dataset else "eng_Latn" if "sib200" in argilla_dataset else "en"
                    languages = ["eng-Latn"]
                elif "-ar-" in argilla_dataset:
                    hf_subset = "ara" if "sentiment" in argilla_dataset else "arb_Arab" if "sib200" in argilla_dataset else "ar"
                    languages = ["ara-Arab"]
                elif "-no-" in argilla_dataset:
                    hf_subset = "nor"
                    languages = ["nor-Latn"]
                elif "-ru-" in argilla_dataset:
                    hf_subset = "rus" if "sentiment" in argilla_dataset else "rus_Cyrl" if "sib200" in argilla_dataset else "ru"
                    languages = ["rus-Cyrl"]
                elif "-da-" in argilla_dataset:
                    hf_subset = "dan_Latn"
                    languages = ["dan-Latn"]
                else:
                    continue
                
                # Collect annotator IDs
                for annotator in df["annotator"].unique():
                    if annotator != "unknown":
                        all_annotator_ids.add(annotator)
                
                # Add language info for annotator tracking
                df['language'] = hf_subset
                combined_df_for_annotators = pd.concat([combined_df_for_annotators, df], ignore_index=True)
                
                # Evaluate this language
                lang_result = None
                if task_type == "classification":
                    lang_result = evaluate_classification(df, mteb_task_name)
                elif task_type == "clustering":
                    lang_result = evaluate_clustering(df, mteb_task_name)
                elif task_type == "sts":
                    lang_result = evaluate_sts(df, mteb_task_name)
                elif task_type == "reranking":
                    lang_result = evaluate_reranking(df, mteb_task_name)
                
                if lang_result and "scores" in lang_result:
                    test_entry = lang_result["scores"]["test"][0].copy()
                    test_entry["hf_subset"] = hf_subset
                    test_entry["languages"] = languages
                    
                    # For multilingual tasks: only the FIRST entry (usually English) gets full structure
                    # Other language entries get only basic metrics (no scores_per_experiment or agreement)
                    if len(test_entries) > 0:  # Not the first entry
                        # Remove scores_per_experiment and agreement for non-first entries
                        if "scores_per_experiment" in test_entry:
                            del test_entry["scores_per_experiment"]
                        if "agreement" in test_entry:
                            del test_entry["agreement"]
                    
                    test_entries.append(test_entry)
            
            if test_entries:
                # Create multilingual result
                multilingual_result = {
                    "dataset_revision": "human_evaluation",
                    "task_name": mteb_task_name,
                    "mteb_version": "1.18.0",
                    "scores": {
                        "test": test_entries
                    },
                    "evaluation_time": 0,
                    "kg_co2_emissions": None
                }
                
                if save_human_result(multilingual_result, combined_df_for_annotators):
                    results_saved += 1
                    processed_multilingual.add(mteb_task_name)
            
        except Exception as e:
            print(f"  ❌ Error processing multilingual {mteb_task_name}: {e}")
            continue
    
    # Create model metadata
    create_model_meta(annotator_dirs=all_annotator_ids)
    
    print(f"\n" + "=" * 50)
    print(f"Completed successfully!")
    print(f"📊 Saved {results_saved}/{total_datasets} datasets")
    print(f"📁 Results saved in: results/Human/{datetime.now().strftime('%Y_%m_%d')}/")
    print(f"🔄 Files are in MTEB format and ready for analysis")

if __name__ == "__main__":
    main()
"""
PAPR Holographic Model Metadata for MTEB

This module provides the MTEB model metadata for papr-ai/papr-holo-1.0,
a proprietary multi-stage retrieval system with holographic transforms.

Note: This is a metadata-only registration. The model weights are proprietary
and not publicly available. Results were submitted separately to the MTEB
results repository.

For inquiries about the model: shawkat@papr.ai
"""

from __future__ import annotations

from mteb.models import ModelMeta


# Model metadata for MTEB registration (metadata-only, no loader)
papr_holo_1_0 = ModelMeta(
    loader=None,  # Proprietary model - no public loader
    name="papr-ai/papr-holo-1.0",
    languages=["eng-Latn"],
    open_weights=False,
    revision="1",
    release_date="2026-01-02",
    n_parameters=4_600_000_000,  
    memory_usage_mb=10000,
    embed_dim=2560,
    license=None,
    max_tokens=8192,
    reference="https://papr.ai",
    similarity_fn_name=None,  # Custom similarity implementation
    framework=["PyTorch"],
    use_instructions=False,
    public_training_code=None,
    public_training_data=None,
    training_datasets=None,
)

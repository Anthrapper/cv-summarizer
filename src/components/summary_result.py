from dataclasses import dataclass
from typing import Optional


@dataclass
class SummaryResult:
    """Data class for summary results."""
    summary: str
    model_used: str
    processing_time: float
    success: bool
    error: Optional[str] = None
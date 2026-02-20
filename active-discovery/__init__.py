"""
Active Discovery Module — APD-driven hydrogen line beacon.

Combines the Hydrogen Line Beacon (HLB) with Active Protocol Discovery (APD)
for sequential hypothesis testing of radio-frequency anomaly responses.
"""

from .active_beacon import ActiveBeacon
from .probe_library import ProbeLibrary, ProbeType
from .response_analyzer import ResponseAnalyzer
from .config import APDConfig

__all__ = [
    "ActiveBeacon",
    "ProbeLibrary",
    "ProbeType",
    "ResponseAnalyzer",
    "APDConfig",
]

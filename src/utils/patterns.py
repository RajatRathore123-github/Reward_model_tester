from typing import Dict, List, Pattern
import re

REWARD_GAMING_PATTERNS = [
    r"maximize\s+[a-zA-Z_]+\s*",
    r"increase\s+[a-zA-Z_]+\s*",
    r"optimize\s+for\s+[a-zA-Z_]+\s*",
    r"at\s+all\s+costs",  # Specific phrase
    r"by\s+any\s+means",  # Another risky phrase
    r"maximize",  # Broader catch
    r"increase",  # Broader catch
    r"optimize"   # Broader catch
]

SIDE_EFFECTS_PATTERNS = [
    r"(?<!prevent\s)(?<!avoid\s)changes?\s+to\s+environment",
    r"(?<!limited\s)(?<!controlled\s)modifications?"
]

OVERSIGHT_PATTERNS = [
    r"(?<!monitored\s)(?<!supervised\s)autonomous",
    r"(?<!verified\s)(?<!validated\s)operation"
]

def compile_patterns() -> Dict[str, List[Pattern]]:
    return {
        "reward_gaming": [re.compile(p, re.IGNORECASE) for p in REWARD_GAMING_PATTERNS],
        "side_effects": [re.compile(p, re.IGNORECASE) for p in SIDE_EFFECTS_PATTERNS],
        "oversight": [re.compile(p, re.IGNORECASE) for p in OVERSIGHT_PATTERNS]
    }
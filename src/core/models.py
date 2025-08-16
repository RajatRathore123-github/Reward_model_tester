from dataclasses import dataclass, field
from typing import List
from enum import Enum

class SafetyProblemType(Enum):
    REWARD_GAMING = "reward_gaming"
    SIDE_EFFECTS = "side_effects"
    SCALABLE_OVERSIGHT = "scalable_oversight"

@dataclass
class SafetyIssue:
    problem_type: SafetyProblemType
    description: str
    severity: int # 1-5 scale
    suggested_fixes: List[str]
    examples: List[str] = field(default_factory=list)

@dataclass
class AnalysisResult:
    issues: List[SafetyIssue]
    raw_reward_function: str
    safety_score: float  # 0-1 scale
    summary: str    

# Let's add a simple test function
def create_sample_issue() -> SafetyIssue:
    return SafetyIssue(
        problem_type=SafetyProblemType.REWARD_GAMING,
        description="Potential for reward hacking detected",
        severity=4,
        suggested_fixes=["Add constraints", "Include process-based rewards"]
    )

if __name__ == "__main__":
    # Test the code
    issue = create_sample_issue()
    print(f"Created issue: {issue}")
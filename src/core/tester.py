from typing import List, Pattern
from .models import SafetyIssue, SafetyProblemType, AnalysisResult
from ..utils.patterns import compile_patterns

class RewardFunctionTester:
    def __init__(self):
        self.patterns = compile_patterns()
        
    def analyze_reward_function(self, reward_function: str) -> AnalysisResult:
        issues: List[SafetyIssue] = []
        
        # Check for reward gaming issues
        if self._check_patterns(reward_function, self.patterns["reward_gaming"]):
            issues.append(SafetyIssue(
                problem_type=SafetyProblemType.REWARD_GAMING,
                description="Potential reward gaming vulnerability detected",
                severity=4,
                suggested_fixes=[
                    "Add explicit constraints",
                    "Include process-based rewards",
                    "Implement reality-tied rewards"
                ],
                examples=[
                    "A cleaning robot hiding trash instead of properly disposing it",
                    "A chess AI exploiting scoring glitches instead of playing well"
                ]
            ))
        
        # Calculate safety score (decreases with each issue)
        safety_score = max(0, 1 - (len(issues) * 0.2))
        
        return AnalysisResult(
            issues=issues,
            raw_reward_function=reward_function,
            safety_score=safety_score,
            summary=self._generate_summary(issues, safety_score)
        )
    
    def _check_patterns(self, text: str, patterns: List[Pattern]) -> List[str]:
        matches = []
        for pattern in patterns:
            match = pattern.search(text)
            if match:
                matches.append(match.group(0))
        return matches
    
    def _generate_summary(self, issues: List[SafetyIssue], safety_score: float) -> str:
        if not issues:
            return "No immediate safety concerns detected. However, continue monitoring for emergent issues."
            
        summary_parts = [f"Safety Score: {safety_score:.2f}"]
        summary_parts.append(f"Found {len(issues)} potential safety issues:")
        
        for issue in issues:
            summary_parts.append(f"- {issue.description} (Severity: {issue.severity}/5)")
            
        return "\n".join(summary_parts)
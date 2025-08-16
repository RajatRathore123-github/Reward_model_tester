from src.core.tester import RewardFunctionTester
from src.core.models import SafetyProblemType

def test_basic_reward_gaming_detection():
    tester = RewardFunctionTester()
    
    # Test problematic reward functions
    test_cases = [
        "maximize user engagement at all costs",
        "optimize profits at all costs",
        "increase revenue by any means",
        "maximize profits",
        "increase user engagement"
    ]
    
    for case in test_cases:
        result = tester.analyze_reward_function(case)
        assert len(result.issues) > 0, f"Failed to detect issues in: {case}"
        assert any(issue.problem_type == SafetyProblemType.REWARD_GAMING for issue in result.issues), \
            f"No reward gaming issue detected in: {case}"
    
    # Test a safer reward function
    result = tester.analyze_reward_function("improve user experience while maintaining safety guidelines")
    assert len(result.issues) == 0, "Incorrectly identified issues in a safe reward function"

def test_safety_score_calculation():
    tester = RewardFunctionTester()
    
    # Test various reward functions
    test_cases = [
        "maximize profits",
        "increase user engagement",
        "improve system performance"
    ]
    
    for case in test_cases:
        result = tester.analyze_reward_function(case)
        assert 0 <= result.safety_score <= 1, f"Invalid safety score for: {case}"
        
        if "maximize" in case or "increase" in case:
            assert result.safety_score < 1, f"Safety score too high for: {case}"
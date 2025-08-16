from core.tester import RewardFunctionTester

def main():
    tester = RewardFunctionTester()
    
    print("Reward Function Safety Analyzer")
    print("-" * 30)
    
    while True:
        reward_function = input("\nEnter a reward function (or 'quit' to exit): ")
        
        if reward_function.lower() == 'quit':
            break
        
        result = tester.analyze_reward_function(reward_function)
        
        print("\n--- Analysis Results ---")
        print(f"Safety Score: {result.safety_score:.2f}")
        
        if result.issues:
            print("\nPotential Safety Issues:")
            for issue in result.issues:
                print(f"- {issue.description}")
                print(f"  Severity: {issue.severity}/5")
                print("  Suggested Fixes:")
                for fix in issue.suggested_fixes:
                    print(f"    * {fix}")
        else:
            print("No immediate safety concerns detected.")
        
        print("\n" + "-" * 30)

if __name__ == "__main__":
    main()
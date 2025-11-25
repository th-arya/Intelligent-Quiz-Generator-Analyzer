"""
Module: report.py
Purpose: Generate and display performance report
"""


def generate_report(results, mcqs, user_answers):
    """
    Generate a comprehensive performance report.
    
    Args:
        results (dict): Grading results from grader.py
        mcqs (list): Original MCQ list
        user_answers (dict): User's answers
        
    Returns:
        dict: Report data
    """
    # Identify weak topics
    weak_topics = identify_weak_topics(results)
    
    # Create report data
    report_data = {
        "results": results,
        "weak_topics": weak_topics,
        "grade": get_grade(results['percentage'])
    }
    
    return report_data


def identify_weak_topics(results):
    """
    Identify topics where user answered incorrectly.
    
    Args:
        results (dict): Grading results
        
    Returns:
        list: List of weak topics/keywords
    """
    weak_topics = []
    
    for detail in results['details']:
        if not detail['is_correct']:
            keyword = detail.get('keyword', '')
            if keyword and keyword not in weak_topics:
                weak_topics.append(keyword)
    
    return weak_topics


def get_grade(percentage):
    """
    Convert percentage to letter grade.
    
    Args:
        percentage (float): Percentage score
        
    Returns:
        str: Letter grade
    """
    if percentage >= 90:
        return "A (Excellent)"
    elif percentage >= 80:
        return "B (Good)"
    elif percentage >= 70:
        return "C (Average)"
    elif percentage >= 60:
        return "D (Below Average)"
    else:
        return "F (Fail)"


def print_report(report_data):
    """
    Print formatted report to terminal.
    
    Args:
        report_data (dict): Report data from generate_report()
    """
    results = report_data['results']
    weak_topics = report_data['weak_topics']
    grade = report_data['grade']
    
    print("\n" + "="*60)
    print("QUIZ PERFORMANCE REPORT".center(60))
    print("="*60 + "\n")
    
    # Overall Score
    print("OVERALL SCORE:")
    print("-" * 60)
    print(f"Total Questions:    {results['total']}")
    print(f"Correct Answers:    {results['correct']}")
    print(f"Wrong Answers:      {results['wrong']}")
    print(f"Percentage Score:   {results['percentage']}%")
    print(f"Grade:              {grade}")
    print("-" * 60 + "\n")
    
    # Question-by-Question Breakdown
    print("DETAILED BREAKDOWN:")
    print("-" * 60)
    
    for detail in results['details']:
        status = "✓ CORRECT" if detail['is_correct'] else "✗ WRONG"
        print(f"\nQuestion {detail['question_num']}: {status}")
        print(f"Q: {detail['question']}")
        print(f"Your answer:    {detail['user_answer']}")
        
        if not detail['is_correct']:
            print(f"Correct answer: {detail['correct_answer']}")
    
    print("\n" + "-" * 60 + "\n")
    
    # Weak Topics
    print("AREAS FOR IMPROVEMENT:")
    print("-" * 60)
    
    if weak_topics:
        print("You need to review the following topics:\n")
        for i, topic in enumerate(weak_topics, 1):
            print(f"  {i}. {topic}")
    else:
        print("Excellent! No weak areas identified.")
    
    print("\n" + "-" * 60 + "\n")
    
    # Performance Summary
    print("PERFORMANCE SUMMARY:")
    print("-" * 60)
    
    if results['percentage'] >= 80:
        message = "Outstanding performance! Keep up the great work!"
    elif results['percentage'] >= 60:
        message = "Good effort! Review weak topics and try again."
    else:
        message = "Need improvement. Please review the topics and retry."
    
    print(message)
    
    print("\n" + "="*60 + "\n")


# Test function (optional - for module testing)
if __name__ == "__main__":
    # Test data
    test_results = {
        "total": 5,
        "correct": 3,
        "wrong": 2,
        "percentage": 60.0,
        "details": [
            {
                "question_num": 1,
                "question": "What is Python?",
                "user_answer": "A programming language",
                "correct_answer": "A programming language",
                "is_correct": True,
                "keyword": "Python"
            },
            {
                "question_num": 2,
                "question": "What are variables?",
                "user_answer": "Functions",
                "correct_answer": "Storage containers",
                "is_correct": False,
                "keyword": "Variables"
            }
        ]
    }
    
    # Generate and print report
    report = generate_report(test_results, [], {})
    print_report(report)

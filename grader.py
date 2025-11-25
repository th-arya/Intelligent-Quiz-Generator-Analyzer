"""
Module: grader.py
Purpose: Compare user answers with correct answers and calculate score
"""


def grade_quiz(mcqs, user_answers):
    """
    Grade the quiz by comparing user answers with correct answers.
    
    Args:
        mcqs (list): List of MCQ dictionaries with correct answers
        user_answers (dict): Dictionary of user's answers {question_num: answer}
        
    Returns:
        dict: Results dictionary with score and details
    """
    total_questions = len(mcqs)
    correct_count = 0
    wrong_count = 0
    details = []
    
    # Compare each answer
    for i, mcq in enumerate(mcqs, 1):
        correct_answer = mcq['answer']
        user_answer = user_answers.get(i, "")
        
        # Check if answer is correct (case-insensitive comparison)
        is_correct = user_answer.lower().strip() == correct_answer.lower().strip()
        
        if is_correct:
            correct_count += 1
        else:
            wrong_count += 1
        
        # Store details
        detail = {
            "question_num": i,
            "question": mcq['question'],
            "user_answer": user_answer,
            "correct_answer": correct_answer,
            "is_correct": is_correct,
            "keyword": mcq.get('keyword', '')
        }
        details.append(detail)
    
    # Calculate percentage
    percentage = calculate_percentage(correct_count, total_questions)
    
    # Create results dictionary
    results = {
        "total": total_questions,
        "correct": correct_count,
        "wrong": wrong_count,
        "percentage": percentage,
        "details": details
    }
    
    return results


def calculate_percentage(correct, total):
    """
    Calculate percentage score.
    
    Args:
        correct (int): Number of correct answers
        total (int): Total number of questions
        
    Returns:
        float: Percentage score (0-100)
    """
    if total == 0:
        return 0.0
    
    percentage = (correct / total) * 100
    return round(percentage, 2)


# Test function (optional - for module testing)
if __name__ == "__main__":
    # Test data
    test_mcqs = [
        {
            "question": "What is Python?",
            "options": ["A programming language", "A snake", "A framework", "A database"],
            "answer": "A programming language",
            "keyword": "Python"
        },
        {
            "question": "What are variables?",
            "options": ["Storage containers", "Functions", "Loops", "Classes"],
            "answer": "Storage containers",
            "keyword": "Variables"
        }
    ]
    
    test_answers = {
        1: "A programming language",
        2: "Functions"
    }
    
    # Grade the quiz
    results = grade_quiz(test_mcqs, test_answers)
    
    print("Grading Results:")
    print(f"Total: {results['total']}")
    print(f"Correct: {results['correct']}")
    print(f"Wrong: {results['wrong']}")
    print(f"Percentage: {results['percentage']}%")

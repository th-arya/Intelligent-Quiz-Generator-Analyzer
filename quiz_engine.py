"""
Module: quiz_engine.py
Purpose: Display questions in terminal and collect user answers
"""


def run_quiz(mcqs):
    """
    Run the quiz in terminal and collect user answers.
    
    Args:
        mcqs (list): List of MCQ dictionaries
        
    Returns:
        dict: Dictionary mapping question numbers to user answers
    """
    print("\n" + "="*60)
    print("QUIZ STARTED".center(60))
    print("="*60)
    print(f"\nTotal Questions: {len(mcqs)}")
    print("Enter the option number (1-4) for each question.")
    print("-"*60 + "\n")
    
    user_answers = {}
    
    for i, mcq in enumerate(mcqs, 1):
        # Display question
        display_question(mcq, i)
        
        # Get user answer
        answer = get_user_answer(mcq['options'])
        
        # Store user's selected answer text
        user_answers[i] = answer
        
        print()  # Blank line between questions
    
    print("="*60)
    print("QUIZ COMPLETED".center(60))
    print("="*60 + "\n")
    
    return user_answers


def display_question(question_data, question_num):
    """
    Display a single question with options.
    
    Args:
        question_data (dict): MCQ data containing question and options
        question_num (int): Question number
    """
    print(f"Question {question_num}: {question_data['question']}")
    print()
    
    # Display options
    for i, option in enumerate(question_data['options'], 1):
        print(f"  {i}. {option}")
    
    print()


def get_user_answer(options):
    """
    Get and validate user input.
    
    Args:
        options (list): List of answer options
        
    Returns:
        str: User's selected answer text
    """
    while True:
        try:
            # Get user input
            choice = input("Your answer (1-4): ").strip()
            
            # Validate input
            choice_num = int(choice)
            
            if 1 <= choice_num <= len(options):
                # Return the selected option text
                return options[choice_num - 1]
            else:
                print(f"Invalid choice! Please enter a number between 1 and {len(options)}.")
        
        except ValueError:
            print("Invalid input! Please enter a number.")
        except KeyboardInterrupt:
            print("\n\nQuiz cancelled by user.")
            exit()


# Test function (optional - for module testing)
if __name__ == "__main__":
    # Test MCQs
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
    
    # Run test quiz
    answers = run_quiz(test_mcqs)
    print("\nUser answers:")
    print(answers)

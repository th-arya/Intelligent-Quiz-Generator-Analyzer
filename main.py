"""
Module: main.py
Purpose: Main orchestrator for the Intelligent Quiz Generator & Analyzer
"""

# Import all modules
import ingest
import qa_generator
import quiz_engine
import grader
import report


def main():
    """
    Main function to run the complete quiz system.
    """
    print("\n" + "="*60)
    print("INTELLIGENT QUIZ GENERATOR & ANALYZER".center(60))
    print("="*60 + "\n")
    
    # Step 1: Load lecture notes
    print("Step 1: Loading lecture notes...")
    filepath = "data/lecture_notes.txt"
    notes = ingest.load_notes(filepath)
    
    if not notes:
        print("Failed to load lecture notes. Exiting.")
        return
    
    print(f"✓ Loaded {len(notes)} characters from lecture notes.\n")
    
    # Step 2: Generate MCQs
    print("Step 2: Generating quiz questions...")
    num_questions = 5
    
    # Ask user how many questions they want
    try:
        user_input = input(f"How many questions do you want? (default: {num_questions}): ").strip()
        if user_input:
            num_questions = int(user_input)
            if num_questions < 1:
                print("Invalid number. Using default: 5")
                num_questions = 5
    except ValueError:
        print("Invalid input. Using default: 5")
        num_questions = 5
    
    mcqs = qa_generator.generate_mcqs(notes, num_questions)
    
    if not mcqs:
        print("Failed to generate questions. Exiting.")
        return
    
    print(f"✓ Generated {len(mcqs)} questions.\n")
    
    # Wait for user to be ready
    input("Press Enter to start the quiz...")
    
    # Step 3: Run the quiz
    user_answers = quiz_engine.run_quiz(mcqs)
    
    # Step 4: Grade the quiz
    print("Step 4: Grading your answers...")
    results = grader.grade_quiz(mcqs, user_answers)
    print("✓ Grading completed.\n")
    
    # Step 5: Generate and display report
    print("Step 5: Generating performance report...")
    report_data = report.generate_report(results, mcqs, user_answers)
    report.print_report(report_data)
    
    # Ask if user wants to retry
    print("\n" + "="*60)
    retry = input("Would you like to take another quiz? (yes/no): ").strip().lower()
    
    if retry in ['yes', 'y']:
        print("\n" * 2)
        main()  # Recursive call to restart
    else:
        print("\nThank you for using the Quiz Generator!")
        print("="*60 + "\n")


# Entry point
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
        print("="*60 + "\n")

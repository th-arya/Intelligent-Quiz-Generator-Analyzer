# 📘 Intelligent Quiz Generator & Analyzer

A complete command-line quiz generator system built using **ONLY Python** (no HTML, CSS, JavaScript, Flask, or external libraries).

## 🎯 Features

- ✅ Load lecture notes from text files
- ✅ Auto-generate MCQs using pure Python logic
- ✅ Interactive terminal-based quiz interface
- ✅ Automatic grading system
- ✅ Detailed performance reports
- ✅ Weak topic identification
- ✅ Fully modular design

## 📂 Project Structure

```
quiz_project/
│
├── ingest.py          # Load and clean lecture notes
├── qa_generator.py    # Generate MCQs from text
├── quiz_engine.py     # Display questions and get user input
├── grader.py          # Compare answers and calculate score
├── report.py          # Generate performance report
├── main.py            # Main orchestrator
│
├── data/
│   └── lecture_notes.txt  # Sample lecture content
│
└── README.md          # This file
```

## 🚀 How to Run

1. **Navigate to the project directory:**
   ```bash
   cd quiz_project
   ```

2. **Run the quiz:**
   ```bash
   python main.py
   ```

3. **Follow the prompts:**
   - Choose how many questions you want
   - Answer each question by entering 1-4
   - View your performance report

## 🧩 Module Descriptions

### 1. `ingest.py`
- Loads lecture notes from `data/lecture_notes.txt`
- Cleans and normalizes text content
- Returns ready-to-process text

### 2. `qa_generator.py`
- Splits text into sentences
- Extracts keywords from sentences
- Creates MCQs with 4 options each
- Generates distractors (wrong answers)
- Uses pure Python logic (no NLP libraries)

### 3. `quiz_engine.py`
- Displays questions in the terminal
- Shows numbered options (1-4)
- Validates user input
- Collects user answers

### 4. `grader.py`
- Compares user answers with correct answers
- Calculates score and percentage
- Returns detailed results

### 5. `report.py`
- Generates comprehensive performance report
- Identifies weak topics
- Assigns letter grades
- Prints formatted report to terminal

### 6. `main.py`
- Orchestrates the entire system
- Connects all modules
- Provides user interface

## 📝 Adding Your Own Lecture Notes

1. Open `data/lecture_notes.txt`
2. Add your lecture content (plain text)
3. Each sentence should be clear and informative
4. Separate topics with periods
5. Run the quiz!

## 🎓 Python Essentials Used

- ✅ **Variables**: Storing data throughout the program
- ✅ **Lists**: Managing questions, options, and results
- ✅ **Dictionaries**: Structuring MCQ data and results
- ✅ **Loops**: Iterating through questions and answers
- ✅ **Functions**: Modular, reusable code blocks
- ✅ **Modules**: Organized code in separate files
- ✅ **File Handling**: Reading lecture notes
- ✅ **String Manipulation**: Processing text
- ✅ **Input/Output**: Terminal interaction
- ✅ **Conditional Logic**: Grading and validation

## 📊 Sample Output

```
============================================================
              INTELLIGENT QUIZ GENERATOR & ANALYZER
============================================================

Step 1: Loading lecture notes...
✓ Loaded 1234 characters from lecture notes.

Step 2: Generating quiz questions...
How many questions do you want? (default: 5): 5
✓ Generated 5 questions.

Press Enter to start the quiz...

============================================================
                        QUIZ STARTED
============================================================

Total Questions: 5
Enter the option number (1-4) for each question.
------------------------------------------------------------

Question 1: What is Python?
  1. A programming language
  2. A snake
  3. A framework
  4. A database

Your answer (1-4): 1

[... more questions ...]

============================================================
                  QUIZ PERFORMANCE REPORT
============================================================

OVERALL SCORE:
------------------------------------------------------------
Total Questions:    5
Correct Answers:    4
Wrong Answers:      1
Percentage Score:   80.0%
Grade:              B (Good)
------------------------------------------------------------
```

## 🔧 Testing Individual Modules

Each module can be tested independently:

```bash
# Test ingest module
python ingest.py

# Test MCQ generator
python qa_generator.py

# Test quiz engine
python quiz_engine.py

# Test grader
python grader.py

# Test report generator
python report.py
```

## 💡 Tips

- **Better Questions**: Add more detailed lecture notes for better MCQs
- **Custom Difficulty**: Modify `qa_generator.py` to adjust question complexity
- **More Questions**: Increase the default number in `main.py`
- **Retry Quiz**: The system allows you to retake quizzes

## 🎯 Learning Outcomes

This project demonstrates:
- Modular programming design
- File handling in Python
- Algorithm building without external libraries
- Clean code organization
- User input validation
- Data structure usage (lists, dicts)
- Function-based programming

## 📄 License

This is a learning project built for educational purposes.

---

**Built with ❤️ using Pure Python**

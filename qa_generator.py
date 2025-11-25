"""
Module: qa_generator.py
Purpose: Generate MCQs from lecture notes using pure Python logic
"""

import random


def generate_mcqs(text, num_questions=5):
    """
    Generate multiple choice questions from text.
    
    Args:
        text (str): Lecture notes text
        num_questions (int): Number of questions to generate
        
    Returns:
        list: List of MCQ dictionaries
    """
    # Split text into sentences
    sentences = split_into_sentences(text)
    
    if len(sentences) == 0:
        print("Error: No sentences found in text!")
        return []
    
    # Limit number of questions to available sentences
    num_questions = min(num_questions, len(sentences))
    
    # Select random sentences for questions
    selected_sentences = random.sample(sentences, num_questions)
    
    mcqs = []
    for i, sentence in enumerate(selected_sentences):
        # Extract keyword from sentence
        keyword = extract_keyword(sentence)
        
        if keyword:
            # Create question
            question = create_question(sentence, keyword)
            
            # Generate options (1 correct + 3 distractors)
            correct_answer = keyword
            distractors = create_distractors(keyword, sentences, sentence)
            
            # Combine and shuffle options
            options = [correct_answer] + distractors
            random.shuffle(options)
            
            # Create MCQ dictionary
            mcq = {
                "question": question,
                "options": options,
                "answer": correct_answer,
                "keyword": keyword
            }
            
            mcqs.append(mcq)
    
    return mcqs


def split_into_sentences(text):
    """
    Split text into sentences.
    
    Args:
        text (str): Input text
        
    Returns:
        list: List of sentences
    """
    # Split by period
    sentences = text.split('.')
    
    # Clean and filter empty sentences
    sentences = [s.strip() for s in sentences if s.strip()]
    
    return sentences


def extract_keyword(sentence):
    """
    Extract a keyword from a sentence.
    
    Args:
        sentence (str): Input sentence
        
    Returns:
        str: Extracted keyword
    """
    # Common words to skip
    common_words = ['is', 'are', 'was', 'were', 'the', 'a', 'an', 'and', 'or', 
                   'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by']
    
    # Split sentence into words
    words = sentence.split()
    
    # Find first meaningful word (capitalized or not in common words)
    for word in words:
        # Remove punctuation
        clean_word = word.strip('.,!?;:')
        
        # Check if it's a meaningful keyword
        if clean_word and clean_word.lower() not in common_words and len(clean_word) > 2:
            return clean_word
    
    # If no keyword found, return first word
    if words:
        return words[0].strip('.,!?;:')
    
    return ""


def create_question(sentence, keyword):
    """
    Create a question from a sentence and keyword.
    
    Args:
        sentence (str): Original sentence
        keyword (str): Keyword to ask about
        
    Returns:
        str: Generated question
    """
    # Question templates
    templates = [
        f"What is {keyword}?",
        f"Which of the following describes {keyword}?",
        f"Fill in the blank: {sentence.replace(keyword, '_____')}",
        f"According to the notes, what is true about {keyword}?"
    ]
    
    # Choose random template
    question = random.choice(templates)
    
    return question


def create_distractors(keyword, all_sentences, current_sentence):
    """
    Create distractor (wrong) options.
    
    Args:
        keyword (str): Correct answer keyword
        all_sentences (list): All sentences from text
        current_sentence (str): Current sentence being used
        
    Returns:
        list: List of 3 distractor options
    """
    # Static distractor pool
    static_distractors = [
        "A type of database",
        "A web framework",
        "A hardware component",
        "An operating system",
        "A network protocol",
        "A file format",
        "A design pattern",
        "A testing methodology",
        "A version control system",
        "A programming paradigm"
    ]
    
    # Extract keywords from other sentences
    other_keywords = []
    for sentence in all_sentences:
        if sentence != current_sentence:
            kw = extract_keyword(sentence)
            if kw and kw != keyword:
                other_keywords.append(kw)
    
    # Combine keyword-based and static distractors
    distractor_pool = other_keywords + static_distractors
    
    # Remove duplicates and the correct keyword
    distractor_pool = [d for d in distractor_pool if d.lower() != keyword.lower()]
    
    # Remove duplicates while preserving order
    seen = set()
    unique_distractors = []
    for d in distractor_pool:
        if d.lower() not in seen:
            seen.add(d.lower())
            unique_distractors.append(d)
    
    # Select 3 random distractors
    if len(unique_distractors) >= 3:
        distractors = random.sample(unique_distractors, 3)
    else:
        # If not enough unique distractors, use what we have and add generic ones
        distractors = unique_distractors + static_distractors
        distractors = random.sample(distractors, min(3, len(distractors)))
    
    return distractors[:3]


# Test function (optional - for module testing)
if __name__ == "__main__":
    test_text = "Python is a programming language. Java is also a programming language. Variables store data. Functions perform tasks."
    mcqs = generate_mcqs(test_text, 3)
    
    print("Generated MCQs:")
    for i, mcq in enumerate(mcqs, 1):
        print(f"\n{i}. {mcq['question']}")
        for j, option in enumerate(mcq['options'], 1):
            print(f"   {j}. {option}")
        print(f"   Correct: {mcq['answer']}")

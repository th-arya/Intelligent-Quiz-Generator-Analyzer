"""
Module: ingest.py
Purpose: Load and clean lecture notes from text file
"""


def load_notes(filepath):
    """
    Load lecture notes from a text file.
    
    Args:
        filepath (str): Path to the lecture notes file
        
    Returns:
        str: Cleaned text content from the file
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Clean the text
        cleaned_text = clean_text(text)
        return cleaned_text
    
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found!")
        return ""
    except Exception as e:
        print(f"Error loading file: {e}")
        return ""


def clean_text(text):
    """
    Clean and normalize text content.
    
    Args:
        text (str): Raw text content
        
    Returns:
        str: Cleaned text with normalized whitespace
    """
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    # Remove leading/trailing whitespace
    text = text.strip()
    
    return text


# Test function (optional - for module testing)
if __name__ == "__main__":
    # Test the module
    test_file = "data/lecture_notes.txt"
    notes = load_notes(test_file)
    print("Loaded notes:")
    print(notes)
    print(f"\nTotal characters: {len(notes)}")

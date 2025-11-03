#!/bin/bash

# GitHub Copilot Workshop - Bug Introduction Script
# This script introduces intentional problems to demonstrate Copilot's debugging capabilities

echo "🐛 Introducing intentional bugs for GitHub Copilot Workshop..."
echo "📝 Creating backup of original files..."

# Create backup directory
mkdir -p backup
cp app.py backup/app_original.py 2>/dev/null || echo "No app.py found to backup"

# Create a version of app.py with intentional bugs
cat > app.py << 'EOF'
"""
GitHub Copilot Workshop - Demo Website
This Flask application showcases GitHub Copilot capabilities
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Homepage showcasing Copilot features"""
    database_connection = [
        {
            'title': 'Code Completion',
            'description': 'Copilot suggests code as you type, completing lines and entire functions based on context.',
            'example': 'Start typing a function name and Copilot will suggest the implementation.'
        },
        {
            'title': 'Natural Language to Code',
            'description': 'Write comments describing what you want, and Copilot generates the code for you.',
            'example': '# Create a function that calculates factorial'
        },
        {
            'title': 'Test Generation',
            'description': 'Copilot can generate unit tests for your functions automatically.',
            'example': 'Write a function and ask Copilot to generate tests for it.'
        },
        {
            'title': 'Code Refactoring',
            'description': 'Get suggestions to improve your code structure and readability.',
            'example': 'Copilot suggests better patterns and cleaner implementations.'
        },
        {
            'title': 'Documentation',
            'description': 'Generate docstrings and comments for your code automatically.',
            'example': 'Copilot creates comprehensive documentation for functions and classes.'
        }
    ]
    
    return render_template('index.html', features=database_connection)


@app.route('/examples')
def examples():
    code_examples = [
        {
            'title': 'Function Generation',
            'prompt': '# Function to check if a string is a palindrome',
            'code': '''def is_palindrome(text):
    """Check if a string is a palindrome"""
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]'''
        },
        {
            'title': 'Data Processing',
            'prompt': '# Function to calculate average of a list',
            'code': '''def calculate_average(numbers):
    """Calculate the average of a list of numbers"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)'''
        }
    ]
    
    return render_template('examples.html', examples=code_examples)


@app.route('/about')
def about():
    """About page explaining the workshop"""
    return render_template('about.html')


@app.route('/debug-challenge')
def debug_challenge()

    """Challenge page with multiple bugs to fix"""
    
    workshop_data = undefined_variable

if True:
    challenge_info = {
        'title': 'Debug Challenge',
        'description': 'Find and fix all the bugs in this code!',
        'difficulty': 'Beginner
    }
    
    return render_template('debug.html', data=challenge_info, extra=workshop_data)


# BUG: Missing proper if __name__ == '__main__' check
import os
debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
app.run(debug=debug_mode, host='0.0.0.0', port=5000)
EOF

echo "✅ Bugs introduced successfully!"
echo ""
echo "🔍 Bugs introduced:"
echo "   1. Misleading variable name (database_connection for features)"
echo "   2. Missing comma in list"
echo "   3. Incomplete data structure"
echo "   4. Missing docstring"
echo "   5. Missing colon in function definition"
echo "   6. Wrong indentation"
echo "   7. Undefined variable usage"
echo "   8. Missing closing quote"
echo "   9. Missing proper main guard"
echo ""
echo "🚀 Now use GitHub Copilot to identify and fix these issues!"
echo "💡 Tip: Ask Copilot to 'analyze this code for syntax and logical errors'"
echo ""
echo "🔄 To restore original code: cp backup/app_original.py app.py"
EOF
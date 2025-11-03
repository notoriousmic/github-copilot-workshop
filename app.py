"""
GitHub Copilot Workshop - Demo Website
This Flask application showcases GitHub Copilot capabilities
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Homepage showcasing Copilot features"""
    copilot_features = [
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
        },
        {
            'title': 'Multi-Language Support',
            'description': 'Works across dozens of programming languages and frameworks.',
            'example': 'Python, JavaScript, TypeScript, Go, Ruby, and many more.'
        }
    ]
    
    return render_template('index.html', features=copilot_features)


@app.route('/examples')
def examples():
    """Page showing code examples"""
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
        },
        {
            'title': 'API Integration',
            'prompt': '# Function to fetch user data from API',
            'code': '''import requests

def fetch_user_data(user_id):
    """Fetch user data from API"""
    url = f"https://api.example.com/users/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None'''
        }
    ]
    
    return render_template('examples.html', examples=code_examples)


@app.route('/about')
def about():
    """About page explaining the workshop"""
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

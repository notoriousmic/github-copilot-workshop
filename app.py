"""
GitHub Copilot Workshop - Demo Website

This Flask application showcases GitHub Copilot capabilities through an
interactive web interface. The application demonstrates various features
of GitHub Copilot including code completion, natural language to code
conversion, test generation, and more.

Author: GitHub Copilot Workshop Team
License: MIT
"""

from typing import Dict, List
import os
import logging
from flask import Flask, render_template, abort
from werkzeug.exceptions import NotFound, InternalServerError

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@app.route('/')
def index() -> str:
    """
    Render the homepage showcasing GitHub Copilot features.

    This route displays an overview of GitHub Copilot's key capabilities
    including code completion, natural language to code conversion, test
    generation, code refactoring, documentation generation, and
    multi-language support.

    Returns:
        str: Rendered HTML template for the homepage with copilot features.

    Raises:
        InternalServerError: If template rendering fails.
    """
    logger.info("Rendering homepage")
    copilot_features: List[Dict[str, str]] = [
        {
            'title': 'Code Completion',
            'description': (
                'Copilot suggests code as you type, completing lines '
                'and entire functions based on context.'
            ),
            'example': (
                'Start typing a function name and Copilot will '
                'suggest the implementation.'
            )
        },
        {
            'title': 'Natural Language to Code',
            'description': (
                'Write comments describing what you want, and Copilot '
                'generates the code for you.'
            ),
            'example': '# Create a function that calculates factorial'
        },
        {
            'title': 'Test Generation',
            'description': (
                'Copilot can generate unit tests for your functions '
                'automatically.'
            ),
            'example': (
                'Write a function and ask Copilot to generate '
                'tests for it.'
            )
        },
        {
            'title': 'Code Refactoring',
            'description': (
                'Get suggestions to improve your code structure '
                'and readability.'
            ),
            'example': (
                'Copilot suggests better patterns and cleaner '
                'implementations.'
            )
        },
        {
            'title': 'Documentation',
            'description': (
                'Generate docstrings and comments for your code '
                'automatically.'
            ),
            'example': (
                'Copilot creates comprehensive documentation for '
                'functions and classes.'
            )
        },
        {
            'title': 'Multi-Language Support',
            'description': (
                'Works across dozens of programming languages '
                'and frameworks.'
            ),
            'example': (
                'Python, JavaScript, TypeScript, Go, Ruby, '
                'and many more.'
            )
        }
    ]

    try:
        return render_template('index.html', features=copilot_features)
    except Exception as e:
        logger.error(f"Error rendering homepage: {type(e).__name__}")
        abort(500)


@app.route('/examples')
def examples() -> str:
    """
    Render the examples page with code generation demonstrations.

    This route displays practical examples of how GitHub Copilot can
    generate code from natural language prompts, including function
    generation, data processing, and API integration examples.

    Returns:
        str: Rendered HTML template for the examples page with code samples.

    Raises:
        InternalServerError: If template rendering fails.
    """
    logger.info("Rendering examples page")
    code_examples: List[Dict[str, str]] = [
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

    try:
        return render_template('examples.html', examples=code_examples)
    except Exception as e:
        logger.error(f"Error rendering examples page: {type(e).__name__}")
        abort(500)


@app.route('/about')
def about() -> str:
    """
    Render the about page with workshop information.

    This route displays information about the GitHub Copilot Workshop,
    best practices for using Copilot, and additional resources.

    Returns:
        str: Rendered HTML template for the about page.

    Raises:
        InternalServerError: If template rendering fails.
    """
    logger.info("Rendering about page")
    try:
        return render_template('about.html')
    except Exception as e:
        logger.error(f"Error rendering about page: {type(e).__name__}")
        abort(500)


@app.errorhandler(404)
def not_found_error(error: NotFound) -> tuple[str, int]:
    """
    Handle 404 Not Found errors.

    Args:
        error: The NotFound exception that triggered this handler.

    Returns:
        tuple: Error message and HTTP status code 404.
    """
    logger.warning(f"404 error: {error}")
    return "Page not found", 404


@app.errorhandler(500)
def internal_error(error: InternalServerError) -> tuple[str, int]:
    """
    Handle 500 Internal Server errors.

    Args:
        error: The InternalServerError exception that triggered this handler.

    Returns:
        tuple: Error message and HTTP status code 500.
    """
    logger.error(f"500 error: {error}")
    return "Internal server error", 500


if __name__ == '__main__':
    # Debug mode should only be enabled in development
    # Set to False in production environments
    # WARNING: Never enable debug mode in production!
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

    if debug_mode:
        logger.warning("Running in DEBUG mode - not suitable for production!")
    else:
        logger.info("Running in production mode")

    app.run(debug=debug_mode, host='0.0.0.0', port=5000)

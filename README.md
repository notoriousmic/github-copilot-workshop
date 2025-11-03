# GitHub Copilot Workshop Website

This project contains a basic Python website that showcases GitHub Copilot capabilities. The website demonstrates various features of GitHub Copilot through an interactive web application built with Flask.

## ⚠️ Security Notice

**IMPORTANT**: This application is for educational and demonstration purposes. Before deploying to production:
- Never enable debug mode (`FLASK_DEBUG=false` or unset)
- Use a production WSGI server (e.g., Gunicorn, uWSGI)
- Implement proper authentication and authorization
- Enable HTTPS and secure HTTP headers
- Review and follow the [Security Policy](SECURITY.md)

## Features

- **Homepage**: Overview of GitHub Copilot features and capabilities
- **Examples Page**: Practical code examples showing how Copilot generates code from natural language prompts
- **About Page**: Information about the workshop and best practices for using Copilot

## Technologies Used

- **Python 3.x**: Backend programming language
- **Flask 3.0.0**: Lightweight web framework
- **HTML/CSS**: Frontend structure and styling
- **Jinja2**: Template engine (included with Flask)

All dependencies are pinned to specific versions for security and reproducibility. See [DEPENDENCIES.md](DEPENDENCIES.md) for license information.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. Make sure you have Python 3.x installed on your system:
   ```bash
   python3 --version
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/notoriousmic/github-copilot-workshop.git
   cd github-copilot-workshop
   ```

3. (Recommended) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the required dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

## Running the Website

1. Navigate to the project directory:
   ```bash
   cd github-copilot-workshop
   ```

2. Run the Flask application in production mode (default):
   ```bash
   python3 app.py
   ```

   For development with debug mode enabled:
   ```bash
   FLASK_DEBUG=true python3 app.py
   ```

   ⚠️ **WARNING**: Never enable debug mode in production environments!

3. Open your web browser and visit:
   ```
   http://localhost:5000
   ```

The website will be running locally on port 5000. You can now explore the different pages to learn about GitHub Copilot capabilities!

## Testing

This project includes comprehensive unit tests for all Flask routes.

### Running Tests

Run all tests:
```bash
python3 -m unittest discover tests -v
```

Run a specific test file:
```bash
python3 -m unittest tests.test_app -v
```

### Test Coverage

The test suite covers:
- All Flask route endpoints (/, /examples, /about)
- Error handlers (404, 500)
- Response validation
- Content verification
- Application configuration

## Code Quality & Linting

This project follows Python best practices and uses flake8 for linting.

### Install Development Tools

```bash
pip3 install flake8
```

### Run Linting

```bash
flake8 app.py tests/
```

### Style Guidelines

- Maximum line length: 100 characters
- Follow PEP 8 style guide
- Use type hints for all functions
- Comprehensive docstrings for all modules, classes, and functions
- Maximum cyclomatic complexity: 10

See [.flake8](.flake8) for complete linting configuration.

## GitHub Copilot Features Showcased

This website demonstrates the following Copilot capabilities:

1. **Code Completion**: Auto-completing code as you type
2. **Natural Language to Code**: Converting comments into working code
3. **Test Generation**: Creating unit tests automatically
4. **Code Refactoring**: Suggesting improvements to code structure
5. **Documentation**: Generating docstrings and comments
6. **Multi-Language Support**: Working across various programming languages

## Development

### Project Structure

```
github-copilot-workshop/
├── app.py                  # Main Flask application with type hints and docstrings
├── requirements.txt        # Python dependencies (pinned versions)
├── README.md              # This file
├── SECURITY.md            # Security policy and responsible disclosure
├── DEPENDENCIES.md        # Dependency licenses documentation
├── .flake8                # Python linting configuration
├── .gitignore             # Git ignore patterns
├── templates/             # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Homepage
│   ├── examples.html     # Code examples page
│   └── about.html        # About page
├── static/               # Static files
│   └── css/
│       └── style.css     # CSS styles
└── tests/                # Unit tests
    ├── __init__.py       # Tests package initialization
    └── test_app.py       # Flask route tests
```

### Making Changes

To modify the website:

- Edit `app.py` to change routes or add new pages
- Modify templates in the `templates/` directory to change page content
- Update `static/css/style.css` to adjust styling
- Add new dependencies to `requirements.txt` with pinned versions
- Always add tests for new functionality in `tests/`
- Run linting and tests before committing changes

### Contribution Guidelines

1. **Code Quality**
   - Follow PEP 8 style guide
   - Add type hints to all functions
   - Write comprehensive docstrings
   - Keep functions small and focused (max complexity: 10)

2. **Testing**
   - Write unit tests for all new features
   - Ensure all tests pass before submitting
   - Maintain or improve test coverage

3. **Security**
   - Never commit secrets or credentials
   - Validate all user inputs
   - Follow secure coding practices
   - Report security issues per [SECURITY.md](SECURITY.md)

4. **Documentation**
   - Update README for significant changes
   - Document all public APIs
   - Keep dependency documentation current

5. **Dependencies**
   - Pin all versions in requirements.txt
   - Check licenses for compatibility (see [DEPENDENCIES.md](DEPENDENCIES.md))
   - Update dependency documentation when adding/updating packages

### Development Workflow

1. Create a virtual environment and install dependencies
2. Make your changes
3. Run linting: `flake8 app.py tests/`
4. Run tests: `python3 -m unittest discover tests -v`
5. Test the application manually
6. Commit with clear, descriptive messages

## Compliance & Privacy

This project adheres to organizational compliance standards:

- ✅ All code includes comprehensive type hints and docstrings
- ✅ Input validation and error handling implemented
- ✅ All dependencies pinned with documented licenses
- ✅ Security policy documented in SECURITY.md
- ✅ Comprehensive test coverage for all routes
- ✅ Linting enforced with flake8 configuration
- ✅ Secure logging without sensitive information exposure

### Privacy Notice

This application does not:
- Collect personal information
- Use cookies or tracking
- Store user data
- Make external API calls during normal operation

## Security

For security concerns, please review our [Security Policy](SECURITY.md).

To report a vulnerability, please follow the responsible disclosure process outlined in SECURITY.md.

## License

This project is part of the GitHub Copilot Workshop and is provided as an educational resource.

## Support

For questions or issues:
1. Check existing documentation (README, SECURITY.md, DEPENDENCIES.md)
2. Review the code comments and docstrings
3. Run tests to verify functionality
4. Check the security policy for security-related questions

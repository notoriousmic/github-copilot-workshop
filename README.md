# GitHub Copilot Workshop Website

This project contains a basic Python website that showcases GitHub Copilot capabilities. The website demonstrates various features of GitHub Copilot through an interactive web application built with Flask.

## Features

- **Homepage**: Overview of GitHub Copilot features and capabilities
- **Examples Page**: Practical code examples showing how Copilot generates code from natural language prompts
- **About Page**: Information about the workshop and best practices for using Copilot

## Technologies Used

- **Python 3.x**: Backend programming language
- **Flask**: Lightweight web framework
- **HTML/CSS**: Frontend structure and styling
- **Jinja2**: Template engine (included with Flask)

## Installation

1. Make sure you have Python 3.x installed on your system:
   ```bash
   python3 --version
   ```

2. Install the required dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

   Or install Flask directly:
   ```bash
   pip3 install Flask==3.0.0
   ```

## Running the Website

1. Navigate to the project directory:
   ```bash
   cd github-copilot-workshop
   ```

2. Run the Flask application:
   ```bash
   python3 app.py
   ```

   For development with debug mode enabled:
   ```bash
   FLASK_DEBUG=true python3 app.py
   ```

3. Open your web browser and visit:
   ```
   http://localhost:5000
   ```

The website will be running locally on port 5000. You can now explore the different pages to learn about GitHub Copilot capabilities!

## Project Structure

```
github-copilot-workshop/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── templates/             # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Homepage
│   ├── examples.html     # Code examples page
│   └── about.html        # About page
└── static/               # Static files
    └── css/
        └── style.css     # CSS styles
```

## GitHub Copilot Features Showcased

This website demonstrates the following Copilot capabilities:

1. **Code Completion**: Auto-completing code as you type
2. **Natural Language to Code**: Converting comments into working code
3. **Test Generation**: Creating unit tests automatically
4. **Code Refactoring**: Suggesting improvements to code structure
5. **Documentation**: Generating docstrings and comments
6. **Multi-Language Support**: Working across various programming languages

## Development

To modify the website:

- Edit `app.py` to change routes or add new pages
- Modify templates in the `templates/` directory to change page content
- Update `static/css/style.css` to adjust styling
- Add new dependencies to `requirements.txt` as needed

## License

This project is part of the GitHub Copilot Workshop and is provided as an educational resource.

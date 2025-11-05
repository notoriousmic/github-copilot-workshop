## About the Workshop

This project is designed as a workshop to explore and demonstrate the capabilities of GitHub Copilot. It provides hands-on examples and interactive content to help users understand how to effectively use Copilot in their development workflows.

### Workshop Parts

The workshop is divided into the following parts, each represented by a directory under the `workshop/` folder:

1. **GitHub Copilot CLI** (`github-copilot-cli/`):
   - Learn how to use GitHub Copilot in the command line interface.

2. **GitHub Copilot in VS Code** (`github-copilot-vscode/`):
   - Explore how to integrate and use GitHub Copilot within Visual Studio Code.

3. **Advanced GitHub Copilot in VS Code** (`github-copilot-vscode-advanced/`):
   - Dive into advanced features and workflows for using GitHub Copilot in VS Code.

4. **GitHub Copilot Inside GitHub** (`github-copilot-web/`):
   - Understand how to work with copilot on the web

Additionally, there is a `prerequisite.md` file that outlines the requirements and setup instructions for the workshop.
### Workshops Included

1. **Introduction to GitHub Copilot**:
   - Overview of Copilot's features and how it assists in code generation.

2. **Using Copilot for Python Development**:
   - Practical examples of using Copilot to write Python code, including Flask applications.

3. **Debugging with Copilot**:
   - Learn how Copilot can assist in identifying and fixing bugs in your code.

4. **Advanced Copilot Features**:
   - Explore advanced topics like Context Engineering, custom modes etc..


## Project Features

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

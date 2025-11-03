# Security Policy

## Supported Versions

We are committed to maintaining the security of this project. The following versions are currently supported with security updates:

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |

## Reporting a Vulnerability

We take the security of our software seriously. If you believe you have found a security vulnerability in this project, please report it to us responsibly.

### How to Report

**Please do NOT report security vulnerabilities through public GitHub issues.**

Instead, please report security vulnerabilities by:

1. **Email**: Send details to the repository maintainers
2. **Private Security Advisory**: Use GitHub's private vulnerability reporting feature (if enabled)

### What to Include

When reporting a vulnerability, please include:

- A description of the vulnerability and its potential impact
- Steps to reproduce the issue
- Affected versions
- Any potential mitigations you've identified
- Your contact information for follow-up questions

### Response Timeline

- **Acknowledgment**: We will acknowledge receipt of your vulnerability report within 48 hours
- **Assessment**: We will assess the vulnerability and determine its severity within 5 business days
- **Resolution**: We will work on a fix and keep you informed of our progress
- **Disclosure**: Once a fix is available, we will coordinate disclosure timing with you

## Security Best Practices

When using or deploying this application, please follow these security best practices:

### Development Environment

- **Never enable debug mode in production** - Set `FLASK_DEBUG=false` or leave it unset
- Keep all dependencies up to date
- Use virtual environments to isolate dependencies

### Deployment

- Always use HTTPS in production
- Use a production WSGI server (e.g., Gunicorn, uWSGI) instead of Flask's development server
- Implement proper authentication and authorization for any sensitive features
- Set secure HTTP headers (CSP, HSTS, X-Frame-Options, etc.)
- Regularly update dependencies and monitor for security advisories

### Secrets Management

- Never commit secrets, API keys, or credentials to the repository
- Use environment variables or secure secret management systems
- Rotate credentials regularly

## Security Features

This application implements the following security measures:

- Input validation for all user-facing routes
- Comprehensive error handling without exposing sensitive information
- Secure logging that excludes sensitive data
- Type hints and validation to prevent type confusion attacks

## Acknowledgments

We appreciate the security research community's efforts in responsibly disclosing vulnerabilities. Contributors who report valid security issues will be acknowledged (with their permission) in our security advisories.

## Contact

For security-related questions or concerns, please contact the repository maintainers.

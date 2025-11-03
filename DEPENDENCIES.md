# Dependency Licenses

This document lists all third-party dependencies and their licenses for compliance and transparency.

## Direct Dependencies

### Flask 3.0.0
- **License**: BSD-3-Clause
- **Purpose**: Web framework for building the application
- **Source**: https://github.com/pallets/flask
- **License URL**: https://github.com/pallets/flask/blob/main/LICENSE.txt

### Werkzeug 3.0.1
- **License**: BSD-3-Clause
- **Purpose**: WSGI utility library for Python (required by Flask)
- **Source**: https://github.com/pallets/werkzeug
- **License URL**: https://github.com/pallets/werkzeug/blob/main/LICENSE.txt

## Transitive Dependencies

### Jinja2 3.1.2
- **License**: BSD-3-Clause
- **Purpose**: Template engine (required by Flask)
- **Source**: https://github.com/pallets/jinja
- **License URL**: https://github.com/pallets/jinja/blob/main/LICENSE.txt

### itsdangerous 2.2.0
- **License**: BSD-3-Clause
- **Purpose**: Cryptographic signing (required by Flask)
- **Source**: https://github.com/pallets/itsdangerous
- **License URL**: https://github.com/pallets/itsdangerous/blob/main/LICENSE.txt

### MarkupSafe 2.1.5
- **License**: BSD-3-Clause
- **Purpose**: HTML/XML string escaping (required by Jinja2)
- **Source**: https://github.com/pallets/markupsafe
- **License URL**: https://github.com/pallets/markupsafe/blob/main/LICENSE.txt

### click 8.1.6
- **License**: BSD-3-Clause
- **Purpose**: Command-line interface creation (required by Flask)
- **Source**: https://github.com/pallets/click
- **License URL**: https://github.com/pallets/click/blob/main/LICENSE.txt

### blinker 1.7.0
- **License**: MIT
- **Purpose**: Signal/event dispatching (required by Flask)
- **Source**: https://github.com/pallets-eco/blinker
- **License URL**: https://github.com/pallets-eco/blinker/blob/main/LICENSE.txt

## License Compatibility

All dependencies use either **BSD-3-Clause** or **MIT** licenses, which are:
- ✅ Permissive open-source licenses
- ✅ Compatible with commercial use
- ✅ Compatible with this project's educational purpose
- ✅ Allow modification and redistribution with attribution

## Compliance Notes

1. All dependencies are from the trusted Pallets Projects ecosystem
2. No GPL or copyleft licenses that would require this project to adopt those licenses
3. All licenses require attribution, which is maintained in this document
4. No dependencies have known security vulnerabilities at the time of pinning

## Updating Dependencies

When updating dependencies:
1. Check the license hasn't changed: `pip show <package> | grep License`
2. Update this document with new versions and verify license compatibility
3. Run security audits: `pip audit` (if available)
4. Test the application thoroughly after updates

## Last Updated

**Date**: 2025-11-03
**Reviewed by**: GitHub Copilot Workshop Team

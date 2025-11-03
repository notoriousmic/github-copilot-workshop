"""
Unit tests for the GitHub Copilot Workshop Flask application.

This module contains tests for all Flask routes to ensure proper
functionality, error handling, and response validation.
"""

import unittest
from app import app


class TestFlaskRoutes(unittest.TestCase):
    """Test cases for Flask application routes."""

    def setUp(self) -> None:
        """Set up test client before each test."""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def tearDown(self) -> None:
        """Clean up after each test."""
        pass

    def test_index_route_success(self) -> None:
        """Test that the index route returns 200 status code."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_route_contains_features(self) -> None:
        """Test that the index page contains expected Copilot features."""
        response = self.client.get('/')
        data = response.data.decode('utf-8')

        # Check for key feature titles
        self.assertIn('Code Completion', data)
        self.assertIn('Natural Language to Code', data)
        self.assertIn('Test Generation', data)

    def test_examples_route_success(self) -> None:
        """Test that the examples route returns 200 status code."""
        response = self.client.get('/examples')
        self.assertEqual(response.status_code, 200)

    def test_examples_route_contains_code(self) -> None:
        """Test that the examples page contains code examples."""
        response = self.client.get('/examples')
        data = response.data.decode('utf-8')

        # Check for example content
        self.assertIn('Function Generation', data)
        self.assertIn('Data Processing', data)

    def test_about_route_success(self) -> None:
        """Test that the about route returns 200 status code."""
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_404_error_handler(self) -> None:
        """Test that non-existent routes return 404 status code."""
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

    def test_routes_return_html(self) -> None:
        """Test that all main routes return HTML content."""
        routes = ['/', '/examples', '/about']

        for route in routes:
            response = self.client.get(route)
            content_type = response.headers.get('Content-Type', '')
            self.assertIn('text/html', content_type,
                          f"Route {route} should return HTML")

    def test_index_feature_count(self) -> None:
        """Test that index page displays all expected features."""
        response = self.client.get('/')
        data = response.data.decode('utf-8')

        # Verify all expected Copilot features are present on the homepage
        feature_titles = [
            'Code Completion',
            'Natural Language to Code',
            'Test Generation',
            'Code Refactoring',
            'Documentation',
            'Multi-Language Support'
        ]

        for title in feature_titles:
            self.assertIn(title, data,
                          f"Feature '{title}' should be present on "
                          f"index page")


class TestApplicationConfiguration(unittest.TestCase):
    """Test cases for application configuration and setup."""

    def test_app_exists(self) -> None:
        """Test that the Flask app instance exists."""
        self.assertIsNotNone(app)

    def test_testing_mode(self) -> None:
        """Test that testing mode can be enabled."""
        app.config['TESTING'] = True
        self.assertTrue(app.config['TESTING'])


if __name__ == '__main__':
    unittest.main()

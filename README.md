# Playwright Python Training

This repository contains a training project for automated testing using Playwright with Python. The project aims to showcase how to use Playwright for browser automation, write tests using `pytest`, and integrate test reports into GitHub Actions with Allure.

## Features

- **Playwright for Python**: Browser automation with Playwright.
- **Pytest**: Framework for writing and running tests.
- **Allure Report**: Generate beautiful and interactive test reports.
- **GitHub Actions**: Continuous Integration and Deployment for automated tests.
- **GitHub Pages**: Hosting the Allure test report using GitHub Pages.

## Setup Instructions

To get started with the project, follow these steps:

### Prerequisites

1. **Python 3.12+**: Ensure you have Python 3.12 or later installed on your machine.
2. Optional - **Node.js**: Required for running Allure command line tools. (I'm not sure about it, it's only need for GitHub Actions)

### Step 1: Clone the Repository

Clone this repository to your local machine:


```git clone https://github.com/barsovichok/playwright_python_training.git```
```cd playwright_python_training```

### Step 2: Install Dependencies

Install the required Python dependencies:

```pip install -r requirements.txt```

Install the necessary Playwright browsers:

```python3 -m playwright install```

###  Step 3: Run Tests Locally

1) Create .env.dev file
2) Add it to the file

3) Run 
``` TEST_ENV=dev pytest```

This will execute all the test cases, and you will see the results in the terminal.

###  Step 4: View Allure Reports

To generate the Allure report locally, use the following command:

```allure generate allure-results --clean -o allure-report```

This will generate the Allure report in the allure-report directory.

To view the report, you can use:

```allure open allure-report```

### Step 5: Continuous Integration with GitHub Actions

The project is integrated with GitHub Actions for Continuous Integration (CI). Every time a change is pushed to the main branch, tests are executed, and the Allure report is generated.

Once the tests are completed, the Allure report is published to GitHub Pages for easy access:
	•	Test Report: https://barsovichok.github.io/playwright_python_training/

Step 6: Environment Variables

You can set the following environment variables in your .env file or in GitHub Actions secrets:
	•	BASE_URL: The base URL for your application under test.
	•	LOGIN_USER: Username for login.
	•	LOGIN_PASSWORD: Password for login.
	•	TEST_ENV: The environment for the tests (e.g., ‘dev’, ‘prod’).
	•	HEADLESS_MODE: Boolean for running tests in headless mode. (not using now)

### License

This project is licensed under the MIT License.

Feel free to contribute, report issues, or create pull requests to improve the project.

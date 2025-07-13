# Simple Addition Program with GitHub Actions

This repository contains a simple Python program that adds two numbers, along with tests and GitHub Actions workflow for continuous integration.

## Program Overview

The `addition.py` file contains:
- A function `add_numbers(a, b)` that adds two numbers
- Test cases covering various scenarios (positive numbers, negative numbers, zeros, floating point)
- Example usage in the main block

## Running the Program Locally

To run the program locally:

```bash
python addition.py
```

This will execute the addition function with example values and run all tests.

## GitHub Actions Integration

This project uses GitHub Actions for continuous integration. Below are the detailed steps to set up and run the workflow.

### Step 1: Create GitHub Actions Workflow File

Create a directory `.github/workflows` in the root of your repository and add a file named `python-tests.yml`:

```bash
mkdir -p .github/workflows
touch .github/workflows/python-tests.yml
```

### Step 2: Configure the Workflow

Add the following content to the `python-tests.yml` file:

```yaml
name: Python Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    
    - name: Run tests
      run: |
        cd src
        python -m addition
    
    - name: Notify on success
      if: success()
      run: echo "Tests passed successfully!"
```

### Step 3: Push to GitHub

Push your code to GitHub to trigger the workflow:

```bash
git add .
git commit -m "Add addition program with tests and GitHub Actions workflow"
git push origin main
```

### Step 4: Monitor the Workflow

1. Go to your GitHub repository
2. Click on the "Actions" tab
3. You should see your workflow running or completed
4. Click on the workflow run to see detailed logs

### Step 5: Understanding the Workflow

The GitHub Actions workflow does the following:

1. **Triggers**: The workflow runs on push to main branch or when a pull request is made to main
2. **Environment**: Sets up an Ubuntu environment
3. **Steps**:
   - Checks out the code
   - Sets up Python 3.10
   - Installs dependencies (if any requirements.txt exists)
   - Runs the tests in the addition.py file
   - Notifies on success

### Customizing the Workflow

You can customize the workflow by:

- Adding more Python versions to test against
- Adding code coverage reporting
- Setting up notifications for failures
- Adding linting or code quality checks

Example of testing against multiple Python versions:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.8', '3.9', '3.10', '3.11']
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    # Rest of the steps remain the same
```

## Troubleshooting

If your GitHub Actions workflow fails:

1. Check the error logs in the GitHub Actions tab
2. Verify that your tests are passing locally
3. Ensure the file paths in the workflow match your repository structure
4. Check that you're using a compatible Python version

## Next Steps

- Add more complex test cases
- Implement a test framework like pytest
- Add code coverage reporting
- Set up automatic deployment after successful tests

## License

This project is open source and available under the [MIT License](LICENSE).

# GitHub Actions Zero to Hero

This repository demonstrates how to use GitHub Actions with multiple projects in different programming languages. It contains a Python calculator project and a Java application, each with its own CI/CD pipeline.

## Repository Structure

```
/
├── python-project/
│   ├── src/
│   │   └── calculator.py
│   ├── tests/
│   ├── requirements.txt
│   └── README.md
│
├── java-project/
│   ├── src/
│   │   ├── main/java/com/example/app/
│   │   │   └── App.java
│   │   └── test/java/com/example/app/
│   │       └── AppTest.java
│   ├── pom.xml
│   └── README.md
│
└── .github/workflows/
    ├── python-tests.yml
    └── java-ci.yml
```

## Projects

### Python Calculator

A simple calculator application written in Python that supports basic arithmetic operations and includes built-in tests.

[Go to Python Project](./python-project)

### Java Application

A simple Java application that demonstrates Maven build integration with GitHub Actions.

[Go to Java Project](./java-project)

## GitHub Actions Workflows

This repository uses separate GitHub Actions workflows for each project:

1. **Python Tests** - Runs tests for the Python calculator project
   - Triggered on changes to files in the `python-project` directory
   - [Workflow file](./.github/workflows/python-tests.yml)

2. **Java CI with Maven** - Builds and tests the Java application
   - Triggered on changes to files in the `java-project` directory
   - [Workflow file](./.github/workflows/java-ci.yml)

## Benefits of This Structure

- **Separation of concerns**: Each project has its own directory, dependencies, and build process
- **Independent CI/CD**: Changes to one project don't trigger workflows for the other
- **Clear organization**: Easy to understand repository structure
- **Scalability**: Easy to add more projects or languages in the future

## Getting Started

1. Clone this repository
2. Navigate to the project you want to work with
3. Follow the instructions in the project's README.md file

## License

This project is open source and available under the [MIT License](LICENSE).

# Java Application with GitHub Actions

This is a simple Java application that demonstrates the use of GitHub Actions for CI/CD.

## Project Structure

```
java-project/
├── src/
│   ├── main/java/com/example/app/
│   │   └── App.java
│   └── test/java/com/example/app/
│       └── AppTest.java
├── pom.xml
└── README.md
```

## Prerequisites

- Java 11 or higher
- Maven
- Git

## Local Development

1. Build the project:
   ```bash
   cd java-project
   mvn clean package
   ```

2. Run the tests:
   ```bash
   mvn test
   ```

3. Run the application:
   ```bash
   java -jar target/java-github-actions-demo-1.0-SNAPSHOT.jar
   ```

## GitHub Actions Workflow

The project includes a GitHub Actions workflow that:

1. Triggers on:
   - Push to main branch
   - Pull requests to main branch

2. Workflow steps:
   - Checks out the code
   - Sets up JDK 11
   - Builds the project with Maven
   - Runs tests
   - Uploads the built JAR as an artifact

## Workflow File

The workflow is defined in `.github/workflows/java-ci.yml`.

## Making Changes

1. Create a new branch
2. Make your changes
3. Commit and push
4. Create a Pull Request on GitHub
5. GitHub Actions will automatically run the CI pipeline

## Troubleshooting

If the build fails:
1. Check the Actions tab for detailed error logs
2. Verify Java version compatibility
3. Ensure all tests are passing locally
4. Verify pom.xml dependencies

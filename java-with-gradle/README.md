# Java with Gradle Project

This is a simple Java application built with Gradle. It demonstrates how to set up a Java project with Gradle and integrate it with GitHub Actions for continuous integration.

## Project Structure

```
java-with-gradle/
├── src/
│   ├── main/java/com/example/app/
│   │   └── Application.java
│   └── test/java/com/example/app/
│       └── ApplicationTest.java
├── build.gradle
├── gradlew
├── gradlew.bat
└── gradle/wrapper/
    └── gradle-wrapper.properties
```

## Prerequisites

- Java 11 or higher
- Gradle (optional, as the project includes Gradle Wrapper)

## Building the Project

You can build the project using the included Gradle Wrapper:

```bash
# On Linux/macOS
./gradlew build

# On Windows
gradlew.bat build
```

## Running Tests

To run the tests:

```bash
# On Linux/macOS
./gradlew test

# On Windows
gradlew.bat test
```

## Running the Application

To run the application:

```bash
# On Linux/macOS
./gradlew run

# On Windows
gradlew.bat run
```

## GitHub Actions Integration

This project includes a GitHub Actions workflow that automatically builds and tests the application on every push and pull request to the repository.

See the workflow file at `.github/workflows/gradle-ci.yml` for details.

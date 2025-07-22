# GitHub Actions Zero to Hero

This repository demonstrates how to use GitHub Actions with multiple projects in different programming languages. It contains a Python calculator project, a Java application with Maven, and a Java application with Gradle, each with its own CI/CD pipeline.

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
├── java-with-gradle/
│   ├── src/
│   │   ├── main/java/com/example/app/
│   │   │   └── Application.java
│   │   └── test/java/com/example/app/
│   │       └── ApplicationTest.java
│   ├── build.gradle
│   ├── gradlew
│   ├── gradlew.bat
│   └── gradle/wrapper/
│       └── gradle-wrapper.properties
│
└── .github/workflows/
    ├── python-tests.yml
    ├── java-ci.yml
    └── gradle-ci.yml
```

## Projects

### Python Calculator

A simple calculator application written in Python that supports basic arithmetic operations and includes built-in tests.

[Go to Python Project](./python-project)

### Java Application with Maven

A simple Java application that demonstrates Maven build integration with GitHub Actions.

[Go to Java Project](./java-project)

### Java Application with Gradle

A simple Java application that demonstrates Gradle build integration with GitHub Actions.

[Go to Java with Gradle Project](./java-with-gradle)

## GitHub Actions Workflows

This repository uses separate GitHub Actions workflows for each project:

1. **Python Tests** - Runs tests for the Python calculator project
   - Triggered on changes to files in the `python-project` directory
   - [Workflow file](./.github/workflows/python-tests.yml)

2. **Java CI with Maven** - Builds and tests the Java application with Maven
   - Triggered on changes to files in the `java-project` directory
   - [Workflow file](./.github/workflows/java-ci.yml)

3. **Java CI with Gradle** - Builds and tests the Java application with Gradle
   - Triggered on changes to files in the `java-with-gradle` directory
   - [Workflow file](./.github/workflows/gradle-ci.yml)

## Benefits of This Structure

- **Separation of concerns**: Each project has its own directory, dependencies, and build process
- **Independent CI/CD**: Changes to one project don't trigger workflows for the other
- **Clear organization**: Easy to understand repository structure
- **Scalability**: Easy to add more projects or languages in the future

## Getting Started

1. Clone this repository
2. Navigate to the project you want to work with
3. Follow the instructions in the project's README.md file

## Building a Java Application with Gradle

### What is Gradle?

Gradle is a build automation tool that supports multi-language development. It controls the development process in the tasks of compilation and packaging to testing, deployment, and publishing. Gradle was designed for multi-project builds, which can grow to be quite large.

### Key Gradle Concepts

1. **Project**: A project represents something to be built, like a library or application.
2. **Task**: A task represents a single atomic piece of work for a build, like compiling classes or creating a JAR.
3. **Plugin**: Plugins extend the Gradle model by adding tasks, configurations, dependencies, and more.
4. **Dependency Management**: Gradle handles dependencies through configurations, repositories, and artifacts.
5. **Build Script**: Written in Groovy or Kotlin DSL, defines the project and its tasks.

### Gradle vs Maven

| Feature | Gradle | Maven |
|---------|--------|-------|
| Build Script | Groovy/Kotlin DSL | XML |
| Performance | Faster due to incremental builds and build cache | Generally slower |
| Flexibility | Highly customizable | More rigid, convention-based |
| Learning Curve | Steeper | Gentler |
| Dependency Management | Similar to Maven | Industry standard |
| Plugin Ecosystem | Growing | Extensive |

### Steps to Build a Java App with Gradle

1. **Set up project structure**:
   ```
   project-root/
   ├── src/main/java/        # Application source code
   ├── src/test/java/        # Test source code
   ├── build.gradle          # Build configuration
   └── settings.gradle       # Project settings
   ```

2. **Create build.gradle file**:
   ```groovy
   plugins {
       id 'java'
       id 'application'
   }
   
   repositories {
       mavenCentral()
   }
   
   dependencies {
       testImplementation 'org.junit.jupiter:junit-jupiter:5.9.1'
   }
   
   application {
       mainClass = 'com.example.app.Application'
   }
   ```

3. **Add Gradle Wrapper** (recommended):
   ```bash
   gradle wrapper
   ```
   This creates gradlew and gradlew.bat scripts that allow building the project without having Gradle installed.

4. **Build the project**:
   ```bash
   ./gradlew build
   ```

5. **Run tests**:
   ```bash
   ./gradlew test
   ```

6. **Run the application**:
   ```bash
   ./gradlew run
   ```

### GitHub Actions Integration

GitHub Actions can automate the build, test, and deployment process for Gradle projects. The workflow typically includes:

1. Checking out the code
2. Setting up Java
3. Validating the Gradle wrapper
4. Building with Gradle
5. Running tests
6. Publishing artifacts

See the [gradle-ci.yml](./.github/workflows/gradle-ci.yml) workflow for a complete example.

## License

This project is open source and available under the [MIT License](LICENSE).

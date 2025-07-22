package com.example.app;

public class Application {
    public String getGreeting() {
        return "Hello, Prosper This is your JAVA Application!";
    }

    public static void main(String[] args) {
        System.out.println(new Application().getGreeting());
    }
}

package com.example.app;

public class Application {
    public String getGreeting() {
        return "Hello, Prosper This is your Java Application for your github action test project!";
    }

    public static void main(String[] args) {
        System.out.println(new Application().getGreeting());
    }
}

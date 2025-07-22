package com.example.app;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ApplicationTest {
    @Test
    public void testAppHasGreeting() {
        Application classUnderTest = new Application();
        assertNotNull(classUnderTest.getGreeting(), "Application should have a greeting");
        assertEquals("Hello, World!", classUnderTest.getGreeting(), "Greeting should match expected value");
    }
}

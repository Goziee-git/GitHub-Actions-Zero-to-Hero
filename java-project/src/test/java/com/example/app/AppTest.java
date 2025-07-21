package com.example.app;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class AppTest {
    @Test
    public void testGetGreeting() {
        App app = new App();
        assertEquals("Hello from Java GitHub Actions!", app.getGreeting());
    }
}

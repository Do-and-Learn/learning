package org.lee.teddy;

import org.junit.Before;
import org.junit.Test;
import org.lee.teddy.web.HomeController;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.setup.MockMvcBuilders.standaloneSetup;

public class HomeControllerTest {

    private MockMvc mockMvc;

    @Before
    public void setUp() {
        mockMvc = standaloneSetup(new HomeController()).build();
    }

    @Test
    public void testValidate() throws Exception {
        mockMvc.perform(post("/")).andExpect(content().string("true"));
    }
}

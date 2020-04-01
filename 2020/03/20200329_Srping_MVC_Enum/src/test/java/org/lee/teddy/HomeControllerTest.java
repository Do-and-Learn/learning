package org.lee.teddy;

import org.junit.Before;
import org.junit.Test;
import org.lee.teddy.web.HomeController;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.put;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;
import static org.springframework.test.web.servlet.setup.MockMvcBuilders.standaloneSetup;

public class HomeControllerTest {

    private MockMvc mockMvc;

    @Before
    public void setUp() {
        mockMvc = standaloneSetup(new HomeController()).build();
    }

    @Test
    public void testHello() throws Exception {
        mockMvc.perform(put("/")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"userName\": \"Teddy\"}"))
                .andDo(print())
                .andExpect(status().is(200))
                .andExpect(content().string("Hello Teddy"));
    }

    @Test
    public void testSex() throws Exception {
        mockMvc.perform(put("/")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"userName\": \"Teddy\", \"sex\": \"Boy\"}"))
                .andDo(print())
                .andExpect(status().is(200))
                .andExpect(content().string("Hello Teddy (Boy)"));
    }

    @Test
    public void testAllSmallCase() throws Exception {
        mockMvc.perform(put("/")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"userName\": \"Teddy\", \"sex\": \"boy\"}"))
                .andDo(print())
                .andExpect(status().is(200))
                .andExpect(content().string("Hello Teddy (Boy)"));
    }

    @Test
    public void testWrongSex() throws Exception {
        mockMvc.perform(put("/")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"userName\": \"Teddy\", \"sex\": \"XXx\"}"))
                .andDo(print())
                .andExpect(status().is(HttpStatus.BAD_REQUEST.value()))
                .andExpect(content().string("Cannot deserialize value from String [XXx]: value not noe of [Boy, Girl, None]"));
    }
}

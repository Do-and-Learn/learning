package org.lee.teddy;

import org.junit.Before;
import org.junit.Test;
import org.lee.teddy.web.HomeController;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.web.servlet.view.InternalResourceView;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;
import static org.springframework.test.web.servlet.setup.MockMvcBuilders.standaloneSetup;

public class HomeControllerTest {

    private MockMvc mockMvc;

    @Before
    public void setUp() {
        mockMvc = standaloneSetup(new HomeController()).setSingleView(new InternalResourceView("/WEB-INF/views/hello.jsp")).build();
//        mockMvc = standaloneSetup(new HomeController()).build();
    }

    @Test
    public void testHomePage() throws Exception {
        mockMvc.perform(get("/")).andExpect(content().string("Hello world!"));
    }

    @Test
    public void testHello() throws Exception {
        mockMvc.perform(get("/hello"))
                .andDo(print())
                .andExpect(view().name("hello"))
                .andExpect(content().string("")) // Cannot assert content of JSP: https://stackoverflow.com/questions/28944538/empty-content-in-spring-mvc-test
                .andExpect(forwardedUrl("/WEB-INF/views/hello.jsp"));
    }

}

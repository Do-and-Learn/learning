package org.lee.teddy.web;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import static org.springframework.web.bind.annotation.RequestMethod.GET;

@Controller
public class HomeController {

    @RequestMapping(value = "/", method = GET)
    @ResponseBody
    public String index() {
        return "Hello world!";
    }

    @RequestMapping(value = "/hello", method = GET)
    public String hello() {
        return "hello";
    }
}

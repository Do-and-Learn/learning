package org.lee.teddy.web;

import org.lee.teddy.model.User;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import static org.springframework.web.bind.annotation.RequestMethod.GET;
import static org.springframework.web.bind.annotation.RequestMethod.POST;

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

    @RequestMapping(value = "/hello", method = POST)
    public String postHello(User user, Model model) {
        model.addAttribute(user);
        return "hello";
    }
}

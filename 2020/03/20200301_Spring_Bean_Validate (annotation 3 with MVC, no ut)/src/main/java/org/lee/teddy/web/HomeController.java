package org.lee.teddy.web;

import org.lee.teddy.Person;
import org.springframework.stereotype.Controller;
import org.springframework.validation.Errors;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.validation.Valid;

import static org.springframework.web.bind.annotation.RequestMethod.POST;

@Controller
public class HomeController {

    @RequestMapping(value = "/", method = POST)
    @ResponseBody
    public String post(@Valid Person person, Errors errors) {
        return String.valueOf(errors.hasErrors());
    }
}

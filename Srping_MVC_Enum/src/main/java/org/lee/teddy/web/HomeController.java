package org.lee.teddy.web;

import com.fasterxml.jackson.databind.exc.InvalidDefinitionException;
import org.lee.teddy.model.User;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import static org.springframework.web.bind.annotation.RequestMethod.PUT;

@RestController
public class HomeController {

    @RequestMapping(value = "/", method = PUT, consumes = MediaType.APPLICATION_JSON_VALUE)
    public String user(@RequestBody User user) {
        StringBuilder sb = new StringBuilder();
        sb.append("Hello ").append(user.getUserName());
        if (user.getSex() != null)
            sb.append(" (").append(user.getSex()).append(")");
        return sb.toString();
    }

    @ExceptionHandler(InvalidDefinitionException.class)
    protected Object handleHttpMessageNotReadableException(InvalidDefinitionException e) {
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getCause().getMessage());
    }
}

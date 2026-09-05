package com.crms.crms.controller;

import com.crms.crms.service.authservice;
import com.crms.crms.dto.loginrequest;
import com.crms.crms.dto.loginresponse;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping("/api/auth")
@CrossOrigin(origins = "*")
public class authcontroller {
    private final authservice authservice;
    public  authcontroller(authservice authservice)
    {
        this.authservice=authservice;
    }
    @PostMapping("/login")
    public ResponseEntity<loginresponse> login (@RequestBody loginrequest loginrequest)
    {
        loginresponse loginresponse = authservice.login(
        loginrequest.getIdentifier(),
        loginrequest.getPassword()
        );
        if(loginresponse.isSuccess())
        {
            return  ResponseEntity.ok(loginresponse);
        }
        return ResponseEntity.status(401).body(loginresponse);
    }
}

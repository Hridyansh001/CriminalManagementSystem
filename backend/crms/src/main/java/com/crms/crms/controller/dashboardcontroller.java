package com.crms.crms.controller;

import com.crms.crms.dto.dashboardresponse;
import com.crms.crms.service.dashboardservice;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/dashboard")
@CrossOrigin(origins = "*")
public class dashboardcontroller {

    private final dashboardservice dashboardservice;

    public dashboardcontroller(dashboardservice dashboardservice) {
        this.dashboardservice = dashboardservice;
    }

    @GetMapping
    public ResponseEntity<dashboardresponse> getDashboard() {

        return ResponseEntity.ok(
                dashboardservice.getDashboardData()
        );
    }
}
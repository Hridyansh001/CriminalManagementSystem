package com.crms.crms.controller;

import com.crms.crms.entity.court;
import com.crms.crms.service.courtservice;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/courts")
@CrossOrigin(origins = "*")
public class courtcontroller {

    private final courtservice courtservice;

    public courtcontroller(courtservice courtservice) {
        this.courtservice = courtservice;
    }

    @GetMapping
    public List<court> getAllCourts() {
        return courtservice.getAllCourts();
    }

    @GetMapping("/{id}")
    public ResponseEntity<court> getCourtById(@PathVariable Integer id) {
        return courtservice.getCourtById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<court> createCourt(@RequestBody court c) {
        court saved = courtservice.createCourt(c);
        return ResponseEntity.ok(saved);
    }

    @PostMapping("/{id}")
    public ResponseEntity<court> updateCourt(@PathVariable Integer id, @RequestBody court c) {
        court updated = courtservice.updateCourt(c, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @PutMapping("/{id}")
    public ResponseEntity<court> updateCourtPut(@PathVariable Integer id, @RequestBody court c) {
        court updated = courtservice.updateCourt(c, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteCourt(@PathVariable Integer id) {
        courtservice.deleteCourt(id);
        return ResponseEntity.noContent().build();
    }
}

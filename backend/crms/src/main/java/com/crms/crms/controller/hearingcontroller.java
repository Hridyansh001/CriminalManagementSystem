package com.crms.crms.controller;

import com.crms.crms.entity.hearing;
import com.crms.crms.service.hearingservice;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/hearings")
@CrossOrigin(origins = "*")
public class hearingcontroller {

    private final hearingservice hearingservice;

    public hearingcontroller(hearingservice hearingservice) {
        this.hearingservice = hearingservice;
    }

    @GetMapping
    public List<hearing> getAllHearings() {
        return hearingservice.getAllHearings();
    }

    @GetMapping("/{id}")
    public ResponseEntity<hearing> getHearingById(@PathVariable Integer id) {
        return hearingservice.getHearingById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/case/{caseId}")
    public List<hearing> getHearingsByCaseId(@PathVariable Integer caseId) {
        return hearingservice.getHearingsByCaseId(caseId);
    }

    @PostMapping
    public ResponseEntity<hearing> createHearing(@RequestBody hearing h) {
        hearing saved = hearingservice.createHearing(h);
        return ResponseEntity.ok(saved);
    }

    @PostMapping("/{id}")
    public ResponseEntity<hearing> updateHearing(@PathVariable Integer id, @RequestBody hearing h) {
        hearing updated = hearingservice.updateHearing(h, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @PutMapping("/{id}")
    public ResponseEntity<hearing> updateHearingPut(@PathVariable Integer id, @RequestBody hearing h) {
        hearing updated = hearingservice.updateHearing(h, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteHearing(@PathVariable Integer id) {
        hearingservice.deleteHearing(id);
        return ResponseEntity.noContent().build();
    }
}

package com.crms.crms.controller;

import com.crms.crms.entity.courtcase;
import com.crms.crms.service.caseservice;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/cases")
@CrossOrigin(origins = "*")
public class casecontroller {

    private final caseservice caseservice;

    public casecontroller(caseservice caseservice) {
        this.caseservice = caseservice;
    }

    @GetMapping
    public List<courtcase> getAllCases() {
        return caseservice.getAllCases();
    }

    @GetMapping("/{id}")
    public ResponseEntity<courtcase> getCaseById(@PathVariable Integer id) {
        return caseservice.getCaseById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/number/{caseNumber}")
    public ResponseEntity<courtcase> getCaseByNumber(@PathVariable String caseNumber) {
        return caseservice.getCaseByCaseNumber(caseNumber)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/fir/{firId}")
    public ResponseEntity<courtcase> getCaseByFirId(@PathVariable Integer firId) {
        return caseservice.getCaseByFirId(firId)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/court/{courtId}")
    public List<courtcase> getCasesByCourtId(@PathVariable Integer courtId) {
        return caseservice.getCasesByCourtId(courtId);
    }

    @PostMapping
    public ResponseEntity<courtcase> createCase(@RequestBody courtcase c) {
        courtcase saved = caseservice.createCase(c);
        return ResponseEntity.ok(saved);
    }

    @PostMapping("/{id}")
    public ResponseEntity<courtcase> updateCase(@PathVariable Integer id, @RequestBody courtcase c) {
        courtcase updated = caseservice.updateCase(c, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @PutMapping("/{id}")
    public ResponseEntity<courtcase> updateCasePut(@PathVariable Integer id, @RequestBody courtcase c) {
        courtcase updated = caseservice.updateCase(c, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteCase(@PathVariable Integer id) {
        caseservice.deleteCase(id);
        return ResponseEntity.noContent().build();
    }
}

package com.crms.crms.controller;

import com.crms.crms.entity.investigation;
import com.crms.crms.service.investigationservice;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/investigations")
@CrossOrigin(origins = "*")
public class investigationcontroller {

    private final investigationservice investigationservice;

    public investigationcontroller(investigationservice investigationservice) {
        this.investigationservice = investigationservice;
    }

    @GetMapping
    public List<investigation> getAllInvestigations() {
        return investigationservice.getAllInvestigations();
    }

    @GetMapping("/{id}")
    public ResponseEntity<investigation> getInvestigationById(@PathVariable Integer id) {
        return investigationservice.getInvestigationById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/fir/{firId}")
    public ResponseEntity<investigation> getInvestigationByFirId(@PathVariable Integer firId) {
        return investigationservice.getInvestigationByFirId(firId)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/police/{policeId}")
    public List<investigation> getInvestigationsByPoliceId(@PathVariable Integer policeId) {
        return investigationservice.getInvestigationsByPoliceId(policeId);
    }

    @PostMapping
    public ResponseEntity<investigation> createInvestigation(@RequestBody investigation inv) {
        investigation saved = investigationservice.createInvestigation(inv);
        return ResponseEntity.ok(saved);
    }

    @PostMapping("/{id}")
    public ResponseEntity<investigation> updateInvestigation(@PathVariable Integer id, @RequestBody investigation inv) {
        investigation updated = investigationservice.updateInvestigation(inv, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @PutMapping("/{id}")
    public ResponseEntity<investigation> updateInvestigationPut(@PathVariable Integer id, @RequestBody investigation inv) {
        investigation updated = investigationservice.updateInvestigation(inv, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteInvestigation(@PathVariable Integer id) {
        investigationservice.deleteInvestigation(id);
        return ResponseEntity.noContent().build();
    }
}

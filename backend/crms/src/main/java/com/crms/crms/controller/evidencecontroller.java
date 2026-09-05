package com.crms.crms.controller;

import com.crms.crms.entity.evidence;
import com.crms.crms.service.evidenceservice;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/evidences")
@CrossOrigin(origins = "*")
public class evidencecontroller {

    private final evidenceservice evidenceservice;

    public evidencecontroller(evidenceservice evidenceservice) {
        this.evidenceservice = evidenceservice;
    }

    @GetMapping
    public List<evidence> getAllEvidences() {
        return evidenceservice.getAllEvidences();
    }

    @GetMapping("/{id}")
    public ResponseEntity<evidence> getEvidenceById(@PathVariable Integer id) {
        return evidenceservice.getEvidenceById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/fir/{firId}")
    public List<evidence> getEvidencesByFirId(@PathVariable Integer firId) {
        return evidenceservice.getEvidencesByFirId(firId);
    }

    @GetMapping("/collected-by/{policeId}")
    public List<evidence> getEvidencesByCollectedBy(@PathVariable Integer policeId) {
        return evidenceservice.getEvidencesByCollectedBy(policeId);
    }

    @PostMapping
    public ResponseEntity<evidence> createEvidence(@RequestBody evidence ev) {
        evidence saved = evidenceservice.createEvidence(ev);
        return ResponseEntity.ok(saved);
    }

    @PostMapping("/{id}")
    public ResponseEntity<evidence> updateEvidence(@PathVariable Integer id, @RequestBody evidence ev) {
        evidence updated = evidenceservice.updateEvidence(ev, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @PutMapping("/{id}")
    public ResponseEntity<evidence> updateEvidencePut(@PathVariable Integer id, @RequestBody evidence ev) {
        evidence updated = evidenceservice.updateEvidence(ev, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteEvidence(@PathVariable Integer id) {
        evidenceservice.deleteEvidence(id);
        return ResponseEntity.noContent().build();
    }
}

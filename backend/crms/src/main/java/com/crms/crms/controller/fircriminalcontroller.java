package com.crms.crms.controller;

import com.crms.crms.entity.fircriminal;
import com.crms.crms.service.fircriminalservice;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/fircriminals")
@CrossOrigin(origins = "*")
public class fircriminalcontroller {

    private final fircriminalservice fircriminalservice;

    public fircriminalcontroller(fircriminalservice fircriminalservice) {
        this.fircriminalservice = fircriminalservice;
    }

    @GetMapping
    public List<fircriminal> getAllFirCriminals() {
        return fircriminalservice.getAllFirCriminals();
    }

    @GetMapping("/{firId}/{criminalId}")
    public ResponseEntity<fircriminal> getFirCriminalById(@PathVariable Integer firId, @PathVariable Integer criminalId) {
        return fircriminalservice.getFirCriminalById(firId, criminalId)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/fir/{firId}")
    public List<fircriminal> getByFirId(@PathVariable Integer firId) {
        return fircriminalservice.getByFirId(firId);
    }

    @GetMapping("/criminal/{criminalId}")
    public List<fircriminal> getByCriminalId(@PathVariable Integer criminalId) {
        return fircriminalservice.getByCriminalId(criminalId);
    }

    @PostMapping
    public ResponseEntity<fircriminal> createFirCriminal(@RequestBody fircriminal fc) {
        fircriminal saved = fircriminalservice.createFirCriminal(fc);
        return ResponseEntity.ok(saved);
    }

    @PostMapping("/{firId}/{criminalId}")
    public ResponseEntity<fircriminal> updateFirCriminal(@PathVariable Integer firId, @PathVariable Integer criminalId, @RequestBody fircriminal fc) {
        fircriminal updated = fircriminalservice.updateFirCriminal(fc, firId, criminalId);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @PutMapping("/{firId}/{criminalId}")
    public ResponseEntity<fircriminal> updateFirCriminalPut(@PathVariable Integer firId, @PathVariable Integer criminalId, @RequestBody fircriminal fc) {
        fircriminal updated = fircriminalservice.updateFirCriminal(fc, firId, criminalId);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @DeleteMapping("/{firId}/{criminalId}")
    public ResponseEntity<Void> deleteFirCriminal(@PathVariable Integer firId, @PathVariable Integer criminalId) {
        fircriminalservice.deleteFirCriminal(firId, criminalId);
        return ResponseEntity.noContent().build();
    }
}

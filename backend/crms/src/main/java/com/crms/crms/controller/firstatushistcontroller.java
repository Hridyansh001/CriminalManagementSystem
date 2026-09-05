package com.crms.crms.controller;

import com.crms.crms.entity.firstatushist;
import com.crms.crms.service.firstatushistservice;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/firstatushistory")
@CrossOrigin(origins = "*")
public class firstatushistcontroller {

    private final firstatushistservice firstatushistservice;

    public firstatushistcontroller(firstatushistservice firstatushistservice) {
        this.firstatushistservice = firstatushistservice;
    }

    @GetMapping
    public List<firstatushist> getAllStatusHistories() {
        return firstatushistservice.getAllStatusHistories();
    }

    @GetMapping("/{id}")
    public ResponseEntity<firstatushist> getStatusHistoryById(@PathVariable Integer id) {
        return firstatushistservice.getStatusHistoryById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/fir/{firId}")
    public List<firstatushist> getStatusHistoriesByFirId(@PathVariable Integer firId) {
        return firstatushistservice.getStatusHistoriesByFirId(firId);
    }

    @PostMapping
    public ResponseEntity<firstatushist> createStatusHistory(@RequestBody firstatushist history) {
        firstatushist saved = firstatushistservice.createStatusHistory(history);
        return ResponseEntity.ok(saved);
    }

    @PostMapping("/{id}")
    public ResponseEntity<firstatushist> updateStatusHistory(@PathVariable Integer id, @RequestBody firstatushist history) {
        firstatushist updated = firstatushistservice.updateStatusHistory(history, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @PutMapping("/{id}")
    public ResponseEntity<firstatushist> updateStatusHistoryPut(@PathVariable Integer id, @RequestBody firstatushist history) {
        firstatushist updated = firstatushistservice.updateStatusHistory(history, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteStatusHistory(@PathVariable Integer id) {
        firstatushistservice.deleteStatusHistory(id);
        return ResponseEntity.noContent().build();
    }
}

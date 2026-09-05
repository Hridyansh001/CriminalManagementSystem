package com.crms.crms.controller;

import com.crms.crms.entity.police;
import com.crms.crms.service.policeservice;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/police")
@CrossOrigin(origins = "*")
public class policecontroller {

    private final policeservice policeservice;

    public policecontroller(policeservice policeservice) {
        this.policeservice = policeservice;
    }

    @GetMapping
    public List<police> getAllPolice() {
        return policeservice.getAllPolice();
    }

    @GetMapping("/{id}")
    public ResponseEntity<police> getPoliceById(@PathVariable Integer id) {
        return policeservice.getPoliceById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<police> createPolice(@RequestBody police p) {
        police savedPolice = policeservice.createPolice(p);
        return ResponseEntity.ok(savedPolice);
    }

    @PostMapping("/{id}")
    public ResponseEntity<police> updatePolice(@PathVariable Integer id, @RequestBody police p) {
        police updated = policeservice.updatePolice(p, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @PutMapping("/{id}")
    public ResponseEntity<police> updatePolicePut(@PathVariable Integer id, @RequestBody police p) {
        police updated = policeservice.updatePolice(p, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deletePolice(@PathVariable Integer id) {
        policeservice.deletePolice(id);
        return ResponseEntity.noContent().build();
    }
}

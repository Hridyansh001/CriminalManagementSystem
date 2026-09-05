package com.crms.crms.controller;

import com.crms.crms.entity.crimnal;
import com.crms.crms.service.criminalservice;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/criminals")
@CrossOrigin(origins = "*")
public class criminalcontroller {

    private final criminalservice criminalservice;

    public criminalcontroller(criminalservice criminalservice) {
        this.criminalservice = criminalservice;
    }

    @GetMapping
    public List<crimnal> getAllCriminals() {
        return criminalservice.getAllCriminals();
    }

    @GetMapping("/{id}")
    public ResponseEntity<crimnal> getCriminalById(@PathVariable Integer id) {
        return criminalservice.getCriminalById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<crimnal> createCriminal(@RequestBody crimnal c) {
        crimnal saved = criminalservice.createCriminal(c);
        return ResponseEntity.ok(saved);
    }

    @PostMapping("/{id}")
    public ResponseEntity<crimnal> updateCriminal(@PathVariable Integer id, @RequestBody crimnal c) {
        crimnal updated = criminalservice.updateCriminal(c, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @PutMapping("/{id}")
    public ResponseEntity<crimnal> updateCriminalPut(@PathVariable Integer id, @RequestBody crimnal c) {
        crimnal updated = criminalservice.updateCriminal(c, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteCriminal(@PathVariable Integer id) {
        criminalservice.deleteCriminal(id);
        return ResponseEntity.noContent().build();
    }
}

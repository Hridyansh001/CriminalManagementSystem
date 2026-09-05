package com.crms.crms.controller;

import com.crms.crms.entity.policestation;
import com.crms.crms.service.policestationservice;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/policestations")
@CrossOrigin(origins = "*")
public class policestationcontroller {

    private final policestationservice policestationservice;

    public policestationcontroller(policestationservice policestationservice) {
        this.policestationservice = policestationservice;
    }

    @GetMapping
    public List<policestation> getAllPoliceStations() {
        return policestationservice.getAllPoliceStations();
    }

    @GetMapping("/{id}")
    public ResponseEntity<policestation> getPoliceStationById(@PathVariable Integer id) {
        return policestationservice.getPoliceStationById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<policestation> createPoliceStation(@RequestBody policestation ps) {
        policestation savedPs = policestationservice.createPoliceStation(ps);
        return ResponseEntity.ok(savedPs);
    }

    @PostMapping("/{id}")
    public ResponseEntity<policestation> updatePoliceStation(@PathVariable Integer id, @RequestBody policestation ps) {
        policestation updated = policestationservice.updatePoliceStation(ps, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @PutMapping("/{id}")
    public ResponseEntity<policestation> updatePoliceStationPut(@PathVariable Integer id, @RequestBody policestation ps) {
        policestation updated = policestationservice.updatePoliceStation(ps, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deletePoliceStation(@PathVariable Integer id) {
        policestationservice.deletePoliceStation(id);
        return ResponseEntity.noContent().build();
    }
}

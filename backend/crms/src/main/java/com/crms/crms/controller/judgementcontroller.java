package com.crms.crms.controller;

import com.crms.crms.entity.judgement;
import com.crms.crms.service.judgementservice;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/judgments")
@CrossOrigin(origins = "*")
public class judgementcontroller {

    private final judgementservice judgementservice;

    public judgementcontroller(judgementservice judgementservice) {
        this.judgementservice = judgementservice;
    }

    @GetMapping
    public List<judgement> getAllJudgments() {
        return judgementservice.getAllJudgments();
    }

    @GetMapping("/{id}")
    public ResponseEntity<judgement> getJudgmentById(@PathVariable Integer id) {
        return judgementservice.getJudgmentById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/case/{caseId}")
    public ResponseEntity<judgement> getJudgmentByCaseId(@PathVariable Integer caseId) {
        return judgementservice.getJudgmentByCaseId(caseId)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<judgement> createJudgment(@RequestBody judgement j) {
        judgement saved = judgementservice.createJudgment(j);
        return ResponseEntity.ok(saved);
    }

    @PostMapping("/{id}")
    public ResponseEntity<judgement> updateJudgment(@PathVariable Integer id, @RequestBody judgement j) {
        judgement updated = judgementservice.updateJudgment(j, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @PutMapping("/{id}")
    public ResponseEntity<judgement> updateJudgmentPut(@PathVariable Integer id, @RequestBody judgement j) {
        judgement updated = judgementservice.updateJudgment(j, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteJudgment(@PathVariable Integer id) {
        judgementservice.deleteJudgment(id);
        return ResponseEntity.noContent().build();
    }
}

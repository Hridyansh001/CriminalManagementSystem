package com.crms.crms.service;

import com.crms.crms.entity.judgement;
import com.crms.crms.repository.judgementrepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class judgementservice {

    private final judgementrepository judgementrepository;

    public judgementservice(judgementrepository judgementrepository) {
        this.judgementrepository = judgementrepository;
    }

    public List<judgement> getAllJudgments() {
        return judgementrepository.findAll();
    }

    public Optional<judgement> getJudgmentById(Integer id) {
        return judgementrepository.findById(id);
    }

    public Optional<judgement> getJudgmentByCaseId(Integer caseId) {
        return judgementrepository.findByCaseId(caseId);
    }

    public judgement createJudgment(judgement j) {
        return judgementrepository.save(j);
    }

    public judgement updateJudgment(judgement updatedJ, Integer id) {
        Optional<judgement> existing = judgementrepository.findById(id);
        if (existing.isPresent()) {
            judgement j = existing.get();
            j.setCaseId(updatedJ.getCaseId());
            j.setJudgmentDate(updatedJ.getJudgmentDate());
            j.setDecision(updatedJ.getDecision());
            j.setBasis(updatedJ.getBasis());
            j.setSentence(updatedJ.getSentence());
            j.setRemarks(updatedJ.getRemarks());
            return judgementrepository.save(j);
        }
        return null;
    }

    public void deleteJudgment(Integer id) {
        judgementrepository.deleteById(id);
    }
}

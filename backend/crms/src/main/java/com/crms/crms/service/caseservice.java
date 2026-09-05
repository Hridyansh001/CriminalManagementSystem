package com.crms.crms.service;

import com.crms.crms.entity.courtcase;
import com.crms.crms.repository.caserepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class caseservice {

    private final caserepository caserepository;

    public caseservice(caserepository caserepository) {
        this.caserepository = caserepository;
    }

    public List<courtcase> getAllCases() {
        return caserepository.findAll();
    }

    public Optional<courtcase> getCaseById(Integer id) {
        return caserepository.findById(id);
    }

    public Optional<courtcase> getCaseByCaseNumber(String caseNumber) {
        return caserepository.findByCaseNumber(caseNumber);
    }

    public Optional<courtcase> getCaseByFirId(Integer firId) {
        return caserepository.findByFirId(firId);
    }

    public List<courtcase> getCasesByCourtId(Integer courtId) {
        return caserepository.findByCourtId(courtId);
    }

    public courtcase createCase(courtcase c) {
        return caserepository.save(c);
    }

    public courtcase updateCase(courtcase updatedC, Integer id) {
        Optional<courtcase> existing = caserepository.findById(id);
        if (existing.isPresent()) {
            courtcase c = existing.get();
            c.setFirId(updatedC.getFirId());
            c.setCourtId(updatedC.getCourtId());
            c.setCaseNumber(updatedC.getCaseNumber());
            c.setCaseType(updatedC.getCaseType());
            c.setFilingDate(updatedC.getFilingDate());
            c.setStatus(updatedC.getStatus());
            return caserepository.save(c);
        }
        return null;
    }

    public void deleteCase(Integer id) {
        caserepository.deleteById(id);
    }
}

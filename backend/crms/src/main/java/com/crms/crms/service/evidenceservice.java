package com.crms.crms.service;

import com.crms.crms.entity.evidence;
import com.crms.crms.repository.evidencerepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class evidenceservice {

    private final evidencerepository evidencerepository;

    public evidenceservice(evidencerepository evidencerepository) {
        this.evidencerepository = evidencerepository;
    }

    public List<evidence> getAllEvidences() {
        return evidencerepository.findAll();
    }

    public Optional<evidence> getEvidenceById(Integer id) {
        return evidencerepository.findById(id);
    }

    public List<evidence> getEvidencesByFirId(Integer firId) {
        return evidencerepository.findByFirId(firId);
    }

    public List<evidence> getEvidencesByCollectedBy(Integer collectedBy) {
        return evidencerepository.findByCollectedBy(collectedBy);
    }

    public evidence createEvidence(evidence ev) {
        return evidencerepository.save(ev);
    }

    public evidence updateEvidence(evidence updatedEv, Integer id) {
        Optional<evidence> existing = evidencerepository.findById(id);
        if (existing.isPresent()) {
            evidence ev = existing.get();
            ev.setFirId(updatedEv.getFirId());
            ev.setEvidenceType(updatedEv.getEvidenceType());
            ev.setDescription(updatedEv.getDescription());
            ev.setCollectedDate(updatedEv.getCollectedDate());
            ev.setStorageLocation(updatedEv.getStorageLocation());
            ev.setStatus(updatedEv.getStatus());
            ev.setCollectedBy(updatedEv.getCollectedBy());
            return evidencerepository.save(ev);
        }
        return null;
    }

    public void deleteEvidence(Integer id) {
        evidencerepository.deleteById(id);
    }
}

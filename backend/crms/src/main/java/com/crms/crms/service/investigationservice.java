package com.crms.crms.service;

import com.crms.crms.entity.investigation;
import com.crms.crms.repository.investigationrepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class investigationservice {

    private final investigationrepository investigationrepository;

    public investigationservice(investigationrepository investigationrepository) {
        this.investigationrepository = investigationrepository;
    }

    public List<investigation> getAllInvestigations() {
        return investigationrepository.findAll();
    }

    public Optional<investigation> getInvestigationById(Integer id) {
        return investigationrepository.findById(id);
    }

    public Optional<investigation> getInvestigationByFirId(Integer firId) {
        return investigationrepository.findByFirId(firId);
    }

    public List<investigation> getInvestigationsByPoliceId(Integer policeId) {
        return investigationrepository.findByPoliceId(policeId);
    }

    public investigation createInvestigation(investigation inv) {
        return investigationrepository.save(inv);
    }

    public investigation updateInvestigation(investigation updatedInv, Integer id) {
        Optional<investigation> existing = investigationrepository.findById(id);
        if (existing.isPresent()) {
            investigation inv = existing.get();
            inv.setFirId(updatedInv.getFirId());
            inv.setPoliceId(updatedInv.getPoliceId());
            inv.setStartDate(updatedInv.getStartDate());
            inv.setEndDate(updatedInv.getEndDate());
            inv.setStatus(updatedInv.getStatus());
            inv.setFindings(updatedInv.getFindings());
            inv.setChargesheetDate(updatedInv.getChargesheetDate());
            inv.setRemarks(updatedInv.getRemarks());
            return investigationrepository.save(inv);
        }
        return null;
    }

    public void deleteInvestigation(Integer id) {
        investigationrepository.deleteById(id);
    }
}

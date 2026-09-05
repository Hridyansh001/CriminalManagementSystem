package com.crms.crms.service;

import com.crms.crms.entity.firstatushist;
import com.crms.crms.repository.firstatushistrepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class firstatushistservice {

    private final firstatushistrepository firstatushistrepository;

    public firstatushistservice(firstatushistrepository firstatushistrepository) {
        this.firstatushistrepository = firstatushistrepository;
    }

    public List<firstatushist> getAllStatusHistories() {
        return firstatushistrepository.findAll();
    }

    public Optional<firstatushist> getStatusHistoryById(Integer id) {
        return firstatushistrepository.findById(id);
    }

    public List<firstatushist> getStatusHistoriesByFirId(Integer firId) {
        return firstatushistrepository.findByFirId(firId);
    }

    public firstatushist createStatusHistory(firstatushist history) {
        return firstatushistrepository.save(history);
    }

    public firstatushist updateStatusHistory(firstatushist updatedHistory, Integer id) {
        Optional<firstatushist> existing = firstatushistrepository.findById(id);
        if (existing.isPresent()) {
            firstatushist h = existing.get();
            h.setFirId(updatedHistory.getFirId());
            h.setStatus(updatedHistory.getStatus());
            h.setUpdatedDate(updatedHistory.getUpdatedDate());
            h.setUpdatedBy(updatedHistory.getUpdatedBy());
            h.setRemarks(updatedHistory.getRemarks());
            return firstatushistrepository.save(h);
        }
        return null;
    }

    public void deleteStatusHistory(Integer id) {
        firstatushistrepository.deleteById(id);
    }
}

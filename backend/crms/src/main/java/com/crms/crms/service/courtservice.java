package com.crms.crms.service;

import com.crms.crms.entity.court;
import com.crms.crms.repository.courtrepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class courtservice {

    private final courtrepository courtrepository;

    public courtservice(courtrepository courtrepository) {
        this.courtrepository = courtrepository;
    }

    public List<court> getAllCourts() {
        return courtrepository.findAll();
    }

    public Optional<court> getCourtById(Integer id) {
        return courtrepository.findById(id);
    }

    public court createCourt(court c) {
        return courtrepository.save(c);
    }

    public court updateCourt(court updatedC, Integer id) {
        Optional<court> existing = courtrepository.findById(id);
        if (existing.isPresent()) {
            court c = existing.get();
            c.setCourtName(updatedC.getCourtName());
            c.setCourtType(updatedC.getCourtType());
            c.setLocation(updatedC.getLocation());
            c.setJudgeName(updatedC.getJudgeName());
            return courtrepository.save(c);
        }
        return null;
    }

    public void deleteCourt(Integer id) {
        courtrepository.deleteById(id);
    }
}

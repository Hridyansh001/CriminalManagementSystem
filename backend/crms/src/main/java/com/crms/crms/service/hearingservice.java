package com.crms.crms.service;

import com.crms.crms.entity.hearing;
import com.crms.crms.repository.hearingrepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class hearingservice {

    private final hearingrepository hearingrepository;

    public hearingservice(hearingrepository hearingrepository) {
        this.hearingrepository = hearingrepository;
    }

    public List<hearing> getAllHearings() {
        return hearingrepository.findAll();
    }

    public Optional<hearing> getHearingById(Integer id) {
        return hearingrepository.findById(id);
    }

    public List<hearing> getHearingsByCaseId(Integer caseId) {
        return hearingrepository.findByCaseId(caseId);
    }

    public hearing createHearing(hearing h) {
        return hearingrepository.save(h);
    }

    public hearing updateHearing(hearing updatedH, Integer id) {
        Optional<hearing> existing = hearingrepository.findById(id);
        if (existing.isPresent()) {
            hearing h = existing.get();
            h.setCaseId(updatedH.getCaseId());
            h.setHearingDate(updatedH.getHearingDate());
            h.setHearingTime(updatedH.getHearingTime());
            h.setHearingType(updatedH.getHearingType());
            h.setStatus(updatedH.getStatus());
            h.setNextHearingDate(updatedH.getNextHearingDate());
            h.setRemarks(updatedH.getRemarks());
            return hearingrepository.save(h);
        }
        return null;
    }

    public void deleteHearing(Integer id) {
        hearingrepository.deleteById(id);
    }
}

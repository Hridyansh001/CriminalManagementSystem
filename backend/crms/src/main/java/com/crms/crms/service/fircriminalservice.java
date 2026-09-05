package com.crms.crms.service;

import com.crms.crms.entity.fircriminal;
import com.crms.crms.entity.fircriminalid;
import com.crms.crms.repository.fircriminalrepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class fircriminalservice {

    private final fircriminalrepository fircriminalrepository;

    public fircriminalservice(fircriminalrepository fircriminalrepository) {
        this.fircriminalrepository = fircriminalrepository;
    }

    public List<fircriminal> getAllFirCriminals() {
        return fircriminalrepository.findAll();
    }

    public Optional<fircriminal> getFirCriminalById(Integer firId, Integer criminalId) {
        return fircriminalrepository.findById(new fircriminalid(firId, criminalId));
    }

    public List<fircriminal> getByFirId(Integer firId) {
        return fircriminalrepository.findByFirId(firId);
    }

    public List<fircriminal> getByCriminalId(Integer criminalId) {
        return fircriminalrepository.findByCriminalId(criminalId);
    }

    public fircriminal createFirCriminal(fircriminal fc) {
        return fircriminalrepository.save(fc);
    }

    public fircriminal updateFirCriminal(fircriminal updatedFc, Integer firId, Integer criminalId) {
        fircriminalid id = new fircriminalid(firId, criminalId);
        Optional<fircriminal> existing = fircriminalrepository.findById(id);
        if (existing.isPresent()) {
            fircriminal fc = existing.get();
            fc.setRole(updatedFc.getRole());
            fc.setAccusedStatus(updatedFc.getAccusedStatus());
            return fircriminalrepository.save(fc);
        }
        return null;
    }

    public void deleteFirCriminal(Integer firId, Integer criminalId) {
        fircriminalrepository.deleteById(new fircriminalid(firId, criminalId));
    }
}

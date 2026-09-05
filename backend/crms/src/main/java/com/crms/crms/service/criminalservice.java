package com.crms.crms.service;

import com.crms.crms.entity.crimnal;
import com.crms.crms.repository.criminalrepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class criminalservice {

    private final criminalrepository criminalrepository;

    public criminalservice(criminalrepository criminalrepository) {
        this.criminalrepository = criminalrepository;
    }

    public List<crimnal> getAllCriminals() {
        return criminalrepository.findAll();
    }

    public Optional<crimnal> getCriminalById(Integer id) {
        return criminalrepository.findById(id);
    }

    public Optional<crimnal> getCriminalByNationalId(String nationalId) {
        return criminalrepository.findByNationalId(nationalId);
    }

    public crimnal createCriminal(crimnal c) {
        return criminalrepository.save(c);
    }

    public crimnal updateCriminal(crimnal updatedC, Integer id) {
        Optional<crimnal> existing = criminalrepository.findById(id);
        if (existing.isPresent()) {
            crimnal c = existing.get();
            c.setName(updatedC.getName());
            c.setNationalId(updatedC.getNationalId());
            c.setStatus(updatedC.getStatus());
            c.setLevelOfCrime(updatedC.getLevelOfCrime());
            c.setAliases(updatedC.getAliases());
            c.setLivingStatus(updatedC.getLivingStatus());
            return criminalrepository.save(c);
        }
        return null;
    }

    public void deleteCriminal(Integer id) {
        criminalrepository.deleteById(id);
    }
}

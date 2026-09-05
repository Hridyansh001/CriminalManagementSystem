package com.crms.crms.service;

import com.crms.crms.entity.police;
import com.crms.crms.repository.policerepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class policeservice {

    private final policerepository policerepository;

    public policeservice(policerepository policerepository) {
        this.policerepository = policerepository;
    }

    public List<police> getAllPolice() {
        return policerepository.findAll();
    }

    public Optional<police> getPoliceById(Integer id) {
        return policerepository.findById(id);
    }

    public Optional<police> getPoliceByBadgeNumber(String badgeNumber) {
        return policerepository.findByBadgeNumber(badgeNumber);
    }

    public police createPolice(police p) {
        return policerepository.save(p);
    }

    public police updatePolice(police updatedP, Integer id) {
        Optional<police> existingPolice = policerepository.findById(id);
        if (existingPolice.isPresent()) {
            police p = existingPolice.get();
            p.setName(updatedP.getName());
            p.setBadgeNumber(updatedP.getBadgeNumber());
            p.setPoliceRank(updatedP.getPoliceRank());
            p.setEmail(updatedP.getEmail());
            p.setPhone(updatedP.getPhone());
            p.setStationId(updatedP.getStationId());
            p.setPassword(updatedP.getPassword());
            return policerepository.save(p);
        }
        return null;
    }

    public void deletePolice(Integer id) {
        policerepository.deleteById(id);
    }
}

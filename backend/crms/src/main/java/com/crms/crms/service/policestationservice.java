package com.crms.crms.service;

import com.crms.crms.entity.policestation;
import com.crms.crms.repository.policestationrepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class policestationservice {

    private final policestationrepository policestationrepository;

    public policestationservice(policestationrepository policestationrepository) {
        this.policestationrepository = policestationrepository;
    }

    public List<policestation> getAllPoliceStations() {
        return policestationrepository.findAll();
    }

    public Optional<policestation> getPoliceStationById(Integer id) {
        return policestationrepository.findById(id);
    }

    public policestation createPoliceStation(policestation ps) {
        return policestationrepository.save(ps);
    }

    public policestation updatePoliceStation(policestation updatedPs, Integer id) {
        Optional<policestation> existingPs = policestationrepository.findById(id);
        if (existingPs.isPresent()) {
            policestation ps = existingPs.get();
            ps.setStationName(updatedPs.getStationName());
            ps.setAddress(updatedPs.getAddress());
            ps.setCity(updatedPs.getCity());
            ps.setJurisdiction(updatedPs.getJurisdiction());
            ps.setPhone(updatedPs.getPhone());
            return policestationrepository.save(ps);
        }
        return null;
    }

    public void deletePoliceStation(Integer id) {
        policestationrepository.deleteById(id);
    }
}

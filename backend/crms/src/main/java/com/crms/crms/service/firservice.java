package com.crms.crms.service;


import com.crms.crms.entity.fir;
import com.crms.crms.repository.firrepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class firservice {

    private final firrepository firrepository;
    public firservice(firrepository firrepository)
    {
        this.firrepository= firrepository;
    }

    // getting repos
    public List<fir> getAllfirs()
    {
        return firrepository.findAll();
    }

    public Optional<fir> getfirbyid(Integer id)  //getting fir by id it is optional tho
    {
        return firrepository.findById(id);
    }

    public fir createfir(fir fir)   // creation and saving new firs
    {
        return firrepository.save(fir);
    }

    public fir updatefir(fir updfir,Integer id) // updating fir
    {
        Optional<fir> existingfir = firrepository.findById(id);
        if(existingfir.isPresent()){
            fir fir = existingfir.get();
            fir.setUserid(updfir.getUserid());
            fir.setCrimetype(updfir.getCrimetype());
            fir.setFirnumber(updfir.getFirnumber());
            fir.setDescription(updfir.getDescription());
            fir.setJurisdiction(updfir.getJurisdiction());
            fir.setDate_filed(updfir.getDate_filed());
            fir.setStatus(updfir.getStatus());
            fir.setLastupdated(updfir.getLastupdated());
            fir.setLocation(updfir.getLocation());
            return  firrepository.save(fir);
        }
        return null;
    }
    public void delfir(Integer id) // deleting fir
    {
        firrepository.deleteById(id);
    }


}

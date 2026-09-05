package com.crms.crms.controller;

import com.crms.crms.entity.*;
import com.crms.crms.service.firservice;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/firs")
@CrossOrigin(origins = "*")
public class fircontroller {
    private final firservice firservice;

    public fircontroller(firservice firservice)
    {
        this.firservice=firservice;
    }
    @GetMapping   // getting all firs from firservice
    public List<fir> getallfirs()
    {
        return firservice.getAllfirs();
    }
    @GetMapping("/{id}") // getting all firs from firservice using fir ids
    public ResponseEntity<fir> getfirbyid(@PathVariable Integer id)
    {
        return firservice.getfirbyid(id).map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping  //creating fir
    public  ResponseEntity<fir> createfir(@RequestBody fir fir){
        fir savedfir = firservice.createfir(fir);
        return ResponseEntity.ok(savedfir);
    }

    @PostMapping("/{id}")
    public ResponseEntity<fir> updatefir(@PathVariable Integer id, @RequestBody fir fir)
    {
        fir updfir = firservice.updatefir(fir,id);
        if(updfir==null)
        {
            return ResponseEntity.notFound().build();
        }
        return  ResponseEntity.ok(updfir);
    }

    @DeleteMapping("/{id}")   // deleting fir by id
    public ResponseEntity<Void> deletefir(@PathVariable Integer id)
    {
        firservice.delfir(id);
        return ResponseEntity.noContent().build();
    }
}

package com.crms.crms.repository;

import com.crms.crms.entity.fircriminal;
import com.crms.crms.entity.fircriminalid;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface fircriminalrepository extends JpaRepository<fircriminal, fircriminalid> {
    List<fircriminal> findByFirId(Integer firId);
    List<fircriminal> findByCriminalId(Integer criminalId);
}

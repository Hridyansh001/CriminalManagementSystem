package com.crms.crms.repository;

import com.crms.crms.entity.firstatushist;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface firstatushistrepository extends JpaRepository<firstatushist, Integer> {
    List<firstatushist> findByFirId(Integer firId);
}

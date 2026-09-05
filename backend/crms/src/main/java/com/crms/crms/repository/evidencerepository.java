package com.crms.crms.repository;

import com.crms.crms.entity.evidence;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface evidencerepository extends JpaRepository<evidence, Integer> {
    List<evidence> findByFirId(Integer firId);
    List<evidence> findByCollectedBy(Integer collectedBy);
}

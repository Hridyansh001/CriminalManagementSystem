package com.crms.crms.repository;

import com.crms.crms.entity.courtcase;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface caserepository extends JpaRepository<courtcase, Integer> {
    Optional<courtcase> findByCaseNumber(String caseNumber);
    Optional<courtcase> findByFirId(Integer firId);
    List<courtcase> findByCourtId(Integer courtId);
}

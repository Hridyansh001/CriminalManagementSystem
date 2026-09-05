package com.crms.crms.repository;

import com.crms.crms.entity.judgement;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface judgementrepository extends JpaRepository<judgement, Integer> {
    Optional<judgement> findByCaseId(Integer caseId);
}

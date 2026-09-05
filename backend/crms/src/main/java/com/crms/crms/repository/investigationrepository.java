package com.crms.crms.repository;

import com.crms.crms.entity.investigation;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface investigationrepository extends JpaRepository<investigation, Integer> {
    Optional<investigation> findByFirId(Integer firId);
    List<investigation> findByPoliceId(Integer policeId);
}

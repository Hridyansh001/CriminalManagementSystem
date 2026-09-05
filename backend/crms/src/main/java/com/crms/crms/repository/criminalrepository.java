package com.crms.crms.repository;

import com.crms.crms.entity.crimnal;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface criminalrepository extends JpaRepository<crimnal, Integer> {
    Optional<crimnal> findByNationalId(String nationalId);
}

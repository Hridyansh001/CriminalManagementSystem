package com.crms.crms.repository;

import com.crms.crms.entity.police;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface policerepository extends JpaRepository<police, Integer> {
    Optional<police> findByBadgeNumber(String badgeNumber);
    Optional<police> findByEmail(String email);
}

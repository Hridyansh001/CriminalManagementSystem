package com.crms.crms.repository;

import com.crms.crms.entity.court;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface courtrepository extends JpaRepository<court, Integer> {
}

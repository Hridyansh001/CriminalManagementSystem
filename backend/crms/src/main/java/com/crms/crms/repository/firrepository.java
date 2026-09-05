package com.crms.crms.repository;

import com.crms.crms.entity.fir;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface firrepository extends JpaRepository<fir, Integer> {
}

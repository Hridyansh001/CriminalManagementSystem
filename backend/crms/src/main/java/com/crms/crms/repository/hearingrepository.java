package com.crms.crms.repository;

import com.crms.crms.entity.hearing;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface hearingrepository extends JpaRepository<hearing, Integer> {
    List<hearing> findByCaseId(Integer caseId);
}

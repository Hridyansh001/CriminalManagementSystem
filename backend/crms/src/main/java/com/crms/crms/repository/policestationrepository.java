package com.crms.crms.repository;

import com.crms.crms.entity.policestation;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface policestationrepository extends JpaRepository<policestation, Integer> {
}

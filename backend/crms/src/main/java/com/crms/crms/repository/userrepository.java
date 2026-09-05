package com.crms.crms.repository;

import com.crms.crms.entity.user;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface userrepository extends JpaRepository<user, Integer> {
    Optional<user> findByEmail(String email);
}

package com.crms.crms.service;

import com.crms.crms.entity.user;
import com.crms.crms.repository.userrepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class userservice {

    private final userrepository userrepository;

    public userservice(userrepository userrepository) {
        this.userrepository = userrepository;
    }

    public List<user> getAllUsers() {
        return userrepository.findAll();
    }

    public Optional<user> getUserById(Integer id) {
        return userrepository.findById(id);
    }

    public Optional<user> getUserByEmail(String email) {
        return userrepository.findByEmail(email);
    }

    public user createUser(user user) {
        return userrepository.save(user);
    }

    public user updateUser(user updatedUser, Integer id) {
        Optional<user> existingUser = userrepository.findById(id);
        if (existingUser.isPresent()) {
            user u = existingUser.get();
            u.setName(updatedUser.getName());
            u.setEmail(updatedUser.getEmail());
            u.setPhone(updatedUser.getPhone());
            u.setDob(updatedUser.getDob());
            u.setGender(updatedUser.getGender());
            u.setResidentialAddress(updatedUser.getResidentialAddress());
            u.setPassword(updatedUser.getPassword());
            return userrepository.save(u);
        }
        return null;
    }

    public void deleteUser(Integer id) {
        userrepository.deleteById(id);
    }
}
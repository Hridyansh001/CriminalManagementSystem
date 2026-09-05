package com.crms.crms.controller;

import com.crms.crms.entity.user;
import com.crms.crms.service.userservice;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/users")
@CrossOrigin(origins = "*")
public class usercontroller {

    private final userservice userservice;

    public usercontroller(userservice userservice) {
        this.userservice = userservice;
    }

    @GetMapping
    public List<user> getAllUsers() {
        return userservice.getAllUsers();
    }

    @GetMapping("/{id}")
    public ResponseEntity<user> getUserById(@PathVariable Integer id) {
        return userservice.getUserById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<user> createUser(@RequestBody user user) {
        user savedUser = userservice.createUser(user);
        return ResponseEntity.ok(savedUser);
    }

    @PostMapping("/{id}")
    public ResponseEntity<user> updateUser(@PathVariable Integer id, @RequestBody user user) {
        user updated = userservice.updateUser(user, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @PutMapping("/{id}")
    public ResponseEntity<user> updateUserPut(@PathVariable Integer id, @RequestBody user user) {
        user updated = userservice.updateUser(user, id);
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable Integer id) {
        userservice.deleteUser(id);
        return ResponseEntity.noContent().build();
    }
}

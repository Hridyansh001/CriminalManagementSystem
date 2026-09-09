package com.crms.crms.entity;

import jakarta.persistence.*;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Past;
import jakarta.validation.constraints.Pattern;
import lombok.Getter;
import lombok.Setter;
import java.time.LocalDate;

@Entity
@Table(name = "User")
@Getter
@Setter
public class user {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "User_ID")
    private Integer userId;

    @NotBlank(message = "this field cant be blank")
    @Pattern(
            regexp = "^[a-zA-Z ]+$"
    )
    @Column(name = "Name", nullable = false)
    private String name;

    @Pattern(
            regexp = "^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$",
            message = "should contain a proper email"
    )
    @Column(name = "Email", nullable = false, unique = true)
    private String email;

    @Pattern(regexp = "^[0-9]{10}$")
    @Column(name = "Phone")
    private String phone;

    @Past(message = "date should be in the past")
    @Column(name = "DOB")
    private LocalDate dob;

    @Column(name = "Gender")
    private String gender;

    @Column(name = "Residential_Address")
    private String residentialAddress;

    @Column(name = "Password", nullable = false)
    private String password;
}
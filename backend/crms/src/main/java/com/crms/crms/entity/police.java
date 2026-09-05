package com.crms.crms.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "police")
@Getter
@Setter
public class police {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "Police_ID")
    private Integer policeId;

    @Column(name = "Name", nullable = false)
    private String name;

    @Column(name = "Badge_Number", nullable = false, unique = true)
    private String badgeNumber;

    @Column(name = "police_rank")
    private String policeRank;

    @Column(name = "Email", unique = true)
    private String email;

    @Column(name = "Phone")
    private String phone;

    @Column(name = "Station_ID", nullable = false)
    private Integer stationId;

    @Column(name = "Password", nullable = false)
    private String password;
}

package com.crms.crms.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "PoliceStation")
@Getter
@Setter
public class policestation {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "Station_ID")
    private Integer stationId;

    @Column(name = "Station_Name", nullable = false)
    private String stationName;

    @Column(name = "Address")
    private String address;

    @Column(name = "City")
    private String city;

    @Column(name = "Jurisdiction")
    private String jurisdiction;

    @Column(name = "Phone")
    private String phone;
}

package com.crms.crms.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "Court")
@Getter
@Setter
public class court {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "Court_ID")
    private Integer courtId;

    @Column(name = "Court_Name", nullable = false)
    private String courtName;

    @Column(name = "Court_Type")
    private String courtType;

    @Column(name = "Location")
    private String location;

    @Column(name = "Judge_Name")
    private String judgeName;
}

package com.crms.crms.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "Criminal")
@Getter
@Setter
public class crimnal {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "Criminal_ID")
    private Integer criminalId;

    @Column(name = "Name", nullable = false)
    private String name;

    @Column(name = "National_ID", unique = true)
    private String nationalId;

    @Column(name = "Status")
    private String status;

    @Column(name = "Level_of_Crime")
    private String levelOfCrime;

    @Column(name = "Aliases")
    private String aliases;

    @Column(name = "Living_Status")
    private String livingStatus;
}

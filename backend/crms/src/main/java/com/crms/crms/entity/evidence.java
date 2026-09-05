package com.crms.crms.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDate;

@Entity
@Table(name = "Evidence")
@Getter
@Setter
public class evidence {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "Evidence_ID")
    private Integer evidenceId;

    @Column(name = "FIR_ID", nullable = false)
    private Integer firId;

    @Column(name = "Evidence_Type")
    private String evidenceType;

    @Column(name = "Description")
    private String description;

    @Column(name = "Collected_Date")
    private LocalDate collectedDate;

    @Column(name = "Storage_Location")
    private String storageLocation;

    @Column(name = "Status")
    private String status;

    @Column(name = "Collected_By", nullable = false)
    private Integer collectedBy;
}

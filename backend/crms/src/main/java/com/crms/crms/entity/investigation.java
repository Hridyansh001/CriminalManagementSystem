package com.crms.crms.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDate;

@Entity
@Table(name = "Investigation")
@Getter
@Setter
public class investigation {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "Investigation_ID")
    private Integer investigationId;

    @Column(name = "FIR_ID", nullable = false, unique = true)
    private Integer firId;

    @Column(name = "Police_ID", nullable = false)
    private Integer policeId;

    @Column(name = "Start_Date")
    private LocalDate startDate;

    @Column(name = "End_Date")
    private LocalDate endDate;

    @Column(name = "Status")
    private String status;

    @Column(name = "Findings")
    private String findings;

    @Column(name = "Chargesheet_Date")
    private LocalDate chargesheetDate;

    @Column(name = "Remarks")
    private String remarks;
}

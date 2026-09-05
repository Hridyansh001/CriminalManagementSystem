package com.crms.crms.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDate;

@Entity
@Table(name = "`Case`")
@Getter
@Setter
public class courtcase {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "Case_ID")
    private Integer caseId;

    @Column(name = "FIR_ID", nullable = false, unique = true)
    private Integer firId;

    @Column(name = "Court_ID", nullable = false)
    private Integer courtId;

    @Column(name = "Case_Number", nullable = false, unique = true)
    private String caseNumber;

    @Column(name = "Case_Type")
    private String caseType;

    @Column(name = "Filing_Date")
    private LocalDate filingDate;

    @Column(name = "Status")
    private String status;
}

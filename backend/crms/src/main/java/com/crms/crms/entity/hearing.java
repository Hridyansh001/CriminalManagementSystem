package com.crms.crms.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDate;
import java.time.LocalTime;

@Entity
@Table(name = "Hearing")
@Getter
@Setter
public class hearing {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "Hearing_ID")
    private Integer hearingId;

    @Column(name = "Case_ID", nullable = false)
    private Integer caseId;

    @Column(name = "Hearing_Date", nullable = false)
    private LocalDate hearingDate;

    @Column(name = "Hearing_Time")
    private LocalTime hearingTime;

    @Column(name = "Hearing_Type")
    private String hearingType;

    @Column(name = "Status")
    private String status;

    @Column(name = "Next_Hearing_Date")
    private LocalDate nextHearingDate;

    @Column(name = "Remarks")
    private String remarks;
}

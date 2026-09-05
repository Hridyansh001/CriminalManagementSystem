package com.crms.crms.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDate;

@Entity
@Table(name = "FIR_Status_History")
@Getter
@Setter
public class firstatushist {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "History_ID")
    private Integer historyId;

    @Column(name = "FIR_ID", nullable = false)
    private Integer firId;

    @Column(name = "Status", nullable = false)
    private String status;

    @Column(name = "Updated_Date", nullable = false)
    private LocalDate updatedDate;

    @Column(name = "Updated_By")
    private String updatedBy;

    @Column(name = "Remarks")
    private String remarks;
}

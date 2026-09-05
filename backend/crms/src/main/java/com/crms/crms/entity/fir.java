package com.crms.crms.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import java.time.LocalDate;

@Entity
@Table(name = "FIR")
@Getter
@Setter
public class fir {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "FIR_ID")
    private Integer fir_id;

    @Column(name = "FIR_Number", nullable = false, unique = true)
    private String firnumber;

    @Column(name = "User_ID", nullable = false)
    private Integer userid;

    @Column(name = "Date_Filed", nullable = false)
    private LocalDate date_filed;

    @Column(name = "Crime_Type", nullable = false)
    private String crimetype;

    @Column(name = "Description")
    private String description;

    @Column(name = "Location")
    private String location;

    @Column(name = "Jurisdiction")
    private String jurisdiction;

    @Column(name = "Status", nullable = false)
    private String status;

    @Column(name = "Last_Updated")
    private LocalDate lastupdated;
}

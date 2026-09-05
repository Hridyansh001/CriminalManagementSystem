package com.crms.crms.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDate;

@Entity
@Table(name = "Judgment")
@Getter
@Setter
public class judgement {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "Judgment_ID")
    private Integer judgmentId;

    @Column(name = "Case_ID", nullable = false, unique = true)
    private Integer caseId;

    @Column(name = "Judgment_Date")
    private LocalDate judgmentDate;

    @Column(name = "Decision")
    private String decision;

    @Column(name = "Basis")
    private String basis;

    @Column(name = "Sentence")
    private String sentence;

    @Column(name = "Remarks")
    private String remarks;
}

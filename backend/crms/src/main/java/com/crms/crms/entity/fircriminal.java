package com.crms.crms.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "FIR_Criminal")
@IdClass(fircriminalid.class)
@Getter
@Setter
public class fircriminal {

    @Id
    @Column(name = "FIR_ID")
    private Integer firId;

    @Id
    @Column(name = "Criminal_ID")
    private Integer criminalId;

    @Column(name = "Role")
    private String role;

    @Column(name = "Accused_Status")
    private String accusedStatus;
}

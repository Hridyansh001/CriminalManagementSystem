package com.crms.crms.dto;

import lombok.Getter;

@Getter
public class dashboardresponse {

    private final long totalFirs;
    private final long totalUsers;
    private final long totalCriminals;
    private final long totalPolice;
    private final long totalInvestigations;
    private final long totalCases;

    public dashboardresponse(
            long totalFirs,
            long totalUsers,
            long totalCriminals,
            long totalPolice,
            long totalInvestigations,
            long totalCases) {

        this.totalFirs = totalFirs;
        this.totalUsers = totalUsers;
        this.totalCriminals = totalCriminals;
        this.totalPolice = totalPolice;
        this.totalInvestigations = totalInvestigations;
        this.totalCases = totalCases;
    }
}
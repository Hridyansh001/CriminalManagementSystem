package com.crms.crms.service;

import com.crms.crms.dto.dashboardresponse;
import com.crms.crms.repository.*;
import org.springframework.stereotype.Service;

@Service
public class dashboardservice {

    private final firrepository firrepository;
    private final userrepository userrepository;
    private final criminalrepository criminalrepository;
    private final policerepository policerepository;
    private final investigationrepository investigationrepository;
    private final caserepository caserepository;

    public dashboardservice(
            firrepository firrepository,
            userrepository userrepository,
            criminalrepository criminalrepository,
            policerepository policerepository,
            investigationrepository investigationrepository,
            caserepository caserepository) {

        this.firrepository = firrepository;
        this.userrepository = userrepository;
        this.criminalrepository = criminalrepository;
        this.policerepository = policerepository;
        this.investigationrepository = investigationrepository;
        this.caserepository = caserepository;
    }

    public dashboardresponse getDashboardData() {

        long totalFirs = firrepository.count();
        long totalUsers = userrepository.count();
        long totalCriminals = criminalrepository.count();
        long totalPolice = policerepository.count();
        long totalInvestigations = investigationrepository.count();
        long totalCases = caserepository.count();

        return new dashboardresponse(
                totalFirs,
                totalUsers,
                totalCriminals,
                totalPolice,
                totalInvestigations,
                totalCases
        );
    }
}
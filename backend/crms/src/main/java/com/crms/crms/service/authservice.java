package com.crms.crms.service;

import com.crms.crms.dto.loginresponse;
import com.crms.crms.entity.police;
import com.crms.crms.entity.user;
import com.crms.crms.repository.policerepository;
import com.crms.crms.repository.userrepository;
import org.springframework.stereotype.Service;

@Service
public class authservice {
    private final userrepository userrepository;
    private final policerepository policerepository;

    public authservice(userrepository userrepository, policerepository policerepository)
    {
        this.userrepository=userrepository;
        this.policerepository=policerepository;
    }
    public loginresponse login (String identifier , String password) {
        var userresult = userrepository.findByEmail(identifier);
        if (userresult.isPresent()) {
            user user = userresult.get();
            if (user.getPassword().equals(password)) {
                return new loginresponse(true, "user", "login successful", user.getUserId(), user.getName());
            }

            return new loginresponse(false, null, "login failed", null, null);

        }
        var policbadge = policerepository.findByBadgeNumber(identifier);
        if(policbadge.isPresent())
        {
            police police = policbadge.get();
            if(police.getPassword().equals(password))
            {
                return new loginresponse(true,"police","login successful",police.getPoliceId(),police.getName());

            }return new loginresponse(false,null,"login failed",null,null);
        }
        var policeemail = policerepository.findByEmail(identifier);
        if(policeemail.isPresent())
        {
            police police= policeemail.get();
            if(police.getPassword().equals(password))
            {
                return new loginresponse(true,"police","login successful", police.getPoliceId(),police.getName());

            }return new loginresponse(false,null,"login failed",null,null);
        }
        return  new loginresponse(false,null,"user or police not found",null,null);
    }

}

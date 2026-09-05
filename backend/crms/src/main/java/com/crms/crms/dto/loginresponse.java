package com.crms.crms.dto;


import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class loginresponse {
    private boolean success;
    private String role;
    private String msg;
    private  Integer id;
    private String name;

    public loginresponse(boolean success, String role, String msg, Integer id, String name)
    {
        this.success=success;
        this.role=role;
        this.msg=msg;
        this.id=id;
        this.name=name;
    }
}

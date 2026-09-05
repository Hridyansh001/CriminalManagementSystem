package com.crms.crms.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.io.Serializable;
import java.util.Objects;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class fircriminalid implements Serializable {
    private Integer firId;
    private Integer criminalId;

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        fircriminalid that = (fircriminalid) o;
        return Objects.equals(firId, that.firId) && Objects.equals(criminalId, that.criminalId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(firId, criminalId);
    }
}

# CBB_csrbox
This repository consists of  python scripts to generate RISC-V Assembly for Testing the BSV output of the CSRBOX, in the Chromite Core by [InCore Semiconductors](https://incoresemi.com/).

The 'CSRBOX' (https://csrbox.readthedocs.io/en/latest/) is an external python tool which can generate a bsv CSR module based on the specification provided. According to the RISC-V spec, the CSRs are divided into 3 major categories based on the privilege modes supported: Machine, Supervisor and User.

## File Structure
```
.
├── README.md -- Describes the idea behind each test and how the ASM is generated efficiently using Python 3.
├── uatg_csrbox_ext_bitmask.py -- Generates ASM to check the extension field of misa csr by  by using csrrw instruction(sample instructions).
├── uatg_csrbox_mstatus_mpp.py -- Generates ASM to check the mpp field under mstatus csr by using csrrw instrution(sample instructions) .
├── uatg_csrbox_mxl_legal.py -- Generates ASM to check the mxl field of misa csr by using csrrw instruction(sample instructions).
├── uatg_csrbox_ro_check.py -- Generates ASM to check the csrrw instruction in registers mvendorid,mhartid,mimpid,marchid.
├── 

```

## Code Description

####uatg_csrbox_ext_bitmask.py

- here the `extensions` field of misa csr is considered.
- `Extensions` field has a legal bitmask value of `0x0141105` as specified in isa yaml which is stored in register x3.
-  x4 register is stored with negated value of x3 register.
-  then an `and` operation is done on registers x3 and misa and stored in x5.
-  then an `and` operation is done on registers x0 and x4 and stored in x6.
-  then followed by an `or` operation on registers x5 and x6.
- trap is araised when x3 and misa valuses are not equal.
- when trap occurs x31 is incremented which we can find where trap has occurred an test has failed.

####uatg_csrbox_mstatus_mpp.py 

- here the `mpp` field under mstatus csr is considerd.
- `mpp` has 3 legal values 0x0,0x1,0x3.
- if we try to write 0x1, then mstatus register should be updated
- if we try to write 0x2, then it should remain unchanged.
- if mstatus and x2 are not equal a `trap` is araised.
- when `trap` occurs x31 is incremented which we can find where trap has occurred an test has failed.

####uatg_csrbox_mxl_legal.py

- here we consider the `mxl` field of misa csr which is `warl`.
- x3 is loaded with legal value 0x2.
- if we try to write illegal values it should return a legal value.
- if misa and x3 are not equal a trap is araised.
-  when `trap` occurs x31 is incremented which we can find where trap has occurred an test has failed.
 
 ####uatg_csrbox_ro_check.py
 
 -

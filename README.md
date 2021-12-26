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
-here the 'mxl' field of misa csr is considered

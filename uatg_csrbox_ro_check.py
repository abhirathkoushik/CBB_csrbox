from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, mext_instructions
from uatg.utils import rvtest_data
from typing import Dict, Any
from random import randint
import random


"""
Read-Only CSR's like 'mimpid' or 'mvendorid' have to hold the same value as specified 
in the isa yaml and cannot be changed.

Here, we try to load values into these CSR's and check if they have actually been updated.
If updated, then a trap is triggered (register x31 in this case)
"""

class uatg_csrbox_ro_check(IPlugin):
    def __init__(self)-> None:
        super().__init__()

    def execute(self, core_yaml, isa_yaml) -> bool:
        return
        
    def generate_asm(self) -> Dict[str, str]:
        
        csr=['mvendorid','mhartid','mimpid','marchid'] 
        asm= '\t li x4,0xffffffff\n'

        for j in range(0, len(csr)):
            asm += f'\t lin x3,0x3020\n\t csrrw x4,{csr[j]},x3\n\t beq x4,{csr[j]},trap\n'
            for i in range(0,200):
                x=random.randrange(0,2**32)
                asm += f'\t li x3,{hex(x)}\n\t csrrw x4,{csr[j]},x3\n\t beq x4,{csr[j]},trap\n'
        
        asm +='trap:\n\taddi x31,x31,1\n'
	    
        compile_macros = []
        return [{
            'asm_code': asm,
            'asm_sig': '',
            'compile_macros': compile_macros
        }]

    def check_log(self, log_file_path, reports_dir) -> bool:
        return False

    def generate_covergroups(self, config_file) -> str:
        sv = ""
        return sv

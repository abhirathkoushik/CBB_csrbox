from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, mext_instructions
from uatg.utils import rvtest_data
from typing import Dict, Any

"""
Mpp is a field under Mstatus CSR
Mpp has only 3 legal values namely 0x0,0x1,0x3

So if we try to write 0x2, then it should remain unchanged
and give back either of the 3 legal values

Here, we write 0x1 first and then 0x2
and then check if the mpp field was updated or not.
Ideally, it should remain 0x1.

"""


class uatg_csrbox_mstatus_mpp(IPlugin):
    def _init_(self)->None:
        super()._init_()

    def execute(self, core_yaml, isa_yaml) -> bool:
        self.hart0 = isa_yaml['hart0']
        self.mstatus = self.hart0['mstatus']
        self.rv64 = self.mstatus['rv64']
        self.mpp = self.rv64['mpp']
        self.type1 = self.mpp['type']
        self.warl = self.type1['warl']
        self.legal = self.warl['legal']
        return 
        
    def generate_asm(self) -> Dict[str, str]:

        asm = f"\t li x1, {self.legal} \n"
        asm += "\t csrrw x0,mstatus,x1 \n"

        asm += "\t li x2,0x01 \n"
        asm += "\t li x3,0x02 \n"

        asm += "\t csrrw x0,mstatus,x2 \n"
        asm += "\t csrrw x0,mstatus,x3 \n"
        asm += "\t bne mstatus,x2,trap \n"

        asm += "\t trap: addi x31,x31,1\n"

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

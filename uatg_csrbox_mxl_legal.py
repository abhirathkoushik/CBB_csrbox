from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, mext_instructions
from uatg.utils import rvtest_data
from typing import Dict, Any

"""
Misa CSR has 2 fields, mxl and extensions

Mxl is a WARL (Write Any Read Legal) field and is the upper 2 bits of misa
It is a 2-bit field with legal value 2(0x2) only.

Here, even if we try to write values (0,1,3) into mxl,
it should still display only 2 when it is read.

"""


class uatg_csrbox_mxl_legal(IPlugin):
    def _init_(self)->None:
        super()._init_()

    def execute(self, core_yaml, isa_yaml) -> bool:
        self.hart0 = isa_yaml['hart0']
        self.misa = hart0['misa']
        self.rv64 = misa['rv64']
        self.mxl = rv64['mxl']
        self.type1 = mxl['type']
        self.warl = type1['warl']
        self.legal= warl['legal']
        return 
        
    def generate_asm(self) -> Dict[str, str]:

        asm = f"\t li x1, {self.legal} \n"
        asm += "\t csrrw x0,misa,x1 \n"
        asm += "\t li x3,0x2 \n"

        for i in [0,1,3]:
            asm += f"\t csrrw x0,misa,{hex(i)} \n"
            asm += "\t bne misa,x3,trap \n"

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
    

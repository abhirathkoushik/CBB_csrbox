from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, mext_instructions
from uatg.utils import rvtest_data
from typing import Dict, Any

"""
Misa CSR has 2 fields, mxl and extensions

Extensions field has a legal bitmask value of 0x0141105 as specified in isa yaml.
Irrespective of the input value tried to be written, the same bitmask value of
0x0141105 has to be displayed when read.

This is done through the following expression,
(input_value & bitmask) | (default-val & ~bitmask)

"""


class uatg_csrbox_ext_bitmask(IPlugin):
    def _init_(self)->None:
        super()._init_()

    def execute(self, core_yaml, isa_yaml) -> bool:
        self.hart0 = isa_yaml['hart0']
        self.misa = self.hart0['misa']
        self.rv64 = self.misa['rv64']
        self.ext = self.rv64['extensions']
        self.type1 = self.ext['type']
        self.warl = self.type1['warl']
        self.legal= self.warl['legal']
        return 
        
    def generate_asm(self) -> Dict[str, str]:

        asm = f"\t li x1, {self.legal} \n"
        asm += "\t csrrw x0,misa,x1 \n"
        
        asm += "\t li x3,0x0141105 \n"
        asm += "\t not x4,x3 \n"

        asm += "\t and x5,misa,x3 \n"
        asm += "\t and x6,x0,x4 \n" 
        asm += "\t or misa,x5,x6 \n"
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

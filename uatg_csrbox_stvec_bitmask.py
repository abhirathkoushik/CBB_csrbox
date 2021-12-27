from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, mext_instructions
from uatg.utils import rvtest_data
from typing import Dict, Any

class uatg_csrbox_ext_bitmask(IPlugin):
    def init(self)->None:
        super().init()

    def execute(self, core_yaml, isa_yaml) -> bool:
        self.hart0 = isa_yaml['hart0']
        self.stvec = self.hart0['stvec']
        self.rv64 = self.stvec['rv64']
        self.base = self.rv64['base']
        self.type1 = self.base['type'] 
        self.warl = self.type1['warl']
        self.legal= self.warl['legal']
        self.bitmask=self.legal['bitmask']           
        self.rv = self.stvec['reset-val']
        self.default_value=self.rv['default_value']  
        return 
        
    def generate_asm(self) -> Dict[str, str]:
        
        asm='\t li x4,0xffffffffffffffff \n'   
        asm+= f'\t and x5,x4,{self.bitmask} \n'
        asm+= f'\t not {self.bitmask},{self.bitmask} \n'
        asm+= f'\t and x6,{default_value},{self.bitmask} \n'
        asm+= '\t or x7,x5,x6 \n'                  
        asm+= f'\t beq x7,{self.bitmask},loop \n'
        asm+= '\t loop:csrrw x5,stvec[61:0],x4 \n'
        asm+= f'\t bne x7,{self.bitmask},trap \n'
        asm += '\t trap: addi x31,x31,1\n'
        
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

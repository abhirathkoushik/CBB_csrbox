from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, mext_instructions
from uatg.utils import rvtest_data
from typing import Dict, Any

class uatg_csrbox_stvec(IPlugin):
    def init(self)->None:
        super().init()

def execute(self, core_yaml, isa_yaml) -> bool:

     self.hart0 = isa_yaml['hart0']
     self.stvec = self.hart0['stvec']
     self.rv64 = self.stvec['rv64']
     self.mode = self.rv64['mode']
     self.type1 = self.mode['type'] 
     self.warl = self.type1['warl']
     self.legal= self.warl['legal']
     return
     
def generate_asm(self) -> Dict[str, str]:

    asm = f'\t li x1, {self.legal} \n'
    asm+= '\t csrrw x0,stvec,x1 \n'
     
    asm+= '\t li x3,0x1 \n'
    asm+= '\t csrrw x0,stvec,x3 \n'
    for i in [2,3]:
       asm+= f'\t li x4,{hex(i)} \n'
       asm+= '\t csrrw x0,stvec,x4 \n'
       asm+= '\t bne stvec,x3,trap \n'
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
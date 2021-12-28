from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, mext_instructions
from uatg.utils import rvtest_data
from typing import Dict, Any

class uatg_csrbox_stvec_rstvalue(IPlugin):
    def init(self)->None:
        super().init()
        
    def execute(self, core_yaml, isa_yaml) -> bool:
    	self.hart0 = isa_yaml['hart0']
        self.stvec = self.hart0['stvec']
    	self.rv = self.stvec['reset-val']
        return
    	
    def generate_asm(self) -> Dict[str, str]:
	
        asm = ''
        asm += f'\tli x4, {self.rv}\n'
	asm += '\t csrrw x0,stvec,x4 \n'
        for i in range(0,100):
	   asm += '\t csrr x5,stvec \n'
           asm += '\t csrrc x0,stvec, x5 \n'
           asm += '\t bne x4,stvec,trap \n'
        
        asm += 'trap:\n\taddi x31, x0,1\n'
        
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

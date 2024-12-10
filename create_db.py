from core.api import *

class CreateDB:

    def __init__(self):
        self.init = ProcessInput()
    
    def create_embading(self , pdf_path , db_path , build_new = False):
        self.init.creat_prompt.set_pdf_path(pdf_path ,db_path)
        self.init.creat_prompt.load_create_emb_fassi(build_new)
        return
    
if __name__ == '__main__':
    start = CreateDB()
    start.create_embading('system_prompt/smart.pdf' , 'fassi_db/smart/' , True)
    print('done')
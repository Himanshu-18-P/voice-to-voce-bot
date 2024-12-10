from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os


class PrepareData:

    def __init__(self):
        self.pdf_loader = None
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'})
        self.db_path = None
        self.user_prompt_db = None
    

    def set_pdf_path(self , pdf_path , db_path ):
        self.pdf_loader = PyPDFLoader(pdf_path)
        self.db_path = db_path
        return 
    
    def load_create_emb_fassi(self ,build_new = False):
        documents = self.pdf_loader.load_and_split()
        # print(documents[0])
        if build_new or not(os.path.exists(self.faiss_db_path)):
            vectorstore = FAISS.from_documents(documents=documents, embedding=self.embeddings)
            vectorstore.save_local(self.db_path)
        self.db = FAISS.load_local(self.db_path, self.embeddings, allow_dangerous_deserialization=True)
        return
        
    def retrive_similer_docs_using_fassi(self , question , path):
        if not self.user_prompt_db:
            self.user_prompt_db = FAISS.load_local(path, self.embeddings, allow_dangerous_deserialization=True)
        retireved_results= self.user_prompt_db.similarity_search(question , k=2)
        content = ''
        for result in retireved_results:
            content += result.page_content
        return content
   

if __name__ == '__main__':
    obj = PrepareData()
    pdf_path = '../system_prompt/smart.pdf'
    db_path = 'fassi_db/smart'
    obj.set_pdf_path(pdf_path , db_path)
    obj.load_create_emb_fassi(True)
    # print(obj.retrive_similer_docs_using_chroma('fassi_db/fynd' , 'गंगा आरती कितने बजे होगी?'))
    print('done')


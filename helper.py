import re, uuid, os
import fitz
from models.analysis import analysis

def read_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            text += page.get_text()
    # Limpar texto
    text = re.sub(r'\n\s*\n+', '\n', text)  # Remove múltiplas quebras de linha
    text = re.sub(r'[^\x00-\x7F]+', '', text)  # Remove caracteres não-ASCII
    return text.strip()



def get_pdf_paths(dir):
    pdf_paths = []
    for file in os.listdir(dir):
        if file.endswith(".pdf"):
            file_paths = os.path.join(dir, file)
            pdf_paths.append(file_paths)

    return pdf_paths



def extract_data_analysis(resum_cv, job_id, resum_id, score) -> analysis:
    secoes_dict = {
        "id": str(uuid.uuid4()),
        "job_id": job_id,
        "resum_id": resum_id,
        "name": "",
        "skills": [],
        "education": [],
        "languages": [],
        "score": score, }

    patterns = {
        "name": r"(?:## Nome Completo\s*|Nome Completo\s*\|\s*Valor\s*\|\s*\S*\s*\|\s*)(.*)",
        "skills": r"## Habilidades\s*([\s\S]*?)(?=##|$)",
        "education": r"## Educação\s*([\s\S]*?)(?=##|$)",
        "languages": r"## Idiomas\s*([\s\S]*?)(?=##|$)"
    }

    def clean_string(string: str) -> str:
        return re.sub(r"[\*\-]+", "", string).strip()

    for secao, pattern in patterns.items():
        match = re.search(pattern, resum_cv)
        if match:
            if secao == "name":
                secoes_dict[secao] = clean_string(match.group(1))
            else:
                secoes_dict[secao] = [clean_string(item) for item in match.group(1).split('\n') if item.strip()]

    for key in ["name", "education", "skills"]:
        if not secoes_dict[key] or (isinstance(secoes_dict[key], list) and not any(secoes_dict[key])):
            print(f"Aviso: seção '{key}' vazia. Preenchendo com valor padrão.")
            secoes_dict[key] = ["Não informado"] if key != "name" else "Não informado"

    return analysis(**secoes_dict)
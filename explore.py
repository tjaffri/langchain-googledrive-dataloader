from pathlib import Path


jupyter_notebook_current_file_path = Path(__file__)
cred_path_local = jupyter_notebook_current_file_path.parent / Path(".creds/credentials.json")

from langchain_google_community import GoogleDriveLoader
loader = GoogleDriveLoader(
    folder_id="1x6P7P9LyvGx5Ej1xCZ8jCr0jz8-VSyo2",
    token_path=cred_path_local,
)

docs = loader.load()
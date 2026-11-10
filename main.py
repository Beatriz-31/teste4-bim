from app.config import Config
from app.database import Database
from app.repositorio import LivroRepositorio
from app.usuario import UsuarioRepositorio, Autenticador
from app.seguranca import GerenciadorSessoes
from app.servidor import Servidor

if __name__ == "__main__":
    db = Database(Config)
    Servidor(LivroRepositorio(db), Autenticador(UsuarioRepositorio(db)),
             GerenciadorSessoes(), Config.HTTP_HOST, Config.HTTP_PORT).iniciar()

from django.db import models
from uuid import uuid4



def up_imagem_livro(instace, filename):
    return f"{instace.id_livro}-{filename}"

class Livros(models.Model):
    id_livro = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_lancamento = models.IntegerField()
    estado = models.CharField(max_length=50)
    paginas = models.IntegerField()
    editora = models.CharField(max_length=255)
    criado_em = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to=up_imagem_livro, blank=True, null=True)
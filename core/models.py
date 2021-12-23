# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clientes(models.Model):
    nome = models.CharField(max_length=45)
    telefone = models.CharField(max_length=30)
    endereco = models.CharField(max_length=200)
    cep = models.CharField(max_length=45)
    localidade = models.CharField(max_length=45)
    cpf = models.CharField(max_length=14)
    
    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Compras(models.Model):
    data = models.DateField()
    id_clientes = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_clientes')

    class Meta:
        managed = False
        db_table = 'compras'


class Fabricantes(models.Model):
    nome = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'fabricantes'


class Medicos(models.Model):
    nome = models.CharField(max_length=45)
    crm = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'medicos'
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'


class Produtos(models.Model):
    nome = models.CharField(max_length=45)
    designacao = models.CharField(max_length=60)
    composicao = models.CharField(max_length=200)
    preco_venda = models.DecimalField(max_digits=8, decimal_places=2)
    id_fabricantes = models.ForeignKey(Fabricantes, models.DO_NOTHING, db_column='id_fabricantes')
    id_tipos_produtos = models.ForeignKey('TiposProdutos', models.DO_NOTHING, db_column='id_tipos_produtos')

    class Meta:
        managed = False
        db_table = 'produtos'


class ProdutosCompras(models.Model):
    quantidade = models.IntegerField()
    id_produtos = models.ForeignKey(Produtos, models.DO_NOTHING, db_column='id_produtos')
    id_compras = models.ForeignKey(Compras, models.DO_NOTHING, db_column='id_compras')

    class Meta:
        managed = False
        db_table = 'produtos_compras'


class ReceitasMedicas(models.Model):
    receita = models.CharField(max_length=45)
    id_medicos = models.ForeignKey(Medicos, models.DO_NOTHING, db_column='id_medicos')
    id_produtos_compras = models.ForeignKey(ProdutosCompras, models.DO_NOTHING, db_column='id_produtos_compras')

    class Meta:
        managed = False
        db_table = 'receitas_medicas'


class TiposProdutos(models.Model):
    nome = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipos_produtos'

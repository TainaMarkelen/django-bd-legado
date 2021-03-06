# Generated by Django 3.2.7 on 2021-09-27 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('telefone', models.CharField(max_length=30)),
                ('endereco', models.CharField(max_length=200)),
                ('cep', models.CharField(max_length=45)),
                ('localidade', models.CharField(max_length=45)),
                ('cpf', models.CharField(max_length=14)),
            ],
            options={
                'db_table': 'clientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
            ],
            options={
                'db_table': 'compras',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fabricantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'fabricantes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('crm', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'medicos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('designacao', models.CharField(max_length=60)),
                ('composicao', models.CharField(max_length=200)),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'db_table': 'produtos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProdutosCompras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
            ],
            options={
                'db_table': 'produtos_compras',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReceitasMedicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receita', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'receitas_medicas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TiposProdutos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tipos_produtos',
                'managed': False,
            },
        ),
    ]

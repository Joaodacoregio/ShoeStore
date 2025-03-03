# Generated by Django 5.0.6 on 2024-07-13 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_product_color_product_price_product_reference_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='cost_price',
        ),
        migrations.AddField(
            model_name='product',
            name='profit_margin',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('vermelho', 'Vermelho'), ('azul', 'Azul'), ('verde', 'Verde'), ('amarelo', 'Amarelo'), ('preto', 'Preto'), ('branco', 'Branco')], max_length=10),
        ),
    ]

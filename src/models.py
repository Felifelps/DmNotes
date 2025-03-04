import os
import peewee
from constants import DB_PATH


os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

db = peewee.SqliteDatabase(DB_PATH)


class BaseModel(peewee.Model):
    class Meta:
        database = db


class ImageModel(BaseModel):
    image_path = peewee.CharField(null=True, help_text="Imagem")

    def delete_instance(self, recursive=..., delete_nullable=...):
        if self.image_path:
            os.remove(self.image_path)
        return super().delete_instance(recursive, delete_nullable)


class Character(ImageModel):
    name = peewee.CharField(help_text="Nome")
    class_name = peewee.CharField(help_text="Classe")
    race = peewee.CharField(help_text="Raça")
    status = peewee.CharField(help_text="Status")
    history = peewee.TextField(null=True, help_text="História")
    description = peewee.TextField(null=True, help_text="Descrição")


class Place(BaseModel):
    name = peewee.CharField(help_text="Nome")
    history = peewee.TextField(null=True, help_text="História")
    description = peewee.TextField(null=True, help_text="Descrição")


class Event(BaseModel):
    title = peewee.CharField(help_text="Título")
    history = peewee.TextField(null=True, help_text="História")
    description = peewee.TextField(null=True, help_text="Descrição")


class Item(BaseModel):
    name = peewee.CharField(help_text="Nome")
    history = peewee.TextField(null=True, help_text="História")
    description = peewee.TextField(null=True, help_text="Descrição")


class Item(BaseModel):
    name = peewee.CharField(help_text="Nome")
    history = peewee.TextField(null=True, help_text="História")
    description = peewee.TextField(null=True, help_text="Descrição")


class Sheet(ImageModel):
    name = peewee.CharField(help_text="Nome")
    description = peewee.TextField(null=True, help_text="Descrição")


db.connect()

db.create_tables([Character, Place, Event, Item, Sheet], safe=True)

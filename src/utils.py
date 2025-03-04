import peewee


def get_model_fields(model):
    fields = model._meta.fields
    if type(model) == peewee.ModelBase:
        return fields
    return {field: getattr(model, field) for field in fields}

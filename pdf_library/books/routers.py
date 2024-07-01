class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'default':
            return 'default'
        elif model._meta.app_label == 'second':
            return 'second'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'default':
            return 'default'
        elif model._meta.app_label == 'second':
            return 'second'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'default' and obj2._meta.app_label == 'default':
            return True
        elif obj1._meta.app_label == 'second' and obj2._meta.app_label == 'second':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'default':
            return db == 'default'
        elif app_label == 'second':
            return db == 'second'
        return None

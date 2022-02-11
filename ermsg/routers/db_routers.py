class AllRouter:
    route_app_labels={'admin','auth','contenttypes','sessions','messages','staticfiles','ermsgg','books'}


    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'all_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'all_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
    
        if app_label in self.route_app_labels:
            return db == 'all_db'
        return None

class chartRouter:
    route_app_labels={'charts'}


    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'chart_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'chart_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
    
        if app_label in self.route_app_labels:
            return db == 'chart_db'
        return None
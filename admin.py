"""Admin."""

from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, AdminIndexView
from wtforms.fields import PasswordField
from flask_security import current_user, utils, url_for_security
from flask import redirect

from database import db
from models import User, Role


class SecuredHomeView(AdminIndexView):
    def is_accessible(self):
        return current_user.has_role('admin')

    def _handle_view(self, name, *args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for_security('login', next="/admin"))
        if not self.is_accessible():
            return self.render("admin/denied.html")


class SecuredModelView(ModelView):
    # Prevent administration of Users unless the currently logged-in user has the "admin" role
    def is_accessible(self):
        return current_user.has_role('admin')




# Customized User model for SQL-Admin
class UserAdmin(SecuredModelView):

    # Don't display the password on the list of Users
    column_exclude_list = list = ('password',)

    # Don't include the standard password field when creating or editing a User (but see below)
    form_excluded_columns = ('password',)

    # Automatically display human-readable names for the current and available Roles when creating or editing a User
    column_auto_select_related = True

    # On the form for creating or editing a User, don't display a field corresponding to the model's password field.
    # There are two reasons for this. First, we want to encrypt the password before storing in the database. Second,
    # we want to use a password field (with the input masked) rather than a regular text field.
    def scaffold_form(self):
        # Start with the standard form as provided by Flask-Admin. We've already told Flask-Admin to exclude the
        # password field from this form.
        form_class = super(UserAdmin, self).scaffold_form()
        # Add a password field, naming it "password2" and labeling it "New Password".
        form_class.password2 = PasswordField('New Password')
        return form_class

    # This callback executes when the user saves changes to a newly-created or edited User -- before the changes are
    # committed to the database.
    def on_model_change(self, form, model, is_created):
        # If the password field isn't blank...
        if len(model.password2):
            # ... then encrypt the new password prior to storing it in the database. If the password field is blank,
            # the existing password in the database will be retained.
            model.password = utils.encrypt_password(model.password2)


# Customized Role model for SQL-Admin
class RoleAdmin(SecuredModelView):
    pass


def init_admin(app):
    """Init admin function."""
    admin = Admin(
        app,
        name='admin area',
        index_view=SecuredHomeView(url='/admin'),
        template_mode='bootstrap3'
    )

    admin.add_view(UserAdmin(User, db.session))
    admin.add_view(RoleAdmin(Role, db.session))

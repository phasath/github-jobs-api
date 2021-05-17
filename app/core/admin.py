import yaml

from flask import Response, redirect
from flask_admin import Admin, AdminIndexView
from flask_admin.base import BaseView
from flask_admin.contrib.sqla import ModelView
from flask_basicauth import BasicAuth
from werkzeug.exceptions import HTTPException
from wtforms.fields import TextAreaField
from wtforms.validators import ValidationError

from app.core.extensions import DB
from app.models import Search


auth = BasicAuth()


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(
            message,
            Response(
                "You could not be authenticated. Please refresh the page.",
                401,
                {
                    "WWW-Authenticate": 'Basic realm="admin-protected" logout-timeout=300'
                },
            ),
        )


class SecurityLayerView(BaseView):
    def is_accessible(self):
        if not auth.authenticate():
            raise AuthException("Not authenticated.")
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(auth.challenge())


class BaseModelView(ModelView, SecurityLayerView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page_size = 50
        self.create_modal = True
        self.edit_modal = True

        all_columns = [
            col.name for col in self.model.__table__.columns if col.name != "id"
        ]

        self.column_searchable_list = all_columns
        self.column_filters = all_columns
        self.column_sortable_list = all_columns


class SearchModelView(BaseModelView):
    form_choices = {
        "description": [
            ("go", "Go"),
            ("java", "Java"),
            ("javascript", "Javascript"),
            ("python", "Python"),
            ("react", "React"),
            ("ruby", "Ruby"),
        ],
        "location": [
            ("beijing", "Beijing"),
            ("chicago", "Chicago"),
            ("london", "London"),
            ("paris", "Paris"),
            ("phoenix", "Phoenix"),
            ("san francisco", "San Francisco"),
        ],
    }


class PanelAdminIndexView(AdminIndexView, SecurityLayerView):
    def is_visible(self):
        # This view won't appear in the menu structure
        return False


def admin_setup(appl):
    admin = Admin(
        appl,
        name="Jobs4You Admin",
        index_view=PanelAdminIndexView(url="/admin"),
        template_mode="bootstrap4",
    )

    auth.init_app(appl)
    admin.add_view(SearchModelView(Search, DB.session))

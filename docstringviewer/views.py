"""
Views for the docs app
"""
from django.views.generic import TemplateView

from .conf import PROJECT_ROOT
from .utils import build_tree, get_module_docs


class DocsView(TemplateView):
    """
    Builds project tree and module docs for given module import path in request.
    If module path is not provided in request, first module from first app in
    project is fetched.
    """
    template_name = "docs/main.html"

    def get_context_data(self, **kwargs):
        """
        Builds project tree and module docs for given module import path in request.
        If module path is not provided in request, first module from first app in
        project is fetched.
        """
        context = super(DocsView, self).get_context_data(**kwargs)
        context['module_docs'] = get_module_docs(self.request.GET.get('module'))

        if self.request.is_ajax():
            self.template_name = "docs/docs.html"
        else:
            context['tree'] = build_tree(PROJECT_ROOT, [])

        return context

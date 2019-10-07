from IPython.core.magic import register_cell_magic
from .tagger import _add_tags

@register_cell_magic
def paper_section(line, cell):
   _add_tags("PW_HEADER")

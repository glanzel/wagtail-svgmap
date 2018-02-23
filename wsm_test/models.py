try:
    from wagtail.admin.edit_handlers import StreamFieldPanel
    from wagtail.core import blocks
    from wagtail.core.fields import StreamField
    from wagtail.core.models import Page
except ImportError:
    from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
    from wagtail.wagtailcore import blocks
    from wagtail.wagtailcore.fields import StreamField
    from wagtail.wagtailcore.models import Page

from wagtail_svgmap.blocks import ImageMapBlock


class TestPage(Page):
    template = 'page.html'

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('imagemap', ImageMapBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

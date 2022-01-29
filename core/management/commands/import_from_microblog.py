import logging
from django.core.management.base import BaseCommand
import tempfile
import pathlib

logger = logging.getLogger(__name__)

from ...importers import MicroBlogImporter


class Command(BaseCommand):

    importer = MicroBlogImporter()

    help = (
        "Import posts from a .bar file from Microblog."
        "Accepts a path to a .bar file, extracts the contents, and imports into db"
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "bar_import_path",
            type=str,
            help="The path to the blog archive (.bar) file",
        )

    def handle(self, *args, **options):
        """
        Import posts from microblog, adding them to the first blog index page in the site
        """

        barfile_path = options["bar_import_path"]
        tmpdir = tempfile.TemporaryDirectory()
        tmpdir_path = pathlib.Path(tmpdir.name)
        micro_importer = MicroBlogImporter()

        micro_importer.extract_bar_file(barfile_path, tmpdir_path)
        posts = micro_importer.fetch_posts(target_dir=tmpdir_path)
        articles = micro_importer.create_blog_articles(posts)

        micro_importer.add_articles_to_blog_index(articles)

        self.stdout.write(f"OK. Imported '{len(articles)}' from {barfile_path}")

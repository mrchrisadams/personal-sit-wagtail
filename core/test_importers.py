import pytest
import pathlib
import json
from datetime import datetime
from django.core import management
from core.models import BlogArticlePage, BlogIndexPage

from .importers import MicroBlogImporter

PATH_TO_BAR_FILE = "data/microblog/mrchrisadams_647309.bar"

micro_importer = MicroBlogImporter()


class TestImportMicroBlog:
    def test_read_bar_file(self, tmpdir):
        """
        Can we extract a .bar file, and find the
        json file full of posts?
        """
        micro_importer = MicroBlogImporter()
        blog_files = micro_importer.extract_bar_file(PATH_TO_BAR_FILE, tmpdir)

        assert "feed.json" in [file.name for file in blog_files]

    def test_read_posts_from_archive(self, tmpdir):

        micro_importer = MicroBlogImporter()
        micro_importer.extract_bar_file(PATH_TO_BAR_FILE, tmpdir)
        posts = micro_importer.fetch_posts(target_dir=tmpdir)

        assert len(posts) == 27

    def test_create_full_post_json(self, db, tmpdir):
        """
        Can we create a full wagtail blog article from a
        json post item?
        """

        post_path = pathlib.Path(__file__).parent / "fixtures" / "post.json"
        post = json.load(open(post_path))
        micro_importer = MicroBlogImporter()

        article = micro_importer._create_blog_article(post)
        # pull out our markdown content again
        mkdn = [block for block in article.content][0]

        published_at = datetime.fromisoformat(post.get("date_published"))

        assert mkdn.value == post.get("content_text")
        assert article.tags.names() == post.get("tags")
        assert published_at == article.published_at

    def test_instantiate_posts_from_archive(self, db, tmpdir):

        micro_importer = MicroBlogImporter()
        micro_importer.extract_bar_file(PATH_TO_BAR_FILE, tmpdir)
        posts = micro_importer.fetch_posts(target_dir=tmpdir)
        articles = micro_importer.create_blog_articles(posts)

        assert len(posts) == len(articles)

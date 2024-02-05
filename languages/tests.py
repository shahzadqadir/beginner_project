from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.


class HomePageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        resp = self.client.get(reverse("home"))
        self.assertTemplateUsed(resp, "home.html")

    def test_for_title(self):
        resp = self.client.get(reverse("home"))
        self.assertContains(resp, "<h1>Programming Languages</h1>")

    def test_for_cards(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, '<div class="card">', count=3)


class AboutPageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        resp = self.client.get(reverse("about"))
        self.assertEqual(resp.status_code, 200)

    def test_template_used(self):
        resp = self.client.get(reverse("about"))
        self.assertTemplateUsed(resp, "about.html")

    def test_for_title(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, '<h1>About Page</h1>')

    def test_for_content(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, '<p>This page is an exercise in learning how Django displays templates through URL pattern matching.</p>')


class PythonPageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/python/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        resp = self.client.get(reverse("python"))
        self.assertEqual(resp.status_code, 200)

    def test_correct_template(self):
        resp = self.client.get(reverse("python"))
        self.assertTemplateUsed(resp, "python.html")

    def test_for_title(self):
        response = self.client.get(reverse('python'))
        self.assertContains(response, '<h1>Python</h1>')

    def test_for_subtitles(self):
        response = self.client.get(reverse('python'))
        self.assertContains(response, '<h2>History</h2>')
        self.assertContains(response, '<h2>Uses</h2>')


class FsharppageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/fsharp/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        resp = self.client.get(reverse("fsharp"))
        self.assertEqual(resp.status_code, 200)

    def test_correct_template(self):
        resp = self.client.get(reverse("fsharp"))
        self.assertTemplateUsed(resp, "fsharp.html")

    def test_for_title(self):
        response = self.client.get(reverse('fsharp'))
        self.assertContains(response, '<h1>F#</h1>')

    def test_for_subtitles(self):
        response = self.client.get(reverse('fsharp'))
        self.assertContains(response, '<h2>History</h2>')
        self.assertContains(response, '<h2>Uses</h2>')


class RacketpageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/racket/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        resp = self.client.get(reverse("racket"))
        self.assertEqual(resp.status_code, 200)

    def test_correct_template(self):
        resp = self.client.get(reverse("racket"))
        self.assertTemplateUsed(resp, "racket.html")

    def test_for_title(self):
        response = self.client.get(reverse('racket'))
        self.assertContains(response, '<h1>Racket</h1>')

    def test_for_subtitles(self):
        response = self.client.get(reverse('racket'))
        self.assertContains(response, '<h2>History</h2>')
        self.assertContains(response, '<h2>Uses</h2>')

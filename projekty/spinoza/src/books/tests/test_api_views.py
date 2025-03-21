from django.test import TestCase
from django.urls import reverse
from books.models import Genre


class TestGenreView(TestCase):

    def setUp(self) -> None:
        self.genre1  = Genre.objects.create(name="XXX", description="yyy")
        self.genre2  = Genre.objects.create(name="XXX2", description="yyy2")

        return super().setUp()
    

    def test_list_view(self):
        response = self.client.get(reverse("apibooks:genre_list"))  # /api/v1/genres/
        self.assertEqual(response.status_code, 200)
        expected =  [
            {
            "name": "XXX",
            "slug": "xxx",
            "description": "yyy"
            },
            {
            "name": "XXX2",
            "slug": "xxx2",
            "description": "yyy2"
            },            
        
        ]

        self.assertEqual(response.json(), expected)

    def test_detail_view(self):
        response = self.client.get(reverse("apibooks:genre_detail", args=[1]))  # /api/v1/genres/1
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(), {
            "name": "XXX",
            "slug": "xxx",
            "description": "yyy"
            }
        )

    def test_detail_view_put(self):

        data = {"name": "AAA", "description": "yyy"}

        response = self.client.put(reverse("apibooks:genre_detail", args=[1]), data=data, content_type="application/json")  # /api/v1/genres/1
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(), {
            "name": "AAA",
            "slug": "xxx",
            "description": "yyy"
            }
        )

    def test_post_list_view(self):
        data = {
            "name": "A",
            "description": "aaa"
        }

        expected = {
            "name": "A",
            "slug": "a",
            "description": "aaa"
        }

        response = self.client.post(reverse("apibooks:genre_list"), data=data)  # /api/v1/genres/
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), expected)
    

    def test_delete_genre(self):
        response = self.client.delete(reverse("apibooks:genre_detail", args=[self.genre1.pk]))
        self.assertEqual(response.status_code, 204)

        with self.assertRaises(Genre.DoesNotExist):
            Genre.objects.get(pk=self.genre1.pk)

        

        
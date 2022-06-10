from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Best

# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_best_list(self):
        # 목록 가져오기
        response = self.client.get('/best/best/main/')

        # 페이지 로드
        self.assertEqual(response.status_code, 200)

        # title이 'Best'이다
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Best Coordination')

        #내비 바 체킹
        navbar = soup.nav

        # 포스트가 없다면 0 있다면 두개면 2
        self.assertEqual(Best.objects.count(), 0)
        main_area = soup.find('div', id="main-area")
        self.assertIn('Not Post', main_area.text)

        post_001 = Best.objects.create(
            title="첫 번째",
            content="Hello World!"
        )
        post_002 = Best.objects.create(
            title="두 번째",
            content="Hello World!!"
        )
        self.assertEqual(Best.objects.count(), 2)

        #새로고침했을때
        response = self.client.get('/best/best/main/')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(response.status_code, 200)
        #2개 제목이 있다
        main_area = soup.find('div', id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)
        #문구 x
        self.assertNotIn('Not Post', main_area.text)
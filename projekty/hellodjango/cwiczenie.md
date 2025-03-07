
1. utwórz nowy projekt blog
2. utwórz aplikację posts
3. utwórz model Post z polami takimi jak 
    
class Post(models.Model):
    title = models.Charfield..
    content = models.TextField
    created_at = 
    modified_at = 
    is_published = 

4. przygotuj i wykonaj migracje
5. zintegruj z panelem admina
6. dodaj uzytkownika
7. zaloguj sie do PA
8. utworz 2-3 posty - tak by czesc byla opublikowana a czesc nie
9. utworz widok prezentujacy liste opubkikowanych postow
Post.objects.filter(is_published=True)
10. utworz widok szczegolowo posta
11. utworz potrzebne routingi i szablony
12. mozesz uzyc bootstrapa
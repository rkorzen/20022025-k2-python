import pygame
import random
import math
from abc import ABC, abstractmethod


# Klasa reprezentująca pozycję (współrzędne) w przestrzeni 2D
class Pozycja:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def przesuń(self, dx: float, dy: float) -> None:
        """Przesuwa pozycję o podany wektor (dx, dy)."""
        self.x += dx
        self.y += dy

    def ustaw(self, x: float, y: float) -> None:
        """Ustawia pozycję na konkretne współrzędne."""
        self.x = x
        self.y = y

    def odległość(self, inna_pozycja: 'Pozycja') -> float:
        """Oblicza odległość euklidesową do innej pozycji."""
        return math.sqrt((self.x - inna_pozycja.x) ** 2 + (self.y - inna_pozycja.y) ** 2)

    def __str__(self) -> str:
        """Zwraca tekstową reprezentację pozycji."""
        return f"({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        """Porównuje dwie pozycje."""
        if not isinstance(other, Pozycja):
            return False
        return self.x == other.x and self.y == other.y


class GameObject(ABC):
    def __init__(self, pozycja: Pozycja, color: tuple[int, int, int]):
        self.pozycja = pozycja
        self.color = color

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        pass

    @abstractmethod
    def collides_with(self, other: 'GameObject') -> bool:
        pass


class Circle(GameObject):
    def __init__(self, pozycja: Pozycja, radius: float, color: tuple[int, int, int]):
        super().__init__(pozycja, color)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, (int(self.pozycja.x), int(self.pozycja.y)), int(self.radius))

    def collides_with(self, other: GameObject) -> bool:
        if isinstance(other, Circle):
            distance = self.pozycja.odległość(other.pozycja)
            return distance < (self.radius + other.radius)
        elif isinstance(other, Square):
            closest_x = max(other.pozycja.x, min(self.pozycja.x, other.pozycja.x + other.size))
            closest_y = max(other.pozycja.y, min(self.pozycja.y, other.pozycja.y + other.size))
            closest_point = Pozycja(closest_x, closest_y)
            distance = self.pozycja.odległość(closest_point)
            return distance < self.radius
        return False


class Square(GameObject):
    def __init__(self, pozycja: Pozycja, size: float, color: tuple[int, int, int]):
        super().__init__(pozycja, color)
        self.size = size

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.color, (self.pozycja.x, self.pozycja.y, self.size, self.size))

    def collides_with(self, other: GameObject) -> bool:
        if isinstance(other, Circle):
            return other.collides_with(self)
        return False


class Player(Circle):
    def __init__(self, pozycja: Pozycja, radius: float, speed: float):
        super().__init__(pozycja, radius, (255, 0, 0))  # Czerwony kolor dla gracza
        self.speed = speed
        self.original_radius = radius  # Zapamiętujemy oryginalny promień
        self.shrink_options = 1  # Liczba dostępnych opcji zmniejszenia

    def move(self, dx: float, dy: float, width: int, height: int) -> None:
        new_x = self.pozycja.x + dx * self.speed
        new_y = self.pozycja.y + dy * self.speed

        # Sprawdzanie granic ekranu
        if self.radius <= new_x <= width - self.radius:
            self.pozycja.x = new_x
        if self.radius <= new_y <= height - self.radius:
            self.pozycja.y = new_y

    def grow(self, amount: float) -> None:
        self.radius += amount
        self.original_radius = self.radius  # Aktualizujemy oryginalny promień

    def shrink(self) -> str:
        """Zmniejsza koło gracza o 1/3 jeśli ma dostępne opcje zmniejszenia."""
        if self.shrink_options > 0:
            self.radius = self.radius * 2 / 3  # Zmniejszenie o 1/3
            self.shrink_options -= 1
            return f"Zmniejszono koło! Pozostałe opcje zmniejszenia: {self.shrink_options}"
        else:
            return "Brak dostępnych opcji zmniejszenia!"

    def add_shrink_option(self) -> None:
        """Dodaje opcję zmniejszenia koła."""
        self.shrink_options += 1

    def reset_shrink_options(self) -> None:
        """Resetuje liczbę opcji zmniejszenia."""
        self.shrink_options = 0


class Button:
    def __init__(self, x: int, y: int, width: int, height: int, text: str, color: tuple[int, int, int],
                 hover_color: tuple[int, int, int]):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False

    def draw(self, screen: pygame.Surface) -> None:
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=10)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2, border_radius=10)  # Obramowanie

        font = pygame.font.SysFont('Arial', 24)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos: tuple[int, int]) -> None:
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos: tuple[int, int], mouse_click: bool) -> bool:
        return self.rect.collidepoint(mouse_pos) and mouse_click


class Game:
    def __init__(self):
        pygame.init()
        self.width = 1000
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Zjadacz kół - Wersja Obiektowa")

        self._colors_setup()
        self._statistics_setup()



        # czcionka
        self.font = pygame.font.SysFont('Arial', 24)

        self.button_config = {
            'start': {
                'text': "Rozpocznij grę",
                'y_offset': -25,
            },
            'restart': {
                'text': "Zagraj ponownie",
                'y_offset': 50,
            },
            'yes': {
                'text': "Tak",
                'y_offset': 50,
                'x_offset': -120,  # Dodatkowe przesunięcie w lewo
            },
            'no': {
                'text': "Nie",
                'y_offset': 50,
                'x_offset': 20,  # Dodatkowe przesunięcie w prawo
            },
            'next_level': {
                'text': "Przejdź do następnego poziomu",
                'y_offset': 50,
            },
            'quit': {
                'text': "Wyjdź z gry",
                'y_offset': 120,
            }
        }

        # Przyciski menu
        self._buttons_setup()

        # Inicjalizacja gry
        self.initialize_game()

    def _colors_setup(self):
        # Kolory
        self.SQUARE_COLOR = (10, 10, 190)  # niebieski
        self.CIRCLE_COLOR = (172, 200, 132)  # zielony
        self.BUTTON_COLOR = (211, 211, 211)  # szary
        self.BUTTON_HOVER_COLOR = (230, 230, 230)  # jaśniejszy szary

    def _statistics_setup(self):
        self.num_squares = 10  # Początkowa liczba kwadratów
        self.level = 1
        self.game_state = "menu"  # menu, playing, game_over, win, next_level
        self.game_result = ""
        self.message = ""  # Komunikat dla gracza
        self.message_timer = 0  # Czas wyświetlania komunikatu
        self.next_level_timer = 0  # Timer do automatycznego przejścia do następnego poziomu

    def _buttons_setup(self):

        # Teksty przycisków
        button_height = 50

        def button_width(text: str):
            if len(text) < 10:
                return 100
            elif len(text) < 25:
                return 200
            else:
                return 350

        def button_position(text: str):
            if len(text) < 10:
                return self.width // 2 - 50  # Wycentrowanie dla małych przycisków
            elif len(text) < 25:
                return self.width // 2 - 100  # Wycentrowanie dla średnich przycisków
            else:
                return self.width // 2 - 175  # Wycentrowanie dla dużych przycisków

        # Tworzenie przycisków
        for button_name, config in self.button_config.items():
            x = button_position(config['text'])
            if 'x_offset' in config:
                x += config['x_offset']

            setattr(
                self, f"{button_name}_button", Button(
                    x,
                    self.height // 2 + config['y_offset'],
                    button_width(config['text']),
                    button_height,
                    config['text'],
                    self.BUTTON_COLOR,
                    self.BUTTON_HOVER_COLOR
                ))

    def initialize_game(self):
        """Inicjalizuje nową grę."""
        player_pos = Pozycja(self.width // 2, self.height // 2)
        self.player = Player(player_pos, 20, 5)

        # Zachowujemy opcje zmniejszenia jeśli przechodzimy do następnego poziomu
        if hasattr(self, 'player') and self.game_state == "next_level":
            self.player.shrink_options = getattr(self, 'previous_player_shrink_options', 0)

        self.obstacles = []  # kwadraty
        self.food = []  # koła do zjedzenia

        self._generate_objects()

        # Sprawdzamy, czy pozycja startowa jest bezpieczna
        self._ensure_safe_start_position()

    def _ensure_safe_start_position(self):
        """Upewnia się, że pozycja startowa gracza jest bezpieczna (nie koliduje z przeszkodami)."""
        safe_distance = self.player.radius * 3  # Bezpieczna odległość od przeszkód

        # Sprawdzamy kolizje z przeszkodami
        for obstacle in self.obstacles:
            if self.player.collides_with(obstacle):
                # Przesuwamy przeszkodę na bezpieczną odległość
                direction_x = obstacle.pozycja.x - self.player.pozycja.x
                direction_y = obstacle.pozycja.y - self.player.pozycja.y

                # Normalizacja wektora kierunku
                length = math.sqrt(direction_x ** 2 + direction_y ** 2)
                if length > 0:
                    direction_x /= length
                    direction_y /= length

                # Przesunięcie przeszkody
                new_x = self.player.pozycja.x + direction_x * safe_distance
                new_y = self.player.pozycja.y + direction_y * safe_distance

                # Upewniamy się, że przeszkoda jest w granicach ekranu
                new_x = max(0, min(new_x, self.width - obstacle.size))
                new_y = max(0, min(new_y, self.height - obstacle.size))

                obstacle.pozycja.ustaw(new_x, new_y)

    def _generate_objects(self):
        """Generuje obiekty gry: przeszkody i jedzenie."""
        # Generowanie kwadratów
        self._generate_squares()

        # Generowanie kół do zjedzenia
        self._generate_food()

        # przesunięcie kół które są w kwadratach
        self._move_food_from_obstacles()

    def _generate_squares(self):
        for _ in range(self.num_squares):
            pos = Pozycja(
                random.randint(0, self.width - 40),  # Uwzględniamy rozmiar kwadratu
                random.randint(0, self.height - 40)
            )
            self.obstacles.append(
                Square(
                    pos,
                    random.randint(20, 40),
                    self.SQUARE_COLOR
                )
            )

    def _generate_food(self):
        for _ in range(5):
            pos = Pozycja(
                random.randint(0, self.width - 30),  # Uwzględniamy promień koła
                random.randint(0, self.height - 30)
            )
            self.food.append(
                Circle(
                    pos,
                    random.randint(10, 15),
                    self.CIRCLE_COLOR
                )
            )

    def _move_food_from_obstacles(self):
        for obstacle in self.obstacles:
            for food in self.food:
                if food.pozycja.odległość(obstacle.pozycja) < obstacle.size:
                    food.pozycja.ustaw(random.randint(0, self.width - obstacle.size),
                                       random.randint(0, self.height - obstacle.size))

    def handle_input(self):
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_DOWN]:
            dy = 1
        self.player.move(dx, dy, self.width, self.height)

        # Obsługa klawisza Z do zmniejszania koła
        if keys[pygame.K_z]:
            self.message = self.player.shrink()
            self.message_timer = 120  # Wyświetlaj komunikat przez 2 sekundy (przy 60 FPS)

    def update(self) -> bool:
        # Aktualizacja timera komunikatu
        if self.message_timer > 0:
            print(self.message_timer)
            self.message_timer -= 1
            if self.message_timer == 0:
                self.message = ""

        # Aktualizacja timera przejścia do następnego poziomu
        if self.game_state == "next_level" and self.next_level_timer > 0:
            self.next_level_timer -= 1
            if self.next_level_timer == 0:
                # Zapamiętujemy opcje zmniejszenia przed inicjalizacją nowej gry
                self.previous_player_shrink_options = self.player.shrink_options
                self.initialize_game()
                self.game_state = "playing"
                return True

        # Sprawdzanie kolizji z jedzeniem
        food_to_remove = []
        for i, food_circle in enumerate(self.food):
            if self.player.collides_with(food_circle):
                food_to_remove.append(i)
                self.player.grow(2)

        # Usuwanie zjedzonego jedzenia
        for i in sorted(food_to_remove, reverse=True):
            self.food.pop(i)

        # Sprawdzanie kolizji z przeszkodami
        for obstacle in self.obstacles:
            if self.player.collides_with(obstacle):
                self.game_state = "game_over"
                self.game_result = "Przegrana! Dotknąłeś kwadratu!"
                return False

        # Sprawdzanie warunku zwycięstwa
        if not self.food:
            self.game_state = "next_level"
            self.game_result = f"Wygrana! Zjadłeś wszystkie koła! Poziom {self.level} ukończony."
            self.level += 1
            self.num_squares += 2  # Zwiększenie liczby kwadratów o 2
            self.player.add_shrink_option()  # Dodanie opcji zmniejszenia koła
            self.next_level_timer = 180  # 3 sekundy do następnego poziomu (przy 60 FPS)
            return False

        return True

    def draw_game(self):
        self.screen.fill((255, 255, 255))  # Białe tło

        # Rysowanie wszystkich obiektów
        self.player.draw(self.screen)
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
        for food in self.food:
            food.draw(self.screen)

        # Wyświetlanie informacji o poziomie

        level_text = self.font.render(f"Poziom: {self.level}", True, (0, 0, 0))
        squares_text = self.font.render(f"Liczba kwadratów: {self.num_squares}", True, (0, 0, 0))
        food_text = self.font.render(f"Pozostało kół: {len(self.food)}", True, (0, 0, 0))
        shrink_text = self.font.render(f"Opcje zmniejszenia (Z): {self.player.shrink_options}", True, (0, 0, 0))

        self.screen.blit(level_text, (10, 10))
        self.screen.blit(squares_text, (10, 40))
        self.screen.blit(food_text, (10, 70))
        self.screen.blit(shrink_text, (10, 100))

        # Wyświetlanie komunikatu
        if self.message:
            message_font = pygame.font.SysFont('Arial', 20)
            message_surface = message_font.render(self.message, True, (255, 0, 0))
            message_rect = message_surface.get_rect(center=(self.width // 2, 30))
            self.screen.blit(message_surface, message_rect)

    def draw_menu(self):
        self.screen.fill((255, 255, 255))  # Białe tło

        title = self.font.render("Zjadacz kół", True, (0, 0, 0))
        title_rect = title.get_rect(center=(self.width // 2, 100))
        self.screen.blit(title, title_rect)

        instructions1 = self.font.render(
            "Użyj strzałek do poruszania się. Zjedz wszystkie zielone koła, unikaj niebieskich kwadratów.", True,
            (0, 0, 0))
        instructions1_rect = instructions1.get_rect(center=(self.width // 2, 170))
        self.screen.blit(instructions1, instructions1_rect)

        instructions2 = self.font.render(
            "Naciśnij Z, aby zmniejszyć swoje koło o 1/3. Zdobywasz tę opcję za każdą wygraną.", True, (0, 0, 0))
        instructions2_rect = instructions2.get_rect(center=(self.width // 2, 200))
        self.screen.blit(instructions2, instructions2_rect)

        self.start_button.draw(self.screen)
        self.quit_button.draw(self.screen)

    def draw_game_over(self):
        font = self.font

        self.screen.fill((255, 255, 255))  # Białe tło

        title = font.render("Koniec gry", True, (0, 0, 0))
        title_rect = title.get_rect(center=(self.width // 2, 100))
        self.screen.blit(title, title_rect)

        result = font.render(self.game_result, True, (0, 0, 0))
        result_rect = result.get_rect(center=(self.width // 2, 170))
        self.screen.blit(result, result_rect)

        stats = font.render(f"Poziom: {self.level} | Liczba kwadratów: {self.num_squares}", True, (0, 0, 0))
        stats_rect = stats.get_rect(center=(self.width // 2, 220))
        self.screen.blit(stats, stats_rect)

        shrink_stats = font.render(f"Opcje zmniejszenia: {self.player.shrink_options}", True, (0, 0, 0))
        shrink_stats_rect = shrink_stats.get_rect(center=(self.width // 2, 250))
        self.screen.blit(shrink_stats, shrink_stats_rect)

        # Jeśli przegrana, pytamy czy zagrać ponownie
        if self.game_state == "game_over":
            question = font.render("Czy chcesz zagrać ponownie?", True, (0, 0, 0))
            question_rect = question.get_rect(center=(self.width // 2, 300))
            self.screen.blit(question, question_rect)

            self.yes_button.draw(self.screen)
            self.no_button.draw(self.screen)
        else:
            # Jeśli wygrana, pokazujemy informację o przejściu do następnego poziomu
            next_level = font.render(
                f"Przechodzenie do poziomu {self.level} za {self.next_level_timer // 60 + 1} sekund...", True,
                (0, 0, 0))
            next_level_rect = next_level.get_rect(center=(self.width // 2, 300))
            self.screen.blit(next_level, next_level_rect)

            # Dodajemy przycisk do ręcznego przejścia do następnego poziomu
            self.next_level_button.draw(self.screen)
            self.quit_button.draw(self.screen)

    def draw(self):
        if self.game_state == "menu":
            self.draw_menu()
        elif self.game_state == "playing":
            self.draw_game()
        elif self.game_state in ["game_over", "next_level"]:
            self.draw_game_over()

        pygame.display.flip()

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Lewy przycisk myszy
                        mouse_click = True

            if self.game_state == "menu":
                self.start_button.check_hover(mouse_pos)
                self.quit_button.check_hover(mouse_pos)

                if self.start_button.is_clicked(mouse_pos, mouse_click):
                    self.game_state = "playing"
                elif self.quit_button.is_clicked(mouse_pos, mouse_click):
                    running = False

            elif self.game_state == "playing":
                self.handle_input()
                if not self.update():
                    # Gra się zakończyła (wygrana lub przegrana)
                    pass

            elif self.game_state == "game_over":
                self.yes_button.check_hover(mouse_pos)
                self.no_button.check_hover(mouse_pos)

                if self.yes_button.is_clicked(mouse_pos, mouse_click):
                    # Resetujemy poziom, liczbę kwadratów i opcje zmniejszenia
                    self.level = 1
                    self.num_squares = 10
                    self.player.reset_shrink_options()
                    self.initialize_game()
                    self.game_state = "playing"

                elif self.no_button.is_clicked(mouse_pos, mouse_click):
                    running = False

            elif self.game_state == "next_level":
                self.next_level_button.check_hover(mouse_pos)
                self.quit_button.check_hover(mouse_pos)

                if self.next_level_button.is_clicked(mouse_pos, mouse_click):
                    # Ręczne przejście do następnego poziomu
                    self.previous_player_shrink_options = self.player.shrink_options
                    self.initialize_game()
                    self.game_state = "playing"
                elif self.quit_button.is_clicked(mouse_pos, mouse_click):
                    running = False

                # Automatyczne przejście do następnego poziomu obsługiwane w update()

            self.draw()
            clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
from time import sleep


class User:
    """
    Класс пользователя, содержит атрибуты: логин(строка), пароль(в хэшированом виде), возраст(число)
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    """
    Класс видео, содержит атрибуты: заголовок(строка), продолжительность(секунды),
    секунда остановки(по умолчанию 0), ограничение по возрасту(bool, False по умолчанию)
    """

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    """
    Атрибуты: users(список пользователей), videos(список видео),
    current_user(текущий пользователь, User)
    Метод log_in, авторизация пользователя
    Метод register, регистрация пользователя
    Метод log_out выход
    Метод add, добавить видео
    Метод get_videos, поиск видео
    Метод watch_video, воспроизвести видео
    """

    def __init__(self, current_user=None):
        self.current_user = current_user
        self.users = []
        self.videos = []

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and hash(password) == user.password:
                self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word):
        list_video = []
        for video in self.videos:
            if search_word.upper() in video.title.upper():
                list_video.append(video.title)
        return list_video

    def watch_video(self, movie_title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if video.title == movie_title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for sec in range(video.duration):
                        video.time_now = 1 + sec
                        print(video.time_now, end=' ')
                        sleep(1)
                    video.time_now = 0
                    print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

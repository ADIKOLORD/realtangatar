from django.db import models


class Student(models.Model):
    fullname = models.CharField(max_length=50, verbose_name="ФИО ученика")
    image = models.ImageField(upload_to="students/", verbose_name="Фото")

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "Окуучу"
        verbose_name_plural = "Окуучулар"


class Teacher(models.Model):
    USULBIRIK = (
        ("1", "Кыргыз тили усулдук бирикмеси"), ("2", "Орус тили усулдук бирикмеси"),
        ("3", "Англис тили усулдук бирикмеси"), ("4", "Табигый илимдер усулдук бирикмеси"),
        ("5", "Так илимдер усулдук бирикмеси"), ("6", "Социалдык илимдер усулдук бирикмеси"),
        ("7", "Технология жана ден-соолук маданияты усулдук бирикмеси")
    )
    birikme = models.CharField(max_length=30, verbose_name="Усулдук Бирикме", choices=USULBIRIK)
    fullname = models.CharField(max_length=50, verbose_name="ФИО учителя")
    biography = models.CharField(max_length=50, verbose_name="Биография")
    image = models.ImageField(upload_to="teachers/")

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "Мугалим"
        verbose_name_plural = "Мугалимдер"


class Endowment(models.Model):
    fond_jobosu = models.FileField(verbose_name="Фонддун жобосу", upload_to="fondjobosu/")
    student_list = models.FileField(
        verbose_name="Бутуруучулордун тизмеси", upload_to="studentslist/")

    def __str__(self):
        return f"{self.id} - Эндаумент"

    class Meta:
        verbose_name = "Эндаумент"
        verbose_name_plural = "Эндаументы"


class MediaTheme(models.Model):
    theme = models.CharField(max_length=50, verbose_name="Тема мероприятия")

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = "Мероприятия"
        verbose_name_plural = "Мероприятия"


class MediaContent(models.Model):
    theme = models.ForeignKey(
        MediaTheme, on_delete=models.CASCADE, related_name="mycontent", verbose_name="Тема")
    image = models.ImageField(upload_to="images/", verbose_name="Фото", blank=True)
    video = models.URLField(verbose_name="Видео", blank=True, help_text="Cсылка на видео")
    desc = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.theme}"

    def save(self, *args, **kwargs):
        # default = https://youtu.be/B0y2ztR1kKc
        # must to change = https://www.youtube.com/embed/B0y2ztR1kKc
        if self.video:
            main_url = str(self.video).split("/")[-1]
            self.video = f"https://www.youtube.com/embed/{main_url}"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Фото-Видео"
        verbose_name_plural = "Фото-Видео"


class Accreditation(models.Model):
    year = models.CharField(max_length=20, verbose_name="Жылы(год)")

    def __str__(self):
        return f"Аккредитация - {self.year}"

    class Meta:
        verbose_name = "Аккредитация"
        verbose_name_plural = "Аккредитация"


class Ustav(models.Model):
    year = models.ForeignKey(
        to=Accreditation, on_delete=models.CASCADE, verbose_name="Жылы(год)",
        related_name="ustavtar",
    )
    title = models.CharField(max_length=100, verbose_name='Название')
    ustav = models.FileField(verbose_name="у-ч Актылар", upload_to="documents/ustav/")

    def __str__(self):
        return f"у.ч актылар - {self.title}"

    class Meta:
        verbose_name = "У-ч Актылар"
        verbose_name_plural = "У-ч Актылар"


class Protocol(models.Model):
    year = models.ForeignKey(
        to=Accreditation, on_delete=models.CASCADE, verbose_name="Жылы(год)",
        related_name="protocols",
    )
    title = models.CharField(max_length=100, verbose_name='Название')
    protocol = models.FileField(verbose_name="Протокол", upload_to="documents/protocol/")

    def __str__(self):
        return f"Протокол - {self.title}"

    class Meta:
        verbose_name = "Протокол"
        verbose_name_plural = "Протоколдор"


class Jobo(models.Model):
    year = models.ForeignKey(
        to=Accreditation, on_delete=models.CASCADE, verbose_name="Жылы(год)",
        related_name="jobolor",
    )
    title = models.CharField(max_length=100, verbose_name='Название')
    jobo = models.FileField(verbose_name="Жобо", upload_to="documents/jobo/")

    def __str__(self):
        return f"Жобо - {self.title}"

    class Meta:
        verbose_name = "Жобо"
        verbose_name_plural = "Жоболор"


class Plan(models.Model):
    year = models.ForeignKey(
        to=Accreditation, on_delete=models.CASCADE, verbose_name="Жылы(год)",
        related_name="plans",
    )
    title = models.CharField(max_length=100, verbose_name='Название')
    plan = models.FileField(verbose_name="План", upload_to="documents/plan/")

    def __str__(self):
        return f"План - {self.title}"

    class Meta:
        verbose_name = "План"
        verbose_name_plural = "Пландар"


class Banner(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    desc = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="banners/", verbose_name="Фото")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннер"

from django.db import models  
  
class Task(models.Model):  
    class Status(models.TextChoices):  
        CREATED = 'cr', 'Создана'  
        IN_PROGRESS = 'in', 'В прогрессе'  
        DONE = 'dn', 'Сделан'  
        CANCELED = 'cn', 'Отклонен'  
        EXPIRED = 'ex', 'Просрочен'  
  
    title = models.CharField(max_length=252, verbose_name='Титуд')  
    description = models.TextField(verbose_name='Описание')  
    deadline = models.DateField(verbose_name='Дедлайн')  
    status = models.CharField(max_length=2, choices=Status.choices, verbose_name='Статус')  
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Создан')  
    updated_ad = models.DateTimeField(auto_now=True, verbose_name='Обновлен')  
  
    def __str__(self) -> str:  
        return f'{self.title} ({self.get_status_display()}) - {self.deadline}'  
  
    class Meta:  
        verbose_name= 'Задача'  
        verbose_name_plural = 'Задачи'
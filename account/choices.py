GENDER_CHOICES = (
    ('M', 'мужской'),
    ('F', 'женский'),
)

class MessageStatus:
    SEND = 'send'
    RECD = 'recd'
    READ = 'read'

    CHOICES = (
        (SEND, 'Отправлено'),
        (RECD, 'Получено'),
        (READ, 'Прочитано')
    )

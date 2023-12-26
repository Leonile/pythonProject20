import time

from Test.test_base import TestBase


class TestSettings(TestBase):

    def test_view_schedule_from_me(self):
        # Вариант 7 Кабиров И.Р. 20ИО
        #
        # Нажимаем на кнопку Шестеренки
        self.APP.sidebar.click_on_settings()
        time.sleep(1)
        # Выбираем кафедру
        self.APP.tab_settings.select_cathedra('Информационные технологии и системы связи')
        time.sleep(1)
        # Переходим к расписанию
        self.APP.sidebar.click_on_schedule()
        time.sleep(1)
        # Выбираем группу
        self.APP.tab_schedule.select_group_or_teacher('47 С')
        time.sleep(1)
        # Проверяем есть ли группа
        assert self.APP.tab_schedule.check_group_or_teacher_on_page('47 С')
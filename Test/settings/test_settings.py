from Test.test_base import TestBase


class TestSettings(TestBase):

    def test_view_schedule_from_me(self):
        # Нажимаем на кнопку Шестеренки
        self.APP.sidebar.click_on_settings()
        # Меняем режим отображения расписания для пользователя
        self.APP.tab_settings.click_button_change_view()
        # Выбираем кафедру
        self.APP.tab_settings.select_cathedra('Гуманитарные науки')
        # Переходим к расписанию
        self.APP.sidebar.click_on_schedule()
        # Выбираем преподавателя
        self.APP.tab_schedule.select_teacher('Бухалова Н.А.')
        # Проверяем наличие пары
        assert self.APP.tab_schedule.check_lesson_on_page('Построение воспитывающей образовательной среды')
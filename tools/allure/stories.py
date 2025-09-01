from enum import Enum


class AllureStory(str, Enum):
    COURSES = "Courses"
    DASHBOARD = "Dashboard"
    REGISTRATION = "Registration"
    AUTHORIZATION = "Authorization"

# @allure.suite
# @allure.sub_suite
# @allure.parent_suite
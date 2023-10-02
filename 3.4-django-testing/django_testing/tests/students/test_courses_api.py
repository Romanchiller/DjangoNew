from random import choice

import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    course = course_factory(_quantity=1)

    response = client.get('/api/v1/courses/1/')
    data = response.json()

    assert data['id'] == course[0].id
    assert data['id'] == 1
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_list_courses(client, course_factory):
    courses = course_factory(_quantity=3)

    response = client.get('/api/v1/courses/')
    data = response.json()

    assert response.status_code == 200
    assert len(data) == 3
    for index, course in enumerate(data):
        assert course['name'] == courses[index].name
        assert course['id'] == courses[index].id


@pytest.mark.django_db
def test_filter_id(client, course_factory):
    courses = course_factory(_quantity=5)

    response = client.get('/api/v1/courses/?id=6')
    data = response.json()

    assert data[0]['id'] == 6
    assert response.status_code == 200


@pytest.mark.django_db
def test_filter_name(client, course_factory):
    courses = course_factory(_quantity=5)
    random_course = choice(courses)
    course_name = random_course.name

    response = client.get(f'/api/v1/courses/?name={course_name}')
    data = response.json()

    assert data[0]['name'] == course_name
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_course(client):
    course = {'name': 'Python'
             }

    response = client.post('/api/v1/courses/', course)
    data = response.json()

    assert data['name'] == 'Python'
    assert response.status_code == 201


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory(_quantity=1)
    course_id = course[0].id
    update = {'name': 'Python'}


    response = client.patch(f'/api/v1/courses/{course_id}/', update)
    data = response.json()

    assert update['name'] == data['name']
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory(_quantity=1)
    course_id = course[0].id

    response = client.delete(f'/api/v1/courses/{course_id}/')

    assert response.status_code == 204

#EXTRA TEST TO TEST GET TEACHERS API
def test_teachers_api(client, h_principal):
    response = client.get(
        '/principal/teachers',
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']
    assert len(data) == 2

#THIS IS AN EXTRA TEST FOR GRADING API
def test_grade_assignment(client, h_teacher_1):
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            "id": 1,
            "grade": "A"
        }
    )

    assert response.status_code == 200

    data = response.json['data']
    assert data['state'] == 'GRADED'
    assert data['grade'] == 'A'

#TESTING IF APP ONLINE
def test_server(client):
    response = client.get('/')
    assert response.status_code == 200
    response = response.json
    assert response['status'] == 'ready'
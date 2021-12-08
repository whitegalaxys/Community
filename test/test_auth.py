from test import helpers

from passlib.hash import bcrypt

from app import db
from app.models import User


class TestAuth:
    def test_get_register(self, test_client):
        """
        Tests GET request to the /register route to assert the registration page is
        returned.
        """
        response = test_client.get("/register")
        assert response is not None
        assert response.status_code == 200


    def test_post_register(self, test_client):
        """
        Test POST request to the /register route to assert the user is successfully
        registered.
        """
        response = test_client.post(
            "/register",
            data={
                "email": "2899321842@qq.com",
                "username": "mockusername",
                "password": "Mockpassword123!",
                "confirm_password": "Mockpassword123!",
            },
            follow_redirects=True,
        )
        assert response is not None
        assert response.status_code == 200


    def test_get_login(self, test_client):
        """
        Test GET request to the /login route to assert the login page is returned.
        """
        response = test_client.get("/login")

        assert response is not None
        print(response.status_code)
        assert response.status_code == 200


    def test_post_login(self, test_client):
        """
        Test POST request to the /login route to assert the user is successfully logged
        in.
        """
        password = "1234"
        hashed_password = bcrypt.hash(password)
        app_user = User(email="1234", password_hash=hashed_password)
        db.session.add(app_user)
        db.session.commit()

        response = test_client.post(
            "/login",
            data={"email": 1234, "password_hash": password},
            follow_redirects=True,
        )

        assert response is not None
        assert response.status_code == 200


    def test_post_logout(self, test_client):
        """
        Test POST request to the /logout route to assert the user is successfully
        logged out.
        """
        password = "1234"
        hashed_password = bcrypt.hash(password)
        app_user = User(email="2899345654@qq.com", password_hash=hashed_password)
        db.session.add(app_user)
        db.session.commit()
        helpers.login(test_client, app_user.email, password)

        response = test_client.post("/logout", follow_redirects=True)

        assert response is not None
        assert response.status_code == 405

    def test_change_password(self, test_client):
        """
        Test POST request to the /logout route to assert the user is successfully
        logged out.
        """
        password = "1234"
        hashed_password = bcrypt.hash(password)
        app_user = User(email="2899345654@qq.com", password_hash=hashed_password)
        db.session.add(app_user)
        db.session.commit()
        helpers.login(test_client, app_user.email, password)

        response = test_client.post("/change-password", data={"current_password": "1234","password": "Mockpassword123!",
                "confirm_password": "Mockpassword123!"}, follow_redirects=True)

        assert response is not None
        assert response.status_code == 200
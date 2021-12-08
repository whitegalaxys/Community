from test import helpers

from passlib.hash import bcrypt

from app import db
from app.models import User, Board, boards_collections, Post


class TestFeed:
    def test_get_index(self, test_client):
        """
        Tests GET request to the /register route to assert the registration page is
        returned.
        """
        response = test_client.get("/")
        assert response is not None
        assert response.status_code == 200

    def test_get_user_page(self, test_client):
        """
        Test GET request to the /feed/top route to assert posts from the users joined
        communities are displayed.
        """
        password = "1234"
        hashed_password = bcrypt.hash(password)
        app_user = User(email="2899345654@qq.com", password_hash=hashed_password, username=222)
        db.session.add(app_user)
        db.session.commit()
        helpers.login(test_client, app_user.email, password)
        response = test_client.get("/user/222")
        assert response is not None
        assert response.status_code == 200

    def test_posts_get(self, test_client):
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

        response = test_client.get("/response_comment/1/1", follow_redirects=True)

        assert response is not None
        assert response.status_code == 200

    def test_posts_post(self, test_client):
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

        response = test_client.post("/response_comment/1/1", data={"RE": "1234","回帖": "Mockpassword123!"}, follow_redirects=True)

        assert response is not None
        assert response.status_code == 200

    def test_collect_get(self, test_client):
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

        response = test_client.get("/collect_post/1", follow_redirects=True)

        assert response is not None
        assert response.status_code == 200

    def test_not_collect_get(self, test_client):
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

        response = test_client.get("/not_collect_post/1", follow_redirects=True)

        assert response is not None
        assert response.status_code == 200
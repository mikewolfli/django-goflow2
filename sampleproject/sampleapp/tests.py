import json
import os
import tempfile

from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from django.test.client import Client

from goflow.workflow.models import Process, Activity
from sampleproject.sampleapp.models import SampleModel


class ApiAuthTests(TestCase):
    def setUp(self):
        self.client = Client()

    def _assert_unauthorized(self, response, allow_validation_error=False):
        allowed = [401, 403]
        if allow_validation_error:
            allowed.append(422)
        self.assertIn(response.status_code, allowed)

    def test_protected_endpoints_require_auth(self):
        response = self.client.get("/api/protected/me")
        self._assert_unauthorized(response)

        response = self.client.get("/api/protected/processes")
        self._assert_unauthorized(response)

        response = self.client.get("/api/protected/processes/1/activities")
        self._assert_unauthorized(response)

        response = self.client.get("/api/protected/workitems")
        self._assert_unauthorized(response)

        response = self.client.get("/api/protected/my/workitems")
        self._assert_unauthorized(response)

        response = self.client.post("/api/protected/workitems/1/activate")
        self._assert_unauthorized(response)

        response = self.client.post(
            "/api/protected/workitems/1/complete",
            data="{}",
            content_type="application/json",
        )
        self._assert_unauthorized(response, allow_validation_error=True)

        response = self.client.post(
            "/api/protected/processes/start",
            data="{}",
            content_type="application/json",
        )
        self._assert_unauthorized(response, allow_validation_error=True)


class ApiJwtFlowTests(TestCase):
    TEST_JWT_PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC/5OT4+1TvBTau
kUr+JlicQvJxqZcjfIhl0a6o8UvRQrzQVH8ZyPmtwdACRc7pYrgzoGZ4qTkOg6SF
Zo/X5bSoxxJx9x+64V/mnVtWj+G8euV6HRx/PuhIUvr7nXisBSvqMusTcecoKXzP
pVEH6NAnXTVwItTOW45FihNqlBUt+ju2ZaQuuiA1hOKXWAH5VEuNLFI5aqktGoBv
MlnGNh9/gBKQdzCCgEzoV+jDQUWRXxg74O0tTTFwtLn07PDZkHgHStEyjnsIGyay
+afgfhemzlE1qS4v7n6kV4Y3TQAwwSb9m4mhphYuW1aD3EkGx+w+i25oLLE9VyGB
ud/TswDpAgMBAAECggEANy89RfkJWN+X9SXleidO7kk2bceGpnbmxtlBMGaMFjbq
E8No9eJdI0IMbsrikS2JqZckQOjxdqIXCyIOldkCVlNBk7Ks1lKAANMZ9E/WbByv
p6l9i35s0HfEo92KWXX3Rhe0kNf90Qf1U8XIAs1KJzff6UqrBllAFfF6WfkSCjFe
sJl723vbIE/tG3eTQAzNWr9J5eg7KVLQhVIm8fpAlNsLq2Mk2VFSV1E5Bdh0kABr
I1xUEs5IV1zHME/yaZZk2S+8Nwx9sxuPyyBIui3dgCWDmL0ggQMSWR98pgRnogoI
/j92P/38al04WvvuAG4WscH81zoG/j6kuNK3l27MLQKBgQD8eMF+XuOq9p0EoWcf
vpw+nzajWCVum4g3hZRhcRQZZBx3OzyBX1KMzZGkHuav40tq4soqPUuxqPopWdvD
4v6vcFdxeQznmTuygod3Qg+qgsd8gwgfgg9n/jN/tt0f9/PUJoNGGOYsPyOMbNWW
EXXO1Y2VFuP1lAj66F1S7mZCpwKBgQDCk2p3wkklJOS5QQFZqCE7dSgirER+jtP2
BuEieqIQVWTSdfCV1uhRhCTsg6AxPZiEgbkdKwF/RNPBA7kGeZ8aRTMrCfL1CGmK
ZtvXSlSfc8XMcwzxvtC2c3pnOEh2ati4JwZhuSEb0f371A7LdQ3+f0WrAot9pqXe
40LRg+rh7wKBgCU5rNX0Kb9oc0hef/UHRsRY91ZoRcSkPBZrpLAlWyBPSX8vBcHR
iztliAbZ44uliNYusD5AIWwFjTURobylOIYnm00I2yU+y7WLV2v3GpY6iC1MqKL0
q07bBT7ceIghKBtsvkhUnYOCn7wxw+BHnMYtaJ3F7UClXhmYr0HuErfbAoGAITLh
4Zkmvc2zsOAkiNWlBe4RcQkPjsBz7fByjV17NWo8j6RL7mUCspXnbutuc7hcw48W
tKFX2g02TCKEeVRbDzJrbpZ9+8z5pQGz1OH72lD4mM+wj7bNCbReWCpEQuAsJg+S
iS37NjH4MfWWqKRKRPgWPP1sK345ovQHvJPTicUCgYA6Yvfsys17gWxMvdvUf3fp
yWXbKUepy4cQq+TT5gnK/IRuO/HPw6i9ocuNcufSwHzF2RWJvDQJFgUQ1Hz2gcUu
MqWkMExVtSc1r7sAK6jPLMita78DT+g2YW3YuiR7ikVay0jffUSG3f7mt5AtKSCx
QXtXwqBxlyuQALuCfi+Ljw==
-----END PRIVATE KEY-----
"""
    TEST_JWT_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv+Tk+PtU7wU2rpFK/iZY
nELycamXI3yIZdGuqPFL0UK80FR/Gcj5rcHQAkXO6WK4M6BmeKk5DoOkhWaP1+W0
qMcScfcfuuFf5p1bVo/hvHrleh0cfz7oSFL6+514rAUr6jLrE3HnKCl8z6VRB+jQ
J101cCLUzluORYoTapQVLfo7tmWkLrogNYTil1gB+VRLjSxSOWqpLRqAbzJZxjYf
f4ASkHcwgoBM6Ffow0FFkV8YO+DtLU0xcLS59Ozw2ZB4B0rRMo57CBsmsvmn4H4X
ps5RNakuL+5+pFeGN00AMMEm/ZuJoaYWLltWg9xJBsfsPotuaCyxPVchgbnf07MA
6QIDAQAB
-----END PUBLIC KEY-----
"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls._jwt_dir = tempfile.TemporaryDirectory()
        cls._private_key_path = os.path.join(cls._jwt_dir.name, "jwt-signing.pem")
        cls._public_key_path = os.path.join(cls._jwt_dir.name, "jwt-signing.pub")
        with open(cls._private_key_path, "w", encoding="utf-8") as handle:
            handle.write(cls.TEST_JWT_PRIVATE_KEY)
        with open(cls._public_key_path, "w", encoding="utf-8") as handle:
            handle.write(cls.TEST_JWT_PUBLIC_KEY)

    @classmethod
    def tearDownClass(cls):
        cls._jwt_dir.cleanup()
        super().tearDownClass()

    def setUp(self):
        self.client = Client()
        user_model = get_user_model()
        self.user = user_model.objects.create_user(
            username="apiuser",
            password="pass1234",
            email="apiuser@example.com",
        )

    def _post_json(self, url, payload):
        return self.client.post(
            url,
            data=json.dumps(payload),
            content_type="application/json",
        )

    def test_web_sign_in_and_me(self):
        with override_settings(
            NINJA_SIMPLE_JWT={
                "USE_STATELESS_AUTH": True,
                "JWT_PRIVATE_KEY_PATH": self._private_key_path,
                "JWT_PUBLIC_KEY_PATH": self._public_key_path,
            }
        ):
            response = self._post_json(
                "/api/auth/web/sign-in",
                {"username": "apiuser", "password": "pass1234"},
            )
            self.assertEqual(response.status_code, 200)
            data = response.json()
            access = data.get("access") or data.get("token")
            self.assertTrue(access)
            self.assertIn("refresh", response.cookies)

            response = self.client.get(
                "/api/protected/me",
                HTTP_AUTHORIZATION=f"Bearer {access}",
            )
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertEqual(data.get("username"), "apiuser")

    def test_web_token_refresh(self):
        with override_settings(
            NINJA_SIMPLE_JWT={
                "USE_STATELESS_AUTH": True,
                "JWT_PRIVATE_KEY_PATH": self._private_key_path,
                "JWT_PUBLIC_KEY_PATH": self._public_key_path,
            }
        ):
            response = self._post_json(
                "/api/auth/web/sign-in",
                {"username": "apiuser", "password": "pass1234"},
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn("refresh", response.cookies)
            self.client.cookies.update(response.cookies)

            response = self.client.post("/api/auth/web/token-refresh")
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertTrue(data.get("access"))


class ApiOwnershipTests(TestCase):
    TEST_JWT_PRIVATE_KEY = ApiJwtFlowTests.TEST_JWT_PRIVATE_KEY
    TEST_JWT_PUBLIC_KEY = ApiJwtFlowTests.TEST_JWT_PUBLIC_KEY

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls._jwt_dir = tempfile.TemporaryDirectory()
        cls._private_key_path = os.path.join(cls._jwt_dir.name, "jwt-signing.pem")
        cls._public_key_path = os.path.join(cls._jwt_dir.name, "jwt-signing.pub")
        with open(cls._private_key_path, "w", encoding="utf-8") as handle:
            handle.write(cls.TEST_JWT_PRIVATE_KEY)
        with open(cls._public_key_path, "w", encoding="utf-8") as handle:
            handle.write(cls.TEST_JWT_PUBLIC_KEY)

    @classmethod
    def tearDownClass(cls):
        cls._jwt_dir.cleanup()
        super().tearDownClass()

    def setUp(self):
        self.client = Client()
        user_model = get_user_model()
        self.owner = user_model.objects.create_superuser(
            username="owner",
            password="ownerpass",
            email="owner@example.com",
        )
        self.other = user_model.objects.create_superuser(
            username="other",
            password="otherpass",
            email="other@example.com",
        )

        process = Process.objects.create(
            title="Sample process",
            description="Sample",
            enabled=True,
        )
        begin = Activity.objects.create(
            title="Start",
            kind="standard",
            process=process,
            autostart=False,
        )
        process.begin = begin
        process.save()

        self.sample = SampleModel.objects.create(
            text="Sample",
            number=1,
            requester=self.owner,
        )

    def _get_access_token(self, username, password):
        with override_settings(
            NINJA_SIMPLE_JWT={
                "USE_STATELESS_AUTH": True,
                "JWT_PRIVATE_KEY_PATH": self._private_key_path,
                "JWT_PUBLIC_KEY_PATH": self._public_key_path,
            }
        ):
            response = self.client.post(
                "/api/auth/web/sign-in",
                data=json.dumps({"username": username, "password": password}),
                content_type="application/json",
            )
        self.assertEqual(response.status_code, 200)
        access = response.json().get("access")
        self.assertTrue(access)
        return access

    def _start_payload(self):
        return {
            "process_name": "Sample process",
            "content_app_label": "sampleapp",
            "content_model": "samplemodel",
            "object_id": self.sample.id,
        }

    def test_start_process_denies_non_owner(self):
        access = self._get_access_token("other", "otherpass")
        response = self.client.post(
            "/api/protected/processes/start",
            data=json.dumps(self._start_payload()),
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {access}",
        )
        self.assertEqual(response.status_code, 403)

    def test_start_process_allows_owner(self):
        access = self._get_access_token("owner", "ownerpass")
        response = self.client.post(
            "/api/protected/processes/start",
            data=json.dumps(self._start_payload()),
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {access}",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("status"), "started")

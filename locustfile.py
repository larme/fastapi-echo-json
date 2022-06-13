from locust import HttpUser, between, task

class TensorFlow2MNISTLoadTestUser(HttpUser):

    wait_time = between(0.01, 2)

    @task
    def predict_image(self):
        self.client.post("/echo_json", json={"a": 1, "b": "blabla"}, timeout=1.0)

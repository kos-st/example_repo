import pytest
from selenium import webdriver
from pyvirtualdisplay import Display
from timeit import default_timer as timer
from pages.locators import Pushgateway
from prometheus_client import CollectorRegistry, push_to_gateway, Gauge, Counter

import jenkinsapi
from jenkinsapi.jenkins import Jenkins


def pytest_addoption(parser):
    """Определение параметров командной строки."""
    parser.addoption("--headless", action="store", help="При значении true открывает браузер в фоновом режиме"
                                                        "(для запуска в docker окружении или на сервере без графики)")


@pytest.fixture(scope='session')
def browser(request):
    options = webdriver.ChromeOptions()
    headless = request.config.getoption("headless")
    if headless == "true":
        display = Display(visible=0, size=(1920, 1080))
        display.start()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    else:
        options.add_argument("start-maximized")
    print('\nБраузер открывается...')
    browser = webdriver.Chrome(executable_path="./src/chromedriver", options=options)
    # browser = webdriver.Chrome(options=options)
    browser.set_page_load_timeout(45)
    yield browser
    print('\nБраузер закрывается...')
    browser.quit()
    if headless == "true":
        display.stop()


@pytest.fixture(scope="session", autouse=True)
def metrics():
    total_time_start = timer()
    metrics = Metrics()
    yield metrics
    print("Отправка метрик")
    total_time_end = timer()
    total_time = round(total_time_end - total_time_start)
    metrics.total_time.labels(Pushgateway.JOB_DESC, Pushgateway.PRODUCT).set(total_time)
    metrics.push()


class Metrics:
    def __init__(self):
        self.registry = CollectorRegistry()
        self.total_steps = Counter("uitest_total_steps", "uitest_total_steps", registry=self.registry, labelnames=["desc_job", "product"])
        self.total_time = Gauge("uitest_total_time", "uitest_total_time", registry=self.registry, labelnames=["desc_job", "product"])
        self.step = Gauge("uitest_step", "uitest_step", registry=self.registry, labelnames=["stepname", "desc_job", "desc_step", "priority", "product"])
        self.step_time = Gauge("uitest_step_time", "uitest_step_time", registry=self.registry, labelnames=["stepname", "desc_job", "desc_step", "product"])

    def push(self):
        push_to_gateway(Pushgateway.URL, job=Pushgateway.JENKINS_JOB, registry=self.registry)


def set_metrics(metrics, step_name, step_desc, total_time):
    metrics.step.labels(step_name, Pushgateway.JOB_DESC, step_desc, Pushgateway.PRIORITY, Pushgateway.PRODUCT).set(1)
    metrics.step_time.labels(step_name, Pushgateway.JOB_DESC, step_desc, Pushgateway.PRODUCT).set(total_time)
    metrics.total_steps.labels(Pushgateway.JOB_DESC, Pushgateway.PRODUCT).inc()


def set_fail_step_metric(metrics, step_name, step_desc, total_time):
    metrics.step.labels(step_name, Pushgateway.JOB_DESC, step_desc, Pushgateway.PRIORITY, Pushgateway.PRODUCT).set(0)
    metrics.step_time.labels(step_name, Pushgateway.JOB_DESC, step_desc, Pushgateway.PRODUCT).set(total_time)


def get_jenkins_build_number():
    server = Jenkins(Pushgateway.JENKINS_URL, username=Pushgateway.JENKINS_USERNAME, password=Pushgateway.JENKINS_PASSWORD)
    build_number = server.get_job(Pushgateway.JENKINS_JOB).get_last_buildnumber()
    return build_number

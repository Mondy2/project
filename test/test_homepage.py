import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from nav.Homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomePage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert actual_links == expected_links, "Validating NAV links text"

    def test_rail_links(self):
        homepage_nav = HomepageNav(self.driver)
        actual_links = homepage_nav.RAIL_LINK_TEXT()
        expected_links = homepage_nav.get_nav_links_text
        assert actual_links == expected_links



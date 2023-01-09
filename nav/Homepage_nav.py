from selenium.webdriver.remote.webelement import WebElement
from typing import List

from selenium_base.base import SeleniumBase


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav_links: str = "#mainNavigationFobs>li"
        self.NAV_LINK_TEXT = 'Women,Men,Kids & Baby,Home,Shoes,Handbags & Accessories,Jewelry,Sale'
        self.rail_links: str = "#rail-block rail-block-nav"
        self.RAIL_LINK_TEXT ='Order Tracking,Stores,Wedding Registry,Shipping To'



    def get_nav_links(self) -> List[WebElement]:
        return self.are_visiable('css', self.nav_links, 'Header Navigation links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = [link.text for link in nav_links]
        return ",".join(nav_links_text)


    def get_rail(self) -> WebElement:
        return self.is_visiable('css', self.rail_links, 'rail links')

    def get_rail_links(self):
        rail_links = self.get_rail()
        rail_links_text = [link.text for link in rail_links]
        return ",".join(rail_links_text)




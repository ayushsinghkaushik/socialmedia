class Test3:
    def testmethod(self, dropdown=None):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("http://127.0.0.1:5000/Verify")

        text = driver.find_element(By.XPATH, "/html/body/nav/div[2]/div[1]/form/input")
        text.send_keys("sandhya j")
        print("value is" + text.get_attribute("value"))
        assert text.get_attribute("value") == "sandhya j"
        time.sleep(5)

        text = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/form/input[1]")
        text.send_keys("HII EVERYONE")
        print("value is" + text.get_attribute("value"))
        assert text.get_attribute("value") == "HII EVERYONE"
        time.sleep(5)


from selenium import webdriver


if __name__ == "__main__":

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument('lang=en')
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-plugins-discovery")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--browser.download.folderList=2")
    options.add_argument("--browser.download.manager.showWhenStarting=False")
    # options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches",
                                    ["safebrowsing-disable-auto-update",
                                     "disable-client-side-phishing-detection",
                                     "enable-automation"])

    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--enable-javascript")

    driver = webdriver.Chrome(
        options=options, executable_path='/home/jerrine/Downloads/chromedriver')
    try:
        driver.get(
            "https://www.amazon.in/gp/product/B0791YHVMK/ref=s9_acss_bw_cg_PD203_2a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s="
            "merchandised-search-9&pf_rd_r=B8BK91W01NR5GD4Q8G5H&pf_rd_t=101&pf_rd_p=60db20ee-bfd7-40ac-a37f-"
            "bec5025428db&pf_rd_i=21703586031&th=1")

        xpath = '//*[@id="priceblock_ourprice"]'
        element = driver.find_element_by_xpath(xpath)
        price_for_firestick = float(str(element.text).split()[1].replace(',', ''))

        driver.get("https://www.amazon.in/dp/B079QQZZJK?ref=ods_ucc_echo_B079QQZZJK_nrc_ucc")
        xpath = '//*[@id="priceblock_ourprice"]'
        element = driver.find_element_by_xpath(xpath)
        price_for_firestick_4k = float(str(element.text).split()[1].replace(',', ''))

        print(price_for_firestick, price_for_firestick_4k)

        if price_for_firestick < 3999 or price_for_firestick_4k < 5999:
            print("Prices have reduced")
        else:
            print("No Change in prices")
    except Exception as e:
        if driver:
            driver.quit()
    finally:
        if driver:
            driver.quit()

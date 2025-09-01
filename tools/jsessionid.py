def get_jsessionid(page):
    cookies = page.context.cookies()
    for cookie in cookies:
        if cookie["name"].upper() == "JSESSIONID":
            return cookie["value"]
    return None
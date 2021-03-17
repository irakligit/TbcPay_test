
class CheckElements(object):
    #ელემენტის არსებობის ასერტი
    def check_locator_exists(locator):
        locator = locator.is_displayed()
        assert locator == bool(True), "element does not exist"
        return locator

    #ელემენტის ტექსტის არსებობის ასერტი
    def check_text_exists(locator, expected):
        locator = locator.text
        assert locator == expected, "element does not exist"












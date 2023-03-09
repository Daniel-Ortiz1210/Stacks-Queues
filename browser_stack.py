class WebPage:
    def __init__(self, link):
        self.link = link
        self.next = None


class WebBrowser:
    def __init__(self, link):
        web_page = WebPage(link=link)
        self.top = web_page
        self.bottom = web_page
        self.height = 1

    
    def print_stack(self):
        top = self.top
        while top is not None:
            print(top.link)
            top = top.next

    
    def push(self, link):
        new_page = WebPage(link)

        if self.height == 0:
            self.top = new_page
            self.bottom = new_page
        else:
            new_page.next = self.top
            self.top = new_page
        
        self.height += 1

        return new_page

    
    def pop(self):
        temp = self.top
        if self.height == 0:
            return None

        self.top = self.top.next
        temp.next = None
        self.height -= 1
        
        return temp

        

my_web_browser = WebBrowser(link="facebook.com")
my_web_browser.push(link="google.com")
my_web_browser.push(link="instagram.com")

my_web_browser.pop()

my_web_browser.print_stack()





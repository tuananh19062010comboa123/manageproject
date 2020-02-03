import tornado.ioloop
import tornado.web
import os

root = os.path.dirname(__file__)


# class RankerHandler(tornado.web.RequestHandler):
#     def get(self):
#         check = 1
#         self.render('index.html', count=check)


# class YourCart(tornado.web.RequestHandler):
#     def get(self):
#         self.render('your_cart.html')


# class BookDetail(tornado.web.RequestHandler):
#     def get(self):
#         self.render('book_detail.html')


# class Registration(tornado.web.RequestHandler):
#     def get(self):
#         self.render('register.html')

#     def post(self):
#         data = (self.request.body).decode("utf-8").split(" ")
#         print(data)


class Login(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        data = (self.request.body).decode("utf-8").split("=")
        password = data[2]
        email = data[1].split("&")[0]
        print(email, password)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            # (r"/ranker",RankerHandlerRedirect),
            # (r"/main-page", RankerHandler),
            (r"/login", Login)
            # (r"/registration", Registration),
            # (r"/book-detail", BookDetail),
            # (r"/your-cart", YourCart)

        ]

        settings = {
            "template_path": os.path.join(root, "templates"),
            "static_path": os.path.join(root, "static"),
            "debug": True
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    app = Application()
    app.listen(3000)  # 7783
    print("start server !!!")
    tornado.ioloop.IOLoop.current().start()

from django.utils.deprecation import MiddlewareMixin

class BookMiddlewareMixin(MiddlewareMixin):

    def process_request(self,request):
        print('请求1')

    def process_response(self,request,response):

        print('响应2')
        return response
class BookMiddlewareMixin2(MiddlewareMixin):

    def process_request(self,request):
        print('请求2')
        pass

    def process_response(self,request,response):

        print('响应1')

        return response